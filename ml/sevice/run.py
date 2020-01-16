# 엔트리 포인트 : 진입로, 시작점
# 1. 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect #첫글자 대문자 => 클래스
from ml.mod import PI
from ml import PI2

# 2. Flask 객체 생성
app = Flask( __name__ )

# 3. 라우팅
@app.route('/')
def home():
    print(PI)
    print(PI2)
    return render_template('index.html')

# 4. 서버가동
if __name__ == '__main__' :
    app.run(debug=True)
else:
    print('작동 X')    
