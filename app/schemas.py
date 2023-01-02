from typing import List, Union
from pydantic import BaseModel

# Pydantic 모델 생성 - api에서 읽을 데이터 형식 지정
class MovieBase(BaseModel):
    email: str