CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select max(salary) as 'getNthHighestSalary(N)' from (
        select salary, dense_rank() over(order by salary desc) as highest from Employee
      ) as ranked
      where highest=N

  );
END