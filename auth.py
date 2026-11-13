from fastapi import FastAPI,HTTPException,Depends, Header
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

#Jwt Config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE =30

#password Hashing Setup
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

#OauthSetup
oath2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy userDB
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}
#hash Passsword
def hash_password(password:str):
    return pwd_context.hash(password)

#verify Password
def verify_password(plain_password, hased_password):
    return pwd_context.verify(plain_password, hased_password)

#Create Token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })

    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return token

#Login Api token Genrate with OAuth2_form
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail = "Invalid username or password"
        )

    access_token = create_token({"sub":form_data.username})
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }


def varify_token(token: str = Depends(oath2_schema)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )

#protected Route
@app.get("/secure")
def secure_data(user = Depends(varify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }

#protector route
@app.get("/protected")
def protected_route(username: str = Depends(varify_token)):
    return{
        "message":f"Hello  you have access to this protected route!",
        "user":username
    }

