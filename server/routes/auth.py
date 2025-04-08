from config import Config
from db.db import get_db
from fastapi import APIRouter, Depends
import boto3
from helpers.auth_helper import get_secret_hash
from pydantic_models.auth_model import SignupRequest
from sqlalchemy.orm import Session

router = APIRouter()

config = Config()

COGNITO_CLIENT_ID = config.COGNITO_CLIENT_ID
COGNITO_CLIENT_SECRET = config.COGNITO_CLIENT_SECRET

cognito_client = boto3.client("cognito-idp",region_name = config.REGION_NAME)

@router.post("/signup")
def signup_user(data: SignupRequest,db:Session = Depends(get_db)):
    secret_hash = get_secret_hash(data.email,COGNITO_CLIENT_ID,COGNITO_CLIENT_SECRET)

    cognito_response = cognito_client.sign_up(
        ClientId = COGNITO_CLIENT_ID,
        Username = data.email,
        Password = data.password,
        SecretHash= secret_hash,
        UserAttributes = [
            {"Name": "email","Value":data.email},
            {"Name":"name","Value":data.name}
        ]
    )

    return cognito_response