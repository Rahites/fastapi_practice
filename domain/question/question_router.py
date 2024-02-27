from fastapi import APIRouter

from database import SessionLocal
from models import Question

'''
라우팅: FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행, 리턴하는 행위
'''

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    db.close()
    return _question_list
