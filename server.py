from imp import reload
# Terminal 에서 uvicorn 명령어를 사용하지 않고 , 'python config.py'로 uvicorn 을 실행할 수 있다.

import uvicorn

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)
