Dependency Inversion Principle

The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces or abstract classes). This helps in reducing tight coupling between components and makes the system more flexible and easier to maintain.

**Key Points:**
- High-level modules: Contain complex logic and policies.
- Low-level modules: Contain detailed implementation.
- Abstractions: Interfaces or abstract classes that define contracts.

## Practical Example (in C#)

Suppose you have a reporting application that sends notifications via email.

**Without DIP:**

```csharp
public class EmailSender
{
    public void SendEmail(string message)
    {
        // Code to send email
    }
}

public class ReportGenerator
{
    private EmailSender _emailSender = new EmailSender();

    public void GenerateReport()
    {
        // Generate report logic
        _emailSender.SendEmail("Report generated");
    }
}
```
Here, `ReportGenerator` (high-level) depends directly on `EmailSender` (low-level).

**With DIP:**

```csharp
public interface IMessageSender
{
    void Send(string message);
}

public class EmailSender : IMessageSender
{
    public void Send(string message)
    {
        // Code to send email
    }
}

public class ReportGenerator
{
    private readonly IMessageSender _messageSender;

    public ReportGenerator(IMessageSender messageSender)
    {
        _messageSender = messageSender;
    }

    public void GenerateReport()
    {
        // Generate report logic
        _messageSender.Send("Report generated");
    }
}
```
Now, `ReportGenerator` depends on the abstraction `IMessageSender`, not on the concrete `EmailSender`. This allows you to easily swap out `EmailSender` for another implementation (e.g., SMS sender) without changing the `ReportGenerator` code.

**Benefits:**
- Easier to extend and maintain.
- Promotes loose coupling.
- Facilitates testing (e.g., by injecting mock implementations).

