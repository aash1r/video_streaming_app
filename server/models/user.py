from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id =Column(Integer,primary_key = True,index = True)
    username = Column(String,nullable= False)
    email = Column(String,unique = True, nullable = False)
    cognito_sub = Column(String, unique = True, nullable = False,index = True)
    