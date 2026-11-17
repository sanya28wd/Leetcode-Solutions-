# Write your MySQL query statement below
select name, sum(amount) as balance from Transactions as t left join Users as u on t.account=u.account group by t.account having sum(amount)>10000
