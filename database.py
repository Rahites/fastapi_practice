from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
ORM(Object Relational Mapping)을 사용할 경우 파이썬 문법만으로 데이터베이스를 다룰 수 있다.  
SQLite는 파이썬 기본 패키지에 포함되어 있으며 가벼운 파일을 기반으로 한 데이터베이스이다.
'''


# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi.db"

# 커넥션 풀 생성
# 커넥션 풀: DB에 접속하는 객체를 일정 개수만큼 만들어두고 돌려가며 사용
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# autocommit: False시 데이터를 변경했을 때 commit 명령일 주어야 저장
# True일 경우에는 rollback 명령으로 되돌릴 수 없다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델을 구성할 때 사용되는 클래스
Base = declarative_base()

# Dependency Injection(의존성 주입): 필요한 기능을 선언하여 사용할 수 있다.
import contextlib

# 제네레이터는 iterator를 생성해주는 함수 (yield 키워드 사용)
# @contextlib.contextmanager -> with문과 사용가능
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    # db 객체를 생성한 후에 db.close()를 수행하지 않으면 커넥션 풀에 문제 발생
    finally:
        db.close()