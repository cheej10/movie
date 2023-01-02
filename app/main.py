from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from fastapi import FastAPI, Depends, Path, HTTPException
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from . import crud, models, schemas
from .database import SessionLocal, engine
import requests
import json
import uuid

# URL='https://www.justwatch.com/kr'

# # requests 해당 페이지 html get
# response=requests.get(URL)
# # BeautifulSoup html 파싱
# soup = BeautifulSoup(response.text, "html.parser")
# # 드라이버 설치 경로
# driver = webdriver.Chrome('/Users/choheejung/Downloads/chromedriver')
# # 드라이버가 페이지 접속
# # driver.get(URL)

# elements = soup.select('.title-list-grid__item')

# movies = []

# for element in elements:
#     movie = {}
#     detail_link = element.find('a', 'title-list-grid__item--link').get('href')
#     img_el = element.find('img', 'picture-comp__img')

#     movie['poster_img'] = img_el.get('data-src') if img_el.get('data-src') else img_el.get('src')

#     movie['actors'] = []
#     detail_arr = []

#     driver.get(f"https://www.justwatch.com{detail_link}")
#     for el in driver.find_elements(By.CLASS_NAME, 'detail-infos__value'):
#         if el.text is not None: detail_arr.append(el.text)

#     detail_arr = list(filter(None, detail_arr))
#     movie['genre'] = detail_arr[1].split(', ')
#     movie['runtime'] = detail_arr[2]
#     if len(detail_arr) > 4:
#         movie['director'] = detail_arr[4]

#     for el in driver.find_elements(By.CLASS_NAME, 'title-credits__actor'):
#         if el.text is not None: movie['actors'].append(el.text.split('\n')[0])

#     movie['id'] = str(uuid.uuid4())
#     movie['title'] = driver.find_element(By.CSS_SELECTOR, '.title-block h1').text
#     movie['story'] = driver.find_element(By.CSS_SELECTOR, '.text-wrap-pre-line > span').text

#     movies.append(movie)



# db에 저장
# models.Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# for movie in movies:
#     input_data = models.Movie(
#         id = movie['id'],
#         poster_img = movie['poster_img'],
#         title = movie['title'],
#         story = movie['story'],
#         actors = movie['actors'],
#         genre = movie['genre'],
#         runtime = movie['runtime'],
#         director = movie.get('director'),
#     )

#     session.add(input_data)
#     session.commit()


# fast api
app = FastAPI()

origins = [
    'http://localhost:8081'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=List[schemas.MovieBase])
async def first_get(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies