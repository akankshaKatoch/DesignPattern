# Liskov Substitution Principle (LSP)

The **Liskov Substitution Principle** is one of the five SOLID principles of object-oriented design. It states that:

> *Objects of a superclass should be replaceable with objects of a subclass without breaking the application.*

In other words, subclasses should extend the behavior of a base class without changing its original functionality. If a program works with a base class, it should also work with any derived class.

## Why is LSP Important?

- Ensures code reusability and flexibility.
- Prevents unexpected behavior when using subclasses.
- Makes code easier to maintain and extend.

## Example

Suppose you have a base class `Bird` and a derived class `Penguin`:

```csharp
class Bird {
    public virtual void Fly() {
        Console.WriteLine("Bird is flying");
    }
}

class Sparrow : Bird {
    public override void Fly() {
        Console.WriteLine("Sparrow is flying");
    }
}

class Penguin : Bird {
    public override void Fly() {
        throw new NotSupportedException("Penguins can't fly");
    }
}
```

Here, substituting `Penguin` for `Bird` breaks the program because `Penguin.Fly()` throws an exception. This violates LSP.

### Correct Approach

Refactor the design so that only birds that can fly inherit from a `FlyingBird` class:

```csharp
class Bird { }

class FlyingBird : Bird {
    public virtual void Fly() {
        Console.WriteLine("Flying bird is flying");
    }
}

class Sparrow : FlyingBird {
    public override void Fly() {
        Console.WriteLine("Sparrow is flying");
    }
}

class Penguin : Bird {
    // No Fly method, as penguins can't fly
}
```

Now, substituting any `FlyingBird` subclass will not break the program, and LSP is maintained.

## Usage

- When designing class hierarchies, ensure derived classes do not remove base class behavior.
- Avoid overriding methods in a way that changes expected outcomes.
- Use interfaces or abstract classes to separate behaviors when necessary.

**Summary:**  
LSP helps you create robust, maintainable, and extensible code by ensuring that subclasses can stand in for their base classes without causing errors.
