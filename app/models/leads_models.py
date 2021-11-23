from datetime import datetime, timedelta
from app.configs.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import ( NULLTYPE, Integer, String, DateTime)
from dataclasses import dataclass
from app.exceptions.exceptions import  InvalidEmailError, InvalidKeysError, InvalidPhoneError,InvalidPhormathPhoneError, InvalidTypeError 
import re 

@dataclass
class Lead(db.Model):
    id: int
    name: str
    email:str
    phone:str
    visits:int

    __tablename__ = "lead_cards"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    creation_date =Column(db.DateTime, default=datetime.utcnow, nullable=True)
    last_visit = Column(db.DateTime, default=datetime.utcnow, nullable=True)   
    visits= Column(Integer, nullable=True, default= 1)


    
    
    @staticmethod
    def validate(data):
        required_keys= [ "name", "email", "phone"]
        pattern = re.compile(r'^\([0-9]{2}\)[0-9]{5}\-[0-9]{4}$')

        for key in data.keys():
            if key not in required_keys:
                raise InvalidKeysError
                
                          
        for value in data.values():
            if type(value) is not str:
                raise InvalidTypeError
        
        unique_key = (
            Lead
            .query
            .filter(Lead.email==data["email"])
            .one_or_none()
        )
        if unique_key is not None:
            raise InvalidEmailError

        unique_phone = (
            Lead
            .query
            .filter(Lead.phone==data["phone"])
            .one_or_none()
        )
        if unique_phone is not None:
            raise InvalidPhoneError

        if pattern.fullmatch(data["phone"]) is None:
            raise InvalidPhormathPhoneError

   
    
        
      