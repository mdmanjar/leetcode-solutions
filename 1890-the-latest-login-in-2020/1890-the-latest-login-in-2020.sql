# Write your MySQL query statement below
SELECT t.user_id,
       MAX(t.time_stamp) as last_stamp
FROM Logins t
WHERE YEAR(t.time_stamp)=2020  
GROUP BY t.user_id
;