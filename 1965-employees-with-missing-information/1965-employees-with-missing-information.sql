# Write your MySQL query statement below

select d.employee_id from
(select e.employee_id, e.name, s.salary from Employees as e left join Salaries as s on e.employee_id=s.employee_id
union
select s.employee_id, e.name, s.salary from Employees as e right join Salaries as s on e.employee_id=s.employee_id) as d

where d.name is null or d.salary is null order by d.employee_id asc