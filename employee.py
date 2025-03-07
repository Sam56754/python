# employee service program

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.salary = 0
        
    def calculate_salary(self):
        return self.salary
    
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return f"{self.name} earns Ksh {self.hourly_rate * self.hours_worked} working {self.hours_worked}hrs"
    
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary
        
    def calculate_salary(self):
        self.salary = self.monthly_salary
        return f"{self.name} is a monthly salaried employee earning Ksh {self.salary}"

person_1 = HourlyEmployee(127843, "john", 500, 8)
person_2 = SalariedEmployee(8969973, "mary", 30000)

print(person_1.calculate_salary())
print(person_2.calculate_salary())