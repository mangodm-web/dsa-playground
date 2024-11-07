WITH mandatory_courses_list AS (
    SELECT 
        c.course_id, 
        c.major
    FROM courses c
    WHERE c.mandatory = 'Yes'
), 
elective_courses_list AS (
    SELECT 
        c.course_id, 
        c.major
    FROM courses c
    WHERE c.mandatory = 'No'
),
student_mandatory_list AS (
    SELECT 
        e.student_id, 
        s.major
    FROM enrollments e
    JOIN mandatory_courses_list m 
        ON e.course_id = m.course_id
    JOIN students s 
        ON e.student_id = s.student_id 
       AND s.major = m.major
    WHERE e.grade = 'A'
    GROUP BY e.student_id, s.major
    HAVING COUNT(DISTINCT e.course_id) = (SELECT COUNT(*) 
                                          FROM mandatory_courses_list 
                                          WHERE major = s.major)
),
student_elective_list AS (
    SELECT e.student_id, s.major
    FROM enrollments e
    JOIN elective_courses_list ec 
        ON e.course_id = ec.course_id
    JOIN students s 
        ON e.student_id = s.student_id 
       AND s.major = ec.major
    WHERE e.grade IN ('A', 'B')
    GROUP BY e.student_id, s.major
    HAVING COUNT(DISTINCT e.course_id) >= 2
),
average_gpa_list AS (
    SELECT e.student_id, AVG(e.GPA) AS avg_gpa
    FROM enrollments e
    GROUP BY e.student_id
    HAVING AVG(e.GPA) >= 2.5
)
SELECT DISTINCT sm.student_id
FROM student_mandatory_list sm
JOIN student_elective_list se 
    ON sm.student_id = se.student_id
JOIN average_gpa_list ag 
    ON sm.student_id = ag.student_id
ORDER BY sm.student_id;
