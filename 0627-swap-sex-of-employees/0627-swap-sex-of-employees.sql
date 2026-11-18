# Write your MySQL query statement below
update salary 
set sex = Case 
when sex='m' then 'f'
when sex='f' then 'm'
else sex
end 

