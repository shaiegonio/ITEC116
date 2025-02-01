from fastapi import FastAPI

application = FastAPI()

@application.get("/factorial/{starting_number}")

def factorial(starting_number: int):
    
    if starting_number == 0:
        return {"result": False}

    factor = 1

    while starting_number > 0:
        factor *= starting_number
        starting_number -= 1 

    return {"result": factor} 