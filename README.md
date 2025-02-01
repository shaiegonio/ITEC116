Laboratory Activity #1: Introduction to FastAPI

This code defines a FastAPI application with a route that calculates the factorial of a number provided in the URL. It starts by importing FastAPI and creating an instance of the FastAPI application. The route listens for GET requests at the path `/factorial/{starting_number}`, where `{starting_number}` is a dynamic part of the URL, representing the number for which the factorial will be calculated. The function `factorial` takes this number as an argument, checks if the number is `0` (in which case it returns `{"result": False}`), and then calculates the factorial by multiplying the number by all the integers less than it down to `1`. The result is stored in the variable `factor` and returned as a dictionary with the key `"result"`. For example, if the URL is `/factorial/5`, the API will return `{"result": 120}`, which is the factorial of `5`.


Laboratory Activity #2: Working with HTTP actions and API parameters

This code creates a simple web API using FastAPI to manage user data, including operations like retrieving, adding, updating, and deleting user information. It begins by importing necessary modules: `FastAPI` for creating the API, `BaseModel` from Pydantic for data validation, and `Optional` from the `typing` module to allow optional parameters. The `User` class, which extends `BaseModel`, defines the structure of a user, requiring a `user_id` and `name`. A sample list, `users_db`, is used to represent a database of users.

The API includes several endpoints: 
1. GET `/users`: This endpoint retrieves all users from `users_db` or, if a `user_id` query parameter is provided, it returns the user with that specific `user_id`. If the user is not found, it returns an error message.
2. POST `/users`: This endpoint allows a new user to be added to the `users_db`. It takes a `User` object in the request body. Before adding the user, it checks if the `user_id` already exists in the database, and if it does, it returns an error message. Otherwise, it appends the new user to the list.
3. DELETE `/users/{user_id}`: This endpoint deletes a user based on the provided `user_id`. It checks if the user exists in `users_db`, removes the user if found, and returns the deleted user's data. If the user is not found, it returns an error message.
4. PUT `/users/{user_id}`: This endpoint allows updating a user's information. It takes a `user_id` as part of the URL and a `User` object in the request body. If the `user_id` matches an existing user, it updates the user's `name` and returns the updated data. If the user is not found, it returns an error message.

The API provides basic CRUD (Create, Read, Update, Delete) functionality, ensuring users can be managed efficiently with proper error handling and validation.


Laboratory Activity #3: Working with JSON

This code creates a FastAPI application that interacts with a remote JSON API (jsonplaceholder.typicode.com) to fetch posts and comments, and then formats the data according to the user's request. The application defines several endpoints, each with specific functionality. The first two endpoints, **GET `/posts/`** and **GET `/comments/`**, fetch posts and comments from the remote API. If a `postId` is provided, they return data for that specific post or comment; otherwise, they return all posts or comments. The third endpoint, **GET `/formatted_posts/{userID}`**, formats the posts for a specific user by filtering posts based on the `userID`, and returns a simplified structure with the post title and body. The fourth endpoint, **GET `/formatted_comment/{postID}`**, formats the comments for a given post by filtering comments based on the `postID`, and returns a structured response with the commenter's email, name, and the comment body. Lastly, the **GET `/detailed_post/{userID}`** endpoint combines the posts and comments data, organizing them in a detailed format. It filters posts for a specific `userID` and for each post, it appends the related comments, presenting them with the commenter's email, name, and the comment body. The code demonstrates how to fetch, filter, and structure data from an external API, and provides an organized and formatted response for the user.


**Laboratory Activity #4: Advanced API Implementation**

This code implements a FastAPI application with two versions of an API for managing tasks, with functionality for adding, fetching, modifying, and deleting tasks. The application uses a simple in-memory database to store tasks. The code also includes API key authentication for version 2 of the API to ensure that only requests with a valid API key can interact with it. In version 1, there are endpoints to fetch a task by its ID (`GET /apiv1/tasks/{task_id}`), add a new task (`POST /apiv1/tasks`), delete a task (`DELETE /apiv1/tasks/{task_id}`), and modify an existing task (`PATCH /apiv1/tasks/{task_id}`). These endpoints perform basic CRUD operations on a list of tasks. Version 2 of the API has similar functionality, but it adds an extra layer of security by validating the API key in each request using a dependency (`validate_api_key`). The application also uses Pydantic models for task validation and ensures that task details like title, description, and completion status are properly handled. Additionally, the second part of the code searches through files in the directory for any mention of "API_KEY" and prints the lines where it is found, likely for security or configuration purposes. This code provides a basic framework for a task management system with API versioning and authentication, demonstrating how to handle API requests with security measures in FastAPI.


Laboratory Activity #5: Deploying API in Cloud

This code is a simple FastAPI application that defines an API for managing tasks, with two versions (v1 and v2). It includes endpoints for creating, reading, updating, and deleting tasks. The tasks are stored in two separate in-memory databases (`task_db_v1` and `task_db_v2`). The application also uses API key authentication for version 2, ensuring that only requests with a valid API key can access certain endpoints. The task data is managed using a Pydantic model, which ensures the correct structure and validation for each task (with fields like title, description, and completion status). Version 1 of the API has endpoints for fetching a task by ID, adding a new task, deleting a task, and updating an existing task. Version 2 offers the same functionality but includes additional security through the API key validation. There's also a general `/protected-route` endpoint that demonstrates the use of API key authentication. The code also includes a root endpoint that returns a basic "Hello, Render!" message, showing that the server is up and running. The FastAPI framework makes it easy to set up this RESTful API, allowing the app to manage tasks and perform CRUD operations efficiently.
