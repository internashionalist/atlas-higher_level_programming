#!/usr/bin/python3
"""
This module contains the City class and the Base instance.
"""
import sys
import MySQLdb
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


Base = declarative_base()

class City(Base):
    """
    City class (links to cities table)
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
