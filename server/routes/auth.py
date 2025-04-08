from config import Config
from fastapi import APIRouter
import boto3
from pydantic_models.auth_model import SignupRequest

router = APIRouter()

config = Config()

COGNITO_CLIENT_ID = config.COGNITO_CLIENT_ID
COGNITO_CLIENT_SECRET = config.COGNITO_CLIENT_SECRET

cognito_client = boto3.client("cognito-idp",region_name = "us-east-1")

@router.post("/signup")
def signup_user(data: SignupRequest):
    cognito_response = cognito_client.sign_up(
        ClientId = COGNITO_CLIENT_ID,
        Username = data.email,
        Password = data.password,
        UserAttributes = [
            {"Name": "email","Value":data.email},
            {"Name":"name","Value":data.name}
        ]
    )

    return cognito_response