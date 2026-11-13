CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  -- Declare a variable to store N - 1 for the OFFSET clause
  DECLARE offset_val INT;
  SET offset_val = N - 1;
  
  RETURN (
      # Write your MySQL query statement below
      SELECT DISTINCT salary 
      FROM Employee 
      ORDER BY salary DESC 
      LIMIT 1 OFFSET offset_val
  );
END;