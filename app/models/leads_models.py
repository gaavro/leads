from datetime import datetime, timedelta
from app.configs.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import ( NULLTYPE, Integer, String, DateTime)
from dataclasses import dataclass
from app.exceptions.exceptions import InvalidCPFError, InvalidKeyError, InvalidTypeError, InvalidUniqueKeyError, MissingOneKey

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
        required_keys= ["id", "name", "email", "phone", "creation_date", "last_visit", "visits"]
        for item in required_keys:
            if item not in data.keys():
                raise InvalidKeyError
        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError
            
        if len(data["cpf"]) != 11:
            raise InvalidCPFError
        unique_key = (
            Lead
            .query
            .filter(Lead.id==data["id"])
            .one_or_none()
        )
        if unique_key is not None:
            raise InvalidUniqueKeyError


   
    
        
      