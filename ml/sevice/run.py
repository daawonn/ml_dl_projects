# 엔트리 포인트 : 진입로, 시작점

# 1. 모듈 가져오기
# 플라스크 관련 모듈 가져오기
from flask import Flask, render_template, request, jsonify, redirect #첫글자 대문자 => 클래스
# 테스트 모듈 가져오기
from ml.mod import PI
# 언어감지 및 번역 모듈 가져오기
from ml import detect_lang as dl, transfer_lang

#---------------------------------------------------------------------#

# 2. Flask 객체 생성
app = Flask( __name__ )

# 3. 라우팅
@app.route('/')
def home():
    #     text_str = '''
        #     En 2000, Bong Joon-ho sort son premier long métrage Barking Dog. En 2003, il réalise Memories of Murder, un film tiré de l'histoire réelle d'un tueur en série. Le film est un grand succès et attire plus de 5 000 000 de spectateurs en Corée du Sud.

        # The Host, son troisième long-métrage, est inspiré par un incident survenu en Corée du Sud à la fin des années 1980. Les Cahiers du cinéma le classent troisième film le plus important de 2006.

        # En 2008, il se joint aux réalisateurs Leos Carax et Michel Gondry dans le film Tokyo! en proposant son court-métrage Shaking Tokyo.

        # En septembre 2009, il est membre du jury international présidé par Laurent Cantet lors du 57e Festival de Saint-Sébastien. Cette même année, il dévoile son quatrième long-métrage, le drame Mother, présenté en compétition au Festival de Cannes 2009.

        # Il revient en 2013 avec une coproduction internationale : le thriller de science-fiction Snowpiercer, le Transperceneige, adaptation du classique de la bande dessinée française homonyme, Le Transperceneige. Joon-ho signe une nouvelle fois lui-même le scénario, et réunit une distribution majoritairement anglo-américaine, menée par Chris Evans, mais complétée par son acteur fétiche Song Kang-ho, qu'il avait déjà dirigé dans The Host, et la jeune Go Ah-seong. Le long-métrage marque sa seconde incursion dans une fiction de genre adulte et spectaculaire.

        # En 2014, il est président du jury du 38e Festival international du film de Hong Kong. La même année il est membre du jury du 19e Festival de Busan, sous la présidence d'Asghar Farhadi.

        # En février 2015, il fait partie des membres du jury des longs métrages lors du 65e Festival de Berlin, présidé par Darren Aronofsky. Cette même année, le Festival International du Film de Belfort Entrevues lui consacre une rétrospective1.

        # L'année 2017 est marquée par la sortie sur Netflix du film de science-fiction Okja, qu'il identifie comme étant au croisement de The Host et Snowpiercer2. Cette fois, une distribution anglo-américaine — composée notamment de Paul Dano et Tilda Swinton — entoure une actrice principale coréenne.

        # En mai 2019, son film Parasite, présenté au festival de Cannes 2019, remporte la Palme d'or à l'unanimité du Jury3
        #     '''
        #     print(dl(text_str))
   

    import os
    import ml
    import sys
    import urllib.request
     

    client_id = ml.CLIENT_ID # 개발자센터에서 발급받은 Client ID 값
    client_secret = ml.SECRET_KEY # 개발자센터에서 발급받은 Client Secret 값

    encText = urllib.parse.quote("반갑습니다")                  #한글의 url 인코딩처리 => %2D....
    data = "source=ko&target=en&text=" + encText               #파라미터 구성
    url = "https://openapi.naver.com/v1/papago/n2mt"           #주소
    request = urllib.request.Request(url)                      # 요청객체 생성
    request.add_header("X-Naver-Client-Id",client_id)          #헤더설정
    request.add_header("X-Naver-Client-Secret",client_secret)  #헤더설정

    response = urllib.request.urlopen(request, data=data.encode("utf-8")) # 요청
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return render_template('index.html')

@app.route('/bsgo', methods=['GET','POST'])
def bsgo():
    if request.method == 'GET':
        return render_template('bsgo.html')
    else :
        # 전달 된 데이터 획득
        # print(request.form.get('o'))
        oriTxt = request.form.get('o')  # 내용이 들어있고 100글자 이상이다.
        # print(request.form['o'])  # 만약 키가 틀리면 오류를 발생한다
        # 언어감지
        na_code, na_str = dl( oriTxt )
        
        if na_code:  # 예측 되었다.
            res = {
                'code':na_code,
                'code_str':na_str
            }

        else:
            res = {
                'code':'0',
                'code_str':'언어 감지 실패'
            }
        # 결과응답                
        return jsonify( res )
        # pass 

@app.route('/transfer', methods=['POST'])
def transfer():
    # 데이터를 획득
    oriTxt = request.form.get('o')
    na     = request.form.get('na')
    # 번역
    print(oriTxt)
    res    = transfer_lang( oriTxt, na )
    # 로그처리

    # 응답
    return  jsonify( res )


# 4. 서버가동
if __name__ == '__main__' :
    app.run(debug=True)
else:
    print('작동 X')

