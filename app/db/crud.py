from sqlalchemy.orm import Session
from . import models

def get_movie(db: Session, movie_id: str):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()