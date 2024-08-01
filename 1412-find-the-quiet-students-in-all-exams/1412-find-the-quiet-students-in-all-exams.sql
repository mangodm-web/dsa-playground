WITH min_max_score_list AS (
    SELECT 
    exam_id,
    MIN(score) AS min_score,
    MAX(score) AS max_score
    FROM Exam
    GROUP BY exam_id
)

SELECT 
    Student.student_id,
    Student.student_name
FROM exam
LEFT JOIN Student
    USING (student_id)
LEFT JOIN min_max_score_list
    ON Exam.exam_id = min_max_score_list.exam_id
    AND (Exam.score = min_max_score_list.min_score OR Exam.score = min_max_score_list.max_score)
GROUP BY
    Student.student_id,
    Student.student_name  
HAVING COUNT(min_max_score_list.exam_id) = 0
ORDER BY Student.student_id;
