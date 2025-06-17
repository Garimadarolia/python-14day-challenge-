class Employee:
    def __init__(self, name, salary, increment = 1):
        self.name = name
        self.salary = salary
        self.increment = increment
#properties
    def get_salary(self):
        return self.salary
    def get_increment(self):
        return self.increment
    def salary_increment(self):
        self.salary = float(self.salary * self.increment)

#user input section
try:
    name = input("Enter your name: ")
    salary_value = input("Enter your salary: ")
    increment_value = input("Enter your increment: ")

    salary = float(salary_value)

    if increment_value.strip() == "":
        emp = Employee(name, salary)
    else:
        increment = float(increment_value)
        emp = Employee(name, salary, increment)

    print(f"\n{name}'s original salary: Rs.{emp.get_salary()}")
    emp.salary_increment()
    print(f"Salary after increment: Rs.{emp.get_salary()}")

except ValueError as e:
    print(f"Input Error: {e}")