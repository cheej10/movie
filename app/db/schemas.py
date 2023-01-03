from typing import List, Union, Optional
from pydantic import BaseModel

# Pydantic 모델 생성 - api에서 읽을 데이터 형식 지정
class MovieModel(BaseModel):
    id: str = None
    poster_img: str = None
    title: str = None
    story: str = None
    actors: list = None
    genre: list = None
    runtime: str = None
    director: str = None

    class Config:
        orm_mode = True