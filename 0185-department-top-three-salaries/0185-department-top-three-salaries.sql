# Write your MySQL query statement below
SELECT d1.Name AS "Department", e1.Name AS "Employee", e1.Salary
FROM Department d1

INNER JOIN Employee e1 ON d1.Id = e1.departmentId
INNER JOIN Department d2 ON d1.Id = d2.Id

LEFT JOIN Employee E2 ON d2.Id = e2.departmentId AND e1.Salary < e2.Salary
GROUP BY d1.Name, e1.Name, e1.Salary
HAVING COUNT(DISTINCT(e2.Salary)) < 3