from fastapi import FastAPI, Depends
app = FastAPI()

def status():
    return "User is verified"

@app.get("/")
def home(user = Depends(status)):
    return {
        "message" : "Welcome home",
        "status" : user
    }