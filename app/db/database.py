# sqlarchemy로 db 연결

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'mysql+pymysql://root:1234@localhost:3306/mydb'

# sqlalchemy engine 생성
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# db 모델, 클래스 생성하기 위한 base 클래스
Base = declarative_base()