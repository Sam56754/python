# employee service program

class employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        
    def calculate_salary():
        return self.salary
    
class HourlyEmployee(employee):
    def __init__(self, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return f"{self.hourly_rate * self.hours_worked}"
    
class salaried_employee(employee):
    def __init__(self, monthly_salary):
        super().__init__(emp_id, name, salary)
        self.monthly_salary = monthly_salary
        
    def calculate_salary():
        salary = self.monthly_salary
        return salary

person = employee(12444567, "mark", 5000)
person_1 = HourlyEmployee(500, 8)
person_2 = salaried_employee(30000)

print(john.calculate_salary())
print(sam.calculate_salary())