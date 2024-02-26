0. nodejs 설치
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&\
sudo apt-get install -y nodejs

1. fastapi 서버 실행
uvicorn main:app --reload

2. svelte 서버 실행
cd frontend
npm run dev

https://velog.io/@terra/SVELTE-%EA%B8%B0%EC%B4%88-%EB%AC%B8%EB%B2%95


