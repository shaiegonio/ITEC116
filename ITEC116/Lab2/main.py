# Needed modules
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Instantiates the FastAPI class
app = FastAPI()

# Handles the format of the object instantiated by the User class
# This extends the BaseModel to ensure proper mapping of the FastAPI to the
# User class
class User(BaseModel):
    user_id: int
    name: str

# Sample data to represent users
users_db = [
    {"user_id": 1, "name": "John Doe"},
    {"user_id": 2, "name": "Jane Smith"},
    {"user_id": 3, "name": "Alice Johnson"}
]

# GET implementation
@app.get("/users") # Set the decorator to implement GET on endpoint /users
def read_users(user_id: Optional[int] = None): # Takes a query parameter named user_id that can take an integer or no value
    # Check if the user_id is provided
    if user_id:        
        # Find user by user_id
        for u in users_db:
            # If the user_id matches the value in the users_db
            # Return value of user
            if u["user_id"] == user_id:
                return {"status": "ok", "result" : u}
        
        # Return value if user is not found
        return {"error": "User not found"}
    
    # Return all users if no user_id is provided
    return {"status": "ok", "result" : users_db}

# POST implementation
@app.post("/users") # Set the decorator to implement POST on endpoint /users
def create_user(user: User): # Takes a request that contains a user object based on the User class
    # Check of user ID is available in the users_db list
    # IF already existing, return error
    if any(u['user_id'] == user.user_id for u in users_db):
        return {"error": "User ID already existing"}
    
    # If user_id is not yet existing, we append the passed User object to the users_db list
    # Take note that we are casting the user object to dict so that it matches the data type
    # Of the contents of users_db
    users_db.append(dict(user))
    return {"status": "ok"}

# DELETE implementation
@app.delete("/users/{user_id}")
def delete_user(user_id: int): # Takes a path parameter user_id that can take integer values
     # Check if the user_id is provided
    if user_id:
        # Find user by user_id
        for idx, u in enumerate(users_db):
            # If the user_id in the users_db matches the inputted user_id from the parameter
            # Remove the user object in users_db
            # Then return a status "ok" and show the removed data
            if u["user_id"] == user_id:
                users_db.remove(u)
                return {"status": "ok", "removed_data": u}
    
    # Return an error message if there is no user found
    return {"error": "User not found. Cannot delete record"}

# PUT example
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):  # Takes a path parameter user_id that can take integer values and user that contains a user object based on the User class
     # Check if the user_id is provided
    if user_id:
        # Find user by user_id
        for idx, u in enumerate(users_db):
            # If the user_id in the users_db matches the inputted user_id from the parameter
            # Update the values of the keys in users_db
            # Then return a status "ok" and show the updated data
            if u["user_id"] == user_id:
                users_db[idx]['name'] = user.name
                return {"status": "ok", "updated_data": users_db[idx]}

    # Return an error message if there is no user found
    return {"error": "User not found. Cannot update record"}
