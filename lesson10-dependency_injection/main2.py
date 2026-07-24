from fastapi import FastAPI,Header, Depends
from fastapi import HTTPException

app = FastAPI()

def verify_token(token : str = Header(None)):
    if token != 'mysecrettoken':
        raise HTTPException(
            status_code=401,
            detail="Unauthorized")
    return {
        "user" : "Authorized User"
    }

@app.get("/secret-user")
def user(user = Depends(verify_token)):
    return {
        "message" : "Secure data accessed",
        "user" : user
    }

