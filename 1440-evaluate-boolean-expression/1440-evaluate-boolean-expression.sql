SELECT
    Expressions.*,
    CASE
        WHEN Expressions.Operator = '>' AND V1.Value > V2.Value THEN 'true'
        WHEN Expressions.Operator = '<' AND V1.Value < V2.Value THEN 'true'
        WHEN Expressions.Operator = '=' AND V1.Value = V2.Value THEN 'true'
        ELSE 'false'
    END AS Value
FROM Expressions
LEFT JOIN Variables AS V1
    ON Expressions.Left_operand = V1.Name
LEFT JOIN Variables AS V2
    ON Expressions.Right_operand = V2.Name;
