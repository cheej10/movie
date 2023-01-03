from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker

from .database import Base

# sqlalchemy 모델 생성
class Movie(Base):
    __tablename__ = "movies"

    id = Column(String(100), primary_key=True, index=True)
    poster_img = Column(String(100))
    title = Column(String(100))
    story = Column(String(500))
    actors = Column(JSON)
    genre = Column(JSON)
    runtime = Column(String(100))
    director = Column(String(100))