# Follows Single Responsibility Principle
class EmployeeSRP:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class EmployeeFileSaver:
    @staticmethod
    def save_to_file(employee, filename):
        with open(filename, 'w') as file:
            file.write(employee.get_details())

class EmployeeEmailSender:
    @staticmethod
    def send_email(employee, email_address):
        print(f"Sending employee details to {email_address}: {employee.get_details()}")

# Example usage of correct code
emp_srp = EmployeeSRP("Jane Smith", "Manager", 90000)
EmployeeFileSaver.save_to_file(emp_srp, "employee_srp.txt")
EmployeeEmailSender.send_email(emp_srp, "jane.smith@example.com")