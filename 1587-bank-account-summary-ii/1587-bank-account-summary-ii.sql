# Write your MySQL query statement below
SELECT 
     u.name AS NAME,
     SUM(amount) as BALANCE
FROM Users AS u
JOIN Transactions t
ON u.account=t.account
GROUP BY u.name
HAVING SUM(amount)>10000;