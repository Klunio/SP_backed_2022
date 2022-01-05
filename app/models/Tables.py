# -*- coding: utf-8 -*-
# Create Time: 01/05 2022
# Author: Yunquan (Clooney) Gu
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Base.metadata.schema = 'main'

class ItemTable(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(VARCHAR(255))
    create_time = Column(TIMESTAMP)
