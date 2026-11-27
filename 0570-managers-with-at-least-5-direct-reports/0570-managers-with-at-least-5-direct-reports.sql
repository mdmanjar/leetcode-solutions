# Write your MySQL query statement below
WITH temp AS (
    SELECT
         e1.id AS emp_id,
         COUNT(*) AS total_count
    FROM Employee e1
    JOIN Employee e2
    ON e1.id=e2.managerId 
    GROUP BY e1.id
    having count(*)>=5
)
SELECT 
     e.name
FROM Employee e
JOIN temp t
ON e.id=t.emp_id;