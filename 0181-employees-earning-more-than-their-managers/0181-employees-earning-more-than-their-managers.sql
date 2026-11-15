# Write your MySQL query statement below
select e.name as Employee
from employee as e
where managerId is not null and salary>(select salary from employee e1 where e.managerId=e1.id);