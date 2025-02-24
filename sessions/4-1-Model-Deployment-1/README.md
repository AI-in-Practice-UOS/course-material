
# Session I

We trained a well-performing model: What comes next?

Today, we cover the serialization of machine learning models and how to make them available to our application(s). For that, we start building a minimal FastAPI Web API that serves predictions of our model via HTTP requests. In session II, we improve our app through input validation, error handling, documentation and more. We introduce Docker as a way to containerize our app and make it deployable to the cloud. Finally, in session III, we cover techniques to monitor our application and model.

## Outline

### Introduction and Serialization

- Introduction: Scope of the day and motivation
- Lecture: What is serialization and what are methods to serialize ML models in Python?
- Practice: Apply different serialization methods to a trained model.

### Web APIs and FastAPI

- Lecture: What is a Web API, including different types and the general anatomy?
- Lecture: Introducing FastAPI and a minimal example.
- Practice: Write a minimal FastAPI app with a chat endpoint.

### API Documentation and alternative Tools

- Walkthrough: Explore Swagger documentation of the API.
- Lecture: Alternative tools to host models.