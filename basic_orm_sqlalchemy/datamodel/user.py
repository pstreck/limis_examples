from sqlalchemy import Column, Integer, String

from datamodel import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
