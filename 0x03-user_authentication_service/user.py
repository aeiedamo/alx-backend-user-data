#!/usr/bin/env python3
"""
User authentication service
"""

from sqlalchemy import Column, Integer, String, column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    to declare User model
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), unique=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
