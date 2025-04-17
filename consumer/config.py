from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Config(BaseSettings):
    REGION_NAME : str = ""
    QUEUE_URL :str =""