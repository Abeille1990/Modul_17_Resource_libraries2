from sqlalchemy import String, Integer, Boolean, Column, ForeignKey, Float
from app.backend.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    category = relationship('tasks', back_populates='user')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))