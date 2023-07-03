ftext1 ="""파이썬의 함수선언은 다음과 같이 작성한다.

def 함수명(매개변수):
    코드

예시👇
def f1(a):
    return a+1

# 값을 여러개 반환 할 수 있다.
def f2(a):
    return a+1,a+2

# 내부 코드가 한줄인 경우 한줄로 쓸 수 있다.
def f3(a): return a+1 

함수 호출은 다음과 같이 사용할 수 있다.

예시👇
a = f1(1) # a == 2

b,c = f2(1) # b == 2, c == 3

d = f3(1) # d == 2 """
ftext2 = """🦊디폴트 매개변수 : 매개변수를 전달하지 않았을 때 사용할 값을 지정한다.

예시👇
def f2(a=3):
    return a
a = f2() # a == 3
b = f2(4) # b == 4

 - 주의! 디폴트 매개변수를 반드시 오른쪽부터 채워져 있어야한다.

 
🦊가변 매개변수 : *를 사용해서 매개변수를 튜플 형태로 여러개 전달 할 수 있다.

예시👇
def argsFunc(*args): return args
a = argsFunc(1,2,3,4,5) # a == (1,2,3,4,5)


🦊키워드 매개변수 : **를 사용해서 매개변수를 사전으로 여러개 전달 할 수 있다.

예시👇
def kargsFunc(**kargs): return args
a = argsFunc(a=1,b=2,c=3) # a == {'a':1,'b':2,'c':3}


🦊람다함수(Lambda) : 이름이 없는 함수를 작성할 수 있다.
 - 코드가 간결해진다.
 - 메모리가 절약된다.
 - 한번만 사용할 함수를 만들 때 사용한다.
 - 매개변수를 여러개 정의할 수 있고 디폴트 매개변수,*,**를 사용할 수 있다.

예시👇
a = lambda a : a+1 # 매개변수+1 을 반환하는 함수
b = a(3) # b == 4"""