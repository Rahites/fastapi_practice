## 점프 투 FastAPI Practice
https://wikidocs.net/book/8531  

OS: Ubuntu 22.04  
Python: 3.10.13  

### Env
0. nodejs(v20.x) 설치  
```curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&```  
```sudo apt-get install -y nodejs```

1. fastapi 서버 실행  
```uvicorn main:app --reload```  

2. svelte 서버 실행  
```cd frontend```  
```npm run dev```


### ORM(SQLAlchemy) + Migrations(Alembic)
1. alembic 설치  
```pip install alembic```  

2. alembic 초기화  
```alembic init migrations```  

3. alembic.ini 수정  
sqlalchemy.url = sqlite:///./fastapi.db  

4. migrations/env.py 수정  
import models    
target_metadata = models.Base.metadata  

5. Revision 파일 생성  
```alembic revision --autogenerate```: migrations/versions에 Revision 파일 생성  
```alembic upgrade head```: Revision 파일 실행(.db 파일 생성)  