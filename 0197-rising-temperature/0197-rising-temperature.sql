# Write your MySQL query statement below
SELECT 
     w1.id
FROM  Weather w1
JOIN Weather w2
ON DATE_SUB(DATE(w1.recordDate),interval 1 day)=DATE(w2.recordDate)
WHERE (w1.temperature-w2.temperature)>0;
