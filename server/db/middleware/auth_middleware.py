from config import Config
from fastapi import HTTPException, Cookie, Depends
import boto3


config = Config()
cognito_client = boto3.client("cognito-idp",region_name= config.REGION_NAME)


def _get_user_from_cognito(access_token:str):
    try:
        user_res = cognito_client.get_user(
            AccessToken = access_token,
        )
        return {
            attribute["Name"]: attribute["Value"]
            for attribute in user_res.get("UserAttributes",[])
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user: {e}")


def get_current_user(access_token:str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return _get_user_from_cognito(access_token)
