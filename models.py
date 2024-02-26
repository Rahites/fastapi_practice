from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# base class를 상속
class Question(Base):
    __tablename__ = "question"

    # Integer: 숫자값
    # String: 글자 수가 제한된 텍스트
    # Text: 글자 수를 제한할 수 없는 텍스트
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    # 답변을 질문과 연결하기 위해 추가한 속성
    # ForeignKey: 기존 모델과 연결된 속성
    # 여기서 question.id는 question 테이블의 id Column
    question_id = Column(Integer, ForeignKey("question.id"))
    # 답변 모델에서 질문 모델을 참조하기 위해 추가
    # backref: 역참조(질문에서 답변을 거꾸로 참조하는 것)
    question = relationship("Question", backref="answers")