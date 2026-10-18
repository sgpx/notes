### Core .NET Concepts

1. **C# Basics**  
   **Exercise**: Write a C# console application that prompts the user for their name and age, then prints out a greeting message including their age in 5 years.

2. **Object-Oriented Programming (OOP)**  
   **Exercise**: Create a class `Car` with properties like `Make`, `Model`, `Year`, and methods such as `StartEngine` and `StopEngine`. Instantiate the class and call its methods.

3. **Collections & Data Structures**  
   **Exercise**: Create a C# program that uses a `Dictionary<string, int>` to store and look up phonebook entries (name and phone number). Print out all the entries.

4. **LINQ (Language Integrated Query)**  
   **Exercise**: Create a list of integers and use LINQ to filter out all the even numbers, sort them, and display them in ascending order.

5. **Delegates and Events**  
   **Exercise**: Implement a `Button` class with a `Click` event. Create a method that subscribes to the event and prints "Button clicked!" when the button is clicked.

6. **Exceptions and Error Handling**  
   **Exercise**: Write a C# program that reads a number from the user, and catches any exceptions that occur (e.g., user inputs non-numeric data). Handle the error gracefully and display an error message.

7. **Asynchronous Programming (Async/Await)**  
   **Exercise**: Write an async method that fetches data from a mock API (e.g., `Task.Delay(2000)`) and returns a string. Call this method and output the result once it's complete.

8. **Dependency Injection (DI)**  
   **Exercise**: Create an interface `IGreetingService` with a method `Greet()`. Implement it in a class `GreetingService`. Set up DI in `Program.cs` and inject `GreetingService` into a controller to use `Greet()`.

9. **Reflection**  
   **Exercise**: Write a method that uses reflection to display the properties and methods of any given class.

10. **Garbage Collection**  
   **Exercise**: Create a class that implements `IDisposable`. Write a program that uses this class and demonstrate how `Dispose()` is called to release unmanaged resources.

11. **Threading and Parallel Programming**  
   **Exercise**: Write a program that uses `Task.Run()` to execute two methods in parallel. Each method should print a message after waiting for a short time.

12. **Interfaces and Abstract Classes**  
   **Exercise**: Create an abstract class `Shape` with a method `Draw()`. Derive classes `Circle` and `Rectangle` from `Shape`, each implementing `Draw()` differently. Instantiate them and call `Draw()`.

13. **Generics**  
   **Exercise**: Create a generic method `Swap<T>(T a, T b)` that swaps two variables of any type and prints their values before and after the swap.

14. **Unit Testing and Mocking**  
   **Exercise**: Write a unit test for a method `Add(int a, int b)` in a class `Calculator`. Use a mocking framework like Moq to mock a dependency (e.g., a logging service).

15. **Versioning & .NET SDKs**  
   **Exercise**: Create a simple console app, then use the .NET CLI to change the target framework version in the `.csproj` file, and update it to a new SDK version.

16. **Data Access with ADO.NET**  
   **Exercise**: Write a console application that connects to a SQL Server database using ADO.NET, retrieves data from a table, and displays the results in the console.

17. **Entity Framework Core (EF Core)**  
   **Exercise**: Create a `Book` entity with properties like `Title` and `Author`. Use EF Core to create a database, add a record, and retrieve all books from the database.

18. **Configuration Management**  
   **Exercise**: Create an ASP.NET Core web app and store a configuration value (e.g., API key) in `appsettings.json`. Load it into your app and display it in the browser.

19. **App Startup and Configuration**  
   **Exercise**: In an ASP.NET Core application, configure services like logging and add custom middleware to the pipeline in `Startup.cs`.

20. **Authentication & Authorization**  
   **Exercise**: Implement cookie-based authentication in an ASP.NET Core app. Protect a route so that only authenticated users can access it.

21. **Logging**  
   **Exercise**: Create an ASP.NET Core console application that logs various messages (info, warning, error) using the built-in logging framework. Write these logs to a file.

22. **Globalization and Localization**  
   **Exercise**: Create an ASP.NET Core web app that supports multiple languages. Provide a button to switch between languages and display the localized content on the page.

23. **Middleware**  
   **Exercise**: Write a custom middleware that logs the time taken for each request to be processed and adds it to the response headers.

24. **Caching**  
   **Exercise**: Implement in-memory caching in an ASP.NET Core web app to store and retrieve a list of products from memory instead of querying a database on every request.

25. **WebSockets and SignalR**  
   **Exercise**: Create a SignalR chat app that allows multiple clients to send and receive messages in real-time.

26. **Security Fundamentals**  
   **Exercise**: Set up SSL/TLS in an ASP.NET Core application. Ensure that all requests are redirected to HTTPS and demonstrate an HTTPS-only environment.

---

### ASP.NET Core Specific Topics

27. **ASP.NET Core Overview**  
   **Exercise**: Create a simple ASP.NET Core MVC web application with a home page and a contact page, and configure routing between the pages.

28. **Controllers & Actions**  
   **Exercise**: Create a controller `HomeController` with actions `Index()` and `Contact()`. Return views from these actions and display data (e.g., user’s name) dynamically.

29. **Model Binding and Validation**  
   **Exercise**: Create a model `Person` with properties `Name` and `Age`. In a controller action, bind the model to form data and perform validation to ensure `Age` is a positive number.

30. **Razor Pages**  
   **Exercise**: Create a Razor Page that accepts a user's name via a form and displays a personalized greeting message on the same page.

31. **Routing**  
   **Exercise**: Define custom routes for an ASP.NET Core MVC app, like `/Products/Details/{id}` and `/Orders/{orderId}/Status`, and use route parameters in the controller actions.

32. **Views and Razor Syntax**  
   **Exercise**: Create a `Product` model with properties `Name`, `Price`, and `Description`. Display the product details in a Razor view and use Razor syntax for dynamic content.

33. **Static Files**  
   **Exercise**: Create a simple web page that includes static assets (CSS and JavaScript files) stored in the `wwwroot` folder. Style the page and add interactivity using JavaScript.

34. **Dependency Injection in ASP.NET Core**  
   **Exercise**: Create a service `ILoggerService` that logs messages to a file. Inject this service into a controller and use it to log messages whenever the user accesses a page.

35. **Action Filters & Result Filters**  
   **Exercise**: Implement an action filter that logs the execution time of controller actions. Apply the filter to one or more actions and display the execution time in the console.

36. **RESTful API Development**  
   **Exercise**: Create a RESTful API that supports CRUD operations for managing products (using a `Product` model). Implement GET, POST, PUT, and DELETE methods in a `ProductsController`.

37. **API Documentation with Swagger**  
   **Exercise**: Add Swagger to an ASP.NET Core API project. Generate and view the API documentation in the Swagger UI, and add example responses to the API methods.

38. **HTTP Clients and Web APIs**  
   **Exercise**: Create an ASP.NET Core service that makes an HTTP request to an external API (e.g., a weather API) and displays the results in a web page.

39. **Versioning APIs**  
   **Exercise**: Implement API versioning in an ASP.NET Core app using URL versioning (e.g., `/api/v1/products`). Add two versions of the `ProductsController` with different methods.

40. **State Management**  
   **Exercise**: Implement session state in an ASP.NET Core web application. Store the user's name in session and display a personalized greeting message across different pages.

41. **Cross-Origin Resource Sharing (CORS)**  
   **Exercise**: Set up CORS in an ASP.NET Core API to allow cross-origin requests from a frontend application running on a different domain.

42. **File Uploads and Downloads**  
   **Exercise**: Create a form in an ASP.NET Core web app that allows users to upload files. Save the file on the server and provide a download link once the upload is complete.

43. **Background Services**  
   **Exercise**: Implement a background service that performs an operation (e.g., sending an email) periodically using `IHostedService` in an ASP.NET Core app.

44. **Identity and ASP.NET Core Identity**  
   **Exercise**: Set up ASP.NET Core Identity in an MVC application, allowing users to

 register, log in, and view their profile. Add role-based authorization to restrict access to certain pages.

45. **Custom Middleware in ASP.NET Core**  
   **Exercise**: Write a custom middleware that checks if the user is authenticated before processing the request. If not, return a 401 Unauthorized status.

46. **Environment Configuration**  
   **Exercise**: Configure an ASP.NET Core application to load different settings based on the environment (Development, Staging, Production) using `appsettings.{Environment}.json`.

47. **Data Protection**  
   **Exercise**: Use the `IDataProtectionProvider` to encrypt and decrypt a sensitive string (e.g., a password) and store it securely in a database.

48. **Health Checks**  
   **Exercise**: Add a health check endpoint in an ASP.NET Core web app that checks the health of the app and its dependencies (e.g., database, cache).

49. **SignalR in ASP.NET Core**  
   **Exercise**: Create a simple chat app using SignalR that allows multiple users to send and receive messages in real-time.

50. **Deployment**  
   **Exercise**: Deploy an ASP.NET Core application to Azure. Configure continuous integration (CI) with GitHub Actions or Azure DevOps and ensure that the app runs smoothly in the cloud.

---

These exercises will help solidify your understanding of the core concepts in both .NET and ASP.NET Core while giving you practical experience with each topic.
