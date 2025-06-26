class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    # Incorrect code: Violation of Single Responsibility Principle
    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.get_details())

    def send_email(self, email_address):
        print(f"Sending employee details to {email_address}: {self.get_details()}")

# Example usage of incorrect code
emp = Employee("John Doe", "Developer", 70000)
emp.save_to_file("employee.txt")
emp.send_email("john.doe@example.com")