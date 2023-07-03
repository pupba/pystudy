cltext1 = """🐻‍❄️객체 지향 프로그래밍

우리가 실생활에서 쓰는 모든것을 객체(Object)라고한다.

객체지향의 4대 특징
 - 추상화(abstraction)
 - 캡슐화(encapsulation)
 - 상속성(inheritance)
 - 다형성(polymorphism)
 - 동적바인딩(Dynamic Binding)


클래스
 - 객체를 만드는 틀
 - 필드와 메서드를 정의
 - 하나의 클래스에서 무수히 많은 객체 생성


객체 == 인스턴스 :
 - 클래스를 실체화한것
 - 클래스에서 정의한 필드와 메서드를 따름
 - 각 객체는 독립적"""
cltext2 = """🐻‍❄️클래스 정의
예시👇
class 클래스명:
    def __init__(self):
        # 생성자 코드
    # 필드, 메서드 정의

 - 생성자는 Overloading 할 수 있다.
예시👇
def __init__(self,a):
    self.a = a
def __init__(self,a,b):
    self.a = a
    self.b = b

 - self는 자기자신을 의미한다.
 - 필드를 정의할 때 앞에 "self.필드명" 형식으로 정의한다.
 - 클래스 내부의 필드를 호출하려면 "self.필드" 형식으로 호출한다.
 - 클래스 내부의 메소드를 호출할 때는 "self.함수" 형식으로 호출한다.


🐻‍❄️객체 생성 : 정의된 클래스를 메서드 호출하듯이 사용하면된다.
예시👇
class C1:
    def __init__(self,a):
        self.a = a
    def __init__(self,*a):
        self.a = a
    def f1(self):
        print(self.a)
c1 = C1(10)
c2 = C1(10,20,30)
c1.f1() # 메서드 호출
c2.a # 필드 호출"""
cltext3 = """파이썬은 기본적으로 모든 필드와 메서드들이 public으로 설정되어 있다.
접근지정자를 변경하려면 다음과 같이 설정하면 된다.

🐻‍❄️public : 클래스 내,외부 자유롭게 접근가능
예시👇
self.a = a
def f1(a):
    print(self.a)
f1(10)
    
🐻‍❄️protected : 클래스 내부, 상속된 클래스 내부에서 접근가능
예시👇
self._a =a
def _f1(a):
    print(self._a)
_f1(10)

🐻‍❄️private : 클래스 내부만 접근가능
예시👇
self.__a = a
def __f1(a):
    print(self.__a)
__f1(10)"""
cltext4 = """🐻‍❄️클래스는 상속을 통해 자신의 자식 클래스를 만들 수 있다.
 - 상속된 클래스(자식)는 상속하는 클래스(부모)의 모든 필드,메서드를 그대로 가진다.
 - 상속은 여러번 할 수 있다.
 - 상속은 여러개 받을 수 있다.(다중 상속)

🐻‍❄️상속 방법
 - 클래스명 옆에 ()안에 부모 클래스를 적으면된다.
 - super()는 부모 클래스를 의미하며 부모의 필드, 메서드를 호출할 때 사용한다.

예시👇
class P1:
    def __init__(self,a):
        self.a = a
    def f1(self): print(1)
class C2(P1):
    def __init__(self,a,b):
        super().__init__(a) # 부모 생성자 실행
        self.b = b
    def f2(self): super().f1()

🐻‍❄️오버라이딩(Overriding)
 - 상속한 자식 클래스에서 부모 클래스의 메서드의 내용을 수정한다.
 - 자식 클래스로 만든 객체에서 메서드를 호출하면 수정한 내용을 실행한다.

 예시👇
 class Person:
    def info(self):
        print("Person입니다.")
 class Pupba(Person):
    def info(self):
        print("info입니다.")

 pb = Pupba()
 pb.info() # 출력 -> info입니다."""
cltext5 = """🐻‍❄️클래스 메소드 : 클래스에서 호출되는 메서드
 - self대신 cls를 사용하여 자신의 클래스를 전달한다.(cls 대신 다른 이름 사용가능)
 - 메서드 정의시 @classmethod라는 데커레이터 사용해야함.
 - cls를 사용하여 전달된 값으로 초기화된 인스턴스를 반환
 
 예시👇
 class Test:
    def __init__(self,a):
        self.a = a
    def printAll(self):
        print(self.a)
    @classmethod
    def clsmd(cls,value):
        return cls(value)
 t1 = Test(1)
 t1.printAll() # 1
 t2 = Test.clsmd(2)
 t2.printAll() # 2


🐻‍❄️정적 메소드 : 인스턴스나 클래스를 인자로 받지 않는 메서드
 - @staticmethod라는 데커레이터를 사용해야함
 - 같은 클래스로 만들어진 객체가 공유함
 
 예시👇
 class Test:
    @staticmethod
    def printAB(a):
        print(a)
 Test.printAB(1) # 출력 -> 1"""
