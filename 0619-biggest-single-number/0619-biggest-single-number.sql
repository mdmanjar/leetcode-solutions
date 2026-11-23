# Write your MySQL query statement below
select max(num) as 'num' from (select num,count(*) as ct from MyNumbers group by num having ct=1) as temp;