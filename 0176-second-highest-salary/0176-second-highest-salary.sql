# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from
(select salary, dense_rank() over(order by salary desc) as HighestSalary from Employee)
as ranked
 where HighestSalary=2