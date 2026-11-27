# Write your MySQL query statement below
SELECT 
     user_id,
     concat(upper(LEFT(name,1)),lower(RIGHT(name,LENGTH(name)-1))) as name
from Users
ORDER BY user_id;
