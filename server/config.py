from pydantic_settings import BaseSettings


class Config(BaseSettings):
    COGNITO_CLIENT_ID: str = ""
    COGNITO_CLIENT_SECRET :str = ""
    
    