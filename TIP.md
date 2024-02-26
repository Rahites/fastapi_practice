0. nodejs 설치
```curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&```  
```sudo apt-get install -y nodejs```

1. fastapi 서버 실행
```uvicorn main:app --reload```  

2. svelte 서버 실행
```cd frontend```
```npm run dev```


### migrations
alembic 도구를 사용할 때 생성되는 리비전 파일들을 저장하는 용도 
1. alembic 설치
```pip install alembic``  

2. alembic 초기화
```alembic init migrations```  

3. alembic.ini 수정
sqlalchemy.url = sqlite:///./fastapi.db

4. migrations/env.py 수정
import models 추가  
target_metadata = models.Base.metadata

5. Revision 파일 생성
```alembic revision --autogenerate```: migrations/versions에 Revision 파일 생성
```alembic upgrade head```: Revision 파일 실행(.db 파일 생성)

