select 
    e1.name AS Employee
    -- e1.Salary AS Employee_Salary, 
    -- e2.name AS MNGR_Name, 
    -- e2.Salary AS MNGR_Salary
from 
    Employee e1 left join Employee e2 on e1.managerID = e2.id 
where
    e1.Salary > e2.Salary
