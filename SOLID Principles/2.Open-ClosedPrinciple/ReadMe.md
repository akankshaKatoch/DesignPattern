## Open/Closed Principle (OCP)

The Open/Closed Principle is one of the five SOLID principles of object-oriented design. It states that:

> **Software entities (such as classes, modules, and functions) should be open for extension, but closed for modification.**

### What does this mean?

- **Open for extension:** You should be able to add new functionality to a module or class without changing its existing code.
- **Closed for modification:** Once a class or module has been developed and tested, you should not need to modify its source code to add new features.

### Why is it important?

- **Extensibility:** New requirements can be implemented by adding new code, not by changing existing, stable code.
- **Maintainability:** Reduces the risk of introducing bugs when requirements change.
- **Reusability:** Encourages the use of abstractions and interfaces, making code more reusable.

### How to achieve OCP?

- Use **abstraction** (interfaces or abstract classes) to define contracts.
- Rely on **polymorphism** to allow new behaviors via subclassing or composition.
- Avoid tightly coupling code to specific implementations.

**Example:**  
Instead of modifying a class to support new features, create new subclasses or strategies that extend the original behavior.

