# Write your MySQL query statement below
SELECT e.name "Employee"
FROM 
    Employee e JOIN (SELECT id m_id, salary m_salary FROM Employee) m
    ON 
        e.managerId = m.m_id
WHERE
    e.salary>m.m_salary