from models import Question, Answer
from datetime import datetime
from database import SessionLocal

### 데이터 추가
q = Question(subject="인사", content="Hello World", create_date=datetime.now())

db = SessionLocal()
db.add(q)
db.commit()

print(q.id)

### 데이터 조회
db = SessionLocal()

print('DB에 저장된 데이터 : ', db.query(Question).all())
print('첫번째 질문 : ', db.query(Question).filter(Question.id==1).all())
# print('첫번째 질문 : ', db.query(Question).get(1)) # 1.x style
print('"인"이 포함된 질문 : ', db.query(Question).filter(Question.subject.like("%인%")).all())


### 데이터 삭제
q = db.get(Question, 1) # 2.0 style
db.delete(q)
db.commit()