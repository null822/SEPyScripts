# note that the Method Overriding task is identical to the Inheritance task, so it is only done once
from time import sleep
from typing import override

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
    
    def get_info(self):
        return f"EmployeeID:{self.id} Salary:{self.salary}"

class SalesEmployee(Employee):
    def __init__(self, id, salary, sales=0):
        super().__init__(id, salary)
        self.sales = sales
    
    @override
    def get_info(self):
        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"
