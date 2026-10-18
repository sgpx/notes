## hello world

Thanks for the structure—your project is correctly scaffolded as a standard Maven-based Spring Boot application with the package name `com.example.demo`.

Let’s **continue from here** and add the `"Hello, World!"` controller step-by-step **based on your existing project structure**.

---

## ✅ Step-by-Step: Add a "Hello, World!" Controller to Your Project

---

### 🔹 Step 1: Add the Controller Class

Create a new Java file inside the `com.example.demo` package:

**Path:**
`src/main/java/com/example/demo/HelloWorldController.java`

**Contents:**

```java
package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloWorldController {

    @GetMapping("/")
    @ResponseBody
    public String hello() {
        return "Hello, World!";
    }
}
```

---

### 🔹 Step 2: Confirm Your `DemoApplication.java`

Open this file:

**Path:**
`src/main/java/com/example/demo/DemoApplication.java`

Make sure it contains this code:

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

This is already there based on your structure, but confirm it's unchanged.

---

### 🔹 Step 3: Run the Application

In **VS Code terminal**, from the root of your project (where `pom.xml` is located), run:

```bash
./mvnw spring-boot:run
```

If you're using Windows:

```cmd
mvnw.cmd spring-boot:run
```

Or with global Maven installed:

```bash
mvn spring-boot:run
```

---

### 🔹 Step 4: View the Output in Your Browser

Go to:

```
http://localhost:8080/
```

You should see:

```
Hello, World!
```

====

# controller example

```java
package com.example.springtut;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class TutController {
    @GetMapping("/ok")
    @ResponseBody
    public String hello() {
        return "OK123";
    }
}
```


```java
package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;
import java.util.Map;

@RestController
public class MessageController {

    @GetMapping("/api/message")
    public Map<String, String> getMessage() {
        Map<String, String> response = new HashMap<>();
        response.put("message", "Hello, welcome to Spring Boot!");
        return response;
    }
}
```

```java
package com.example.springtut;

import java.util.HashMap;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class TutController {
    @GetMapping("/ok")
    @ResponseBody
    public HashMap<String, String> hello() {
        HashMap<String, String> resp = new HashMap<>();
        resp.put("lol","123");
        return resp;
    }
}
```

```
package com.example.springtut;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TutController {
    @GetMapping("/ok")
    public String hello(@RequestParam(name = "myfield", defaultValue = "myval") String name) {
        return "hello " + name;
    }
}

// curl localhost:8080/ok<=> gives "hello myval"
// curl localhost:8080/ok?myfield=foobar <=> gives "hello foobar"
```

# ====
# ====

```
package com.example.springtut;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

class RX {
    public String unm;
    public String addr;

    public RX() {

    }
}

@RestController
@RequestMapping("/api")
public class TutController {
    @PostMapping("/echo")
    public RX echoUser(@RequestBody RX rx1) {
        return rx1;
    }
}
```
