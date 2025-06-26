The **Single Responsibility Principle (SRP)** is one of the five SOLID principles of object-oriented design. It states that a class should have only one reason to change, meaning it should have only one responsibility or job. By ensuring that each class focuses on a single task, your code becomes easier to understand, maintain, and extend.

**Key Points:**
- A class should encapsulate only one responsibility.
- Changes to a class should result from only one kind of change in the software's requirements.
- Adhering to SRP reduces the risk of unintended side effects when modifying code.

**Example:**  
If a class handles both data persistence and business logic, changes in data storage requirements could force changes to business logic code. By separating these concerns into different classes, each class remains focused and easier to manage.