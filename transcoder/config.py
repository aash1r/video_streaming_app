from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class Config(BaseSettings):
    REGION_NAME: str =""
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""