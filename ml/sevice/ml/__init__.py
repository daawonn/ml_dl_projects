from sklearn.externals import joblib 
import json
import re
import os
import sys
import urllib.request


# 1. python 3.3 이하 버전과 하위 호환을 위해서 사용
# 2. 패키지 자체를 지칭할때 사용된다

PI2 = 3.144
def a():
    print('구동')

# 0. 경로 -> 상수값 -> 환경변수 혹은 DB 에서 획득
MODEL_PATH  = './ml/sevice/ml/clf_model_202001161419.model'
MODEL_LABEL = './ml/sevice/ml/clf_labels.label'

if __name__ != '__main__':
    # 1. 모델 로드 (1회만) -> 요청이 많아지면 컨트롤이 가능한지 체크
    clf = joblib.load(MODEL_PATH)

    # 2. 레이블 로드
    with open (MODEL_LABEL,'r') as f:
        clf_label = json.load(f)

# 3. 예측 함수 (input -> text , out -> 예측결과 ex> en,fr,....)

def detect_lang( text ):

    # 개인별로 신청한 lv2 open api 사용

    # A. text => 빈도계산 => 알고리즘에 예측요청(데이터 주입) => 그 결과를 리턴
    text = text.lower()                #1. 소문자처리
    p    = re.compile('[^a-z]')        #2. 정규식(알파벳소문자만제외)
    text = p.sub( '' , text )          #3. 소문자만 남는다.
    counts = [ 0 for n in range(26) ]  # 알파벳별 카운트를 담을 공간(리스트)
    limit_a = ord('a')                 # 반복해서 작업하니까 그냥 최초 한번 변수로 받아서 사용
    for word in text:
        counts[ord(word)-limit_a] += 1     # 문자 1개당 카운트 추가
    total_count = sum(counts)
    freq = list( map( lambda x:x/total_count , counts ) )        # 정규화

    # B. 알고리즘에 예측요청(데이터 주입)
    predict = clf.predict( [freq] )  # 입력 형태를 개발했던 형태와 동일하게 차원을 맞춘다.
    na_code = predict[0]             # en, fr, ....
    na_str = clf_label[na_code]      #'영어', '프랑스어', .... 


    # C. 결과를 리턴
    return na_code, na_str

CLIENT_ID = 'vDFc8ZDZ6txFA2fxJUDa'
SECRET_KEY = 'cLw_4HLzFP'
PAPAGO_URL = "https://openapi.naver.com/v1/papago/n2mt"           #주소
'''
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: vDFc8ZDZ6txFA2fxJUDa" \
-H "X-Naver-Client-Secret: cLw_4HLzFP" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
'''    

# 4. 번역 함수 (현: 파파고 연동, 향후: RNN로 구현)    
def transfer_lang( text, na_input_code = 'en', na_output_code = 'ko'):
    print('파파고와 연동한 번역 처리 시작')
    print(text)
    encText = urllib.parse.quote(text)                    #한글의 url 인코딩처리 => %2D.... 변환처리
    data    = "source={}&target={}&text={}".format(na_input_code,na_output_code,encText )  #파라미터 구성    
    request = urllib.request.Request(PAPAGO_URL)            # 요청객체 생성
    request.add_header("X-Naver-Client-Id",CLIENT_ID)       # 헤더설정
    request.add_header("X-Naver-Client-Secret",SECRET_KEY)  # 헤더설정

    response = urllib.request.urlopen(request, data=data.encode("utf-8")) # 요청
    rescode = response.getcode()
    if(rescode==200):  #응답성공
        return json.load( response )
    else:
        return {}        


# 이 코드는 개발시 테스트 했던 코드이다.
# 의도(개발시) 될때만 작동해야 한다.
if __name__ == '__main__':
    #print('테스트', PI2)
    test_str = 'Bong Joon-ho (Korean: 봉준호, Korean pronunciation: [poːŋ tɕuːnho → poːŋdʑunɦo]; born September 14, 1969) is a South Korean film director and screenwriter. '
    transfer_lang( test_str )

