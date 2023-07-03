etext1 = """🐤모듈 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

 - 다른 파이썬 파일에서 불러와서 사용할 수 있고 다음과 같은 키워드를 통해 불러올 수 있다.

  예시👇
 import 파이썬 파일(경로) as 별명
 # 또는 
 from 파이썬 파일(경로) import 클래스 또는 메서드
 # import * 하면 모듈 내 전체 불러오기

 import math as mt
 from pandas import *
 

 🐤모듈 구분
 - 표준 라이브러리 모듈 : 파이썬 인터프리터 설치 시 자동으로 설치되는 모듈 
   -> https://docs.python.org/ko/3/library/index.html

 - 서드파티 모듈 : 제3자나 회사가 만든 라이브러리
   -> https://pypi.org/"""

etext2 = """🐤 예외 : 코드 실행 도중 일어나는 에러

try 블럭 : 실행할 코드를 작성하는 블럭

except 블럭 : 예외 발생 시 실행할 코드를 작성하는 블럭

else 블럭 : 정상 실행 시 try 블럭 실행 후 실행할 코드를 작성하는 블럭

finally 블럭 : 예외 발생 또는 발생하지 않아도 무조건 실행할 코드를 작성하는 블럭


 예시👇
 try : 
    l1 = [1,2,3,4]
    print(l1[5]) # 인덱스 에러
 except IndexError as IE:
    print("인덱스 에러!")
 else :
    print("else 블럭")
 finally : 
    print("finally 블럭")
# 출력 -> 인덱스 에러!
         finally 블럭"""
etext3 = """🐤 파일처리 : 파이썬에서 파일을 읽고 쓸 수 있다.
 
 - 모드
  r : 읽기 모드
  w : 쓰기 모드
  a : 추가 모드
  x : 파일이 없으면 생성하고 쓰기모드, 있으면 에러
  b : 바이너리 모드
  t : 텍스트 모드(기본)

  
 - 함수들
  open() : 파일 열기
  close() : 파일 닫기
  write() : 파일 쓰기
  writelines() : 파일 한줄 쓰기
  read() : 파일 읽기
  readline() : 파일 한줄 읽기
  readlines() : 해당 위치 부터 파일 모든 문자열 읽기
  seek() : 해당 위치로 파일의 커서를 옮김
  tell() : 현재 커서의 위치 반환

  
예시👇
f = open("./test.txt",'x')
f.write("안녕하세요")
f.close


# with open을 사용하면 close를 할 필요 없음
# 블럭을 벗어나면 자동으로 파일 close
with open("./test.txt",'x') as f:
    f.write("안녕하세요.")"""