from sqlalchemy import String, Integer, Boolean, Column, ForeignKey
from app.backend.db import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("tasks.id"), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)

    relationship("User", back_populates="tasks")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
