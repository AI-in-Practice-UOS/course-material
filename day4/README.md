# AI in Practice - Day 4

We trained a well-performing model: What comes next?

Today, we cover the serialization of machine learning models and how to make them available to our application(s). For that, we start building a minimal FastAPI Web API that serves predictions of our model via HTTP requests. In session II, we improve our app through input validation, error handling, documentation and more. We introduce Docker as a way to containerize our app and make it deployable to the cloud. Finally, in session III, we cover techniques to monitor our application and model.

## Requirements

- Clone this repository to your local machine
- Set up a Python environment to work in
- Install required packages `pip install -r requirements.txt`
- Install Docker Engine (or Desktop)

## Session I

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

## Session II

### FastAPI Improvements

- Lecture: Improve API through input validation, error handling and logging.
- Lecture: Adding basic testing and simple authentication.
- Practice: Implement the improvements into the minimal FastAPI.

### Containerization

- Lecture: What is containerization and what is the purpose?
- Lecture: Introducing Docker for containerization of FastAPI.
- Practice: Build Docker image for the FastAPI app and run locally.
- Walkthrough: Deploy docker image to a cloud provider.

## Session III

### Monitoring

- Lecture: What is monitoring and the motivation behind it?
- Lecture: Different monitoring tools and techniques.
- Practice/Walkthrough: Exploration of a monitoring tool.

### Performance Improvements

- Lecture: What are model optimization techniques for inference?
- Lecture/Walkthrough: What are other ways to improve performance?
