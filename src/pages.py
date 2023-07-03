import tkinter as tk
import os
from PIL import ImageTk,Image
class MainPage(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너
        con = tk.Frame(self)
        con.pack(fill='both',expand=True)

        # 제목
        titleLabel = tk.Label(con, text="파이썬 Basic 훈련 프로그램", font=("Helvetica", 24, "bold"))
        titleLabel.pack(side=tk.TOP,pady=60)

        # 시작 버튼
        button = tk.Button(con, text="시작!", width=10, height=2, font=("Helvetica", 14, "bold"), command=self.moveNextPage)
        button.pack(side=tk.TOP,pady=10)
        
        image = Image.open(os.getcwd()+"/src/static/pupbani.png")
        image = image.resize((300,300))
        self.photo = ImageTk.PhotoImage(image)

        self.canvas = tk.Canvas(con,width=300,height=300)
        self.canvas.pack(side=tk.TOP,pady=10)

        self.canvas.create_image(0,0,anchor=tk.NW,image=self.photo)

        # 제작자 정보
        infoLabel = tk.Label(con, text="제작자: 컴공 18 정광원\n이메일: rhdk5148@gmail.com", font=("Helvetica", 12))
        infoLabel.pack(side=tk.RIGHT, anchor=tk.SE, padx=20, pady=20)
    
    def moveNextPage(self)->None:
        self.master.switchPage(Pagelist)

class Pagelist(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너
        con = tk.Frame(self)
        con.pack(fill='both',expand=True)

        # 제목
        titleLabel = tk.Label(con, text="목차", font=("Helvetica", 24, "bold"))
        titleLabel.pack(side=tk.TOP,pady=60)

        # 시작 버튼
        button1 = tk.Button(con, text="개요", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Overview1))
        button1.pack(side=tk.TOP,pady=10)

        button2 = tk.Button(con, text="기초 내용", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Basic1))
        button2.pack(side=tk.TOP,pady=10)

        button3 = tk.Button(con, text="제어문", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Control1))
        button3.pack(side=tk.TOP,pady=10)

        button4 = tk.Button(con, text="자료구조", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Struct1))
        button4.pack(side=tk.TOP,pady=10)

        button5 = tk.Button(con, text="함수", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Func1))
        button5.pack(side=tk.TOP,pady=10)

        button6 = tk.Button(con, text="클래스", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Class1))
        button6.pack(side=tk.TOP,pady=10)

        button7 = tk.Button(con, text="기타", width=10, height=2, font=("Helvetica", 14, "bold"), command=lambda : self.master.switchPage(Etc1))
        button7.pack(side=tk.TOP,pady=10)

from static.overview import *
class Overview1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="처음으로",command=self.go2list)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="개요",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2Ov2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=20)

        self.text = tk.Text(con2,font=("Helvetica", 13))
        self.text.pack()

        self.text.insert(tk.END,otext1)

    def go2list(self)->None:
        self.master.switchPage(Pagelist)
    def go2Ov2(self)->None:
        self.master.switchPage(Overview2)

class Overview2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2Ov1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="개요",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2Ov3)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=20,pady=0)
        self.text.pack(side=tk.TOP)

        self.text.insert(tk.END,otext2)
        self.text.insert(tk.END,"\n\n파이썬 언어로 작성된 파일이 컴퓨터에서 실행되는 구조는 다음과 같다.")

        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.CENTER)
        
        image = Image.open(os.getcwd()+"/src/static/process.png")
        image = image.resize((650,100))
        self.photo = ImageTk.PhotoImage(image)

        self.canvas = tk.Canvas(con3,width=650,height=100)
        self.canvas.pack(side=tk.TOP,pady=10)

        self.canvas.create_image(0,0,anchor=tk.NW,image=self.photo)

    def go2Ov1(self)->None:
        self.master.switchPage(Overview1)
    def go2Ov3(self)->None:
        self.master.switchPage(Overview3)

class Overview3(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2Ov2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="개요",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2basic1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=12,pady=0)
        self.text.pack(side=tk.TOP)

        self.text.insert(tk.END,otext3)
        
        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.CENTER)
        
        image = Image.open(os.getcwd()+"/src/static/thirdp.png")
        image = image.resize((500,380))
        self.photo = ImageTk.PhotoImage(image)

        self.canvas = tk.Canvas(con3,width=500,height=380)
        self.canvas.pack(side=tk.TOP,pady=10)

        self.canvas.create_image(0,0,anchor=tk.NW,image=self.photo)

    def go2Ov2(self)->None:
        self.master.switchPage(Overview2)
    def go2basic1(self)->None:
        self.master.switchPage(Basic1)

from static.basic import *
class Basic1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2Ov3)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="변수",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2basic2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.txt1 = tk.Text(con2,font=("Helvetica", 13),height=12,pady=0)
        self.txt1.pack(side=tk.TOP)

        self.txt1.insert(tk.END,btext1)

        self.lb = tk.Label(con2,text="변수 사용 예시",font=("Helvetica",13,"bold"))
        self.lb.pack(side=tk.TOP,anchor=tk.S,pady=10)

        self.txt2 = tk.Text(con2,font=("Helvetica", 13),height=6,pady=0)
        self.txt2.pack(side=tk.TOP)
        self.ex1 = """
  num = 1
  fnum = 1.0
  string = 'hello'
  List:list = [1,2,3,4,5] # 어노테이션
        """
        self.txt2.insert(tk.END,self.ex1)

    def go2Ov3(self)->None:
        self.master.switchPage(Overview3)
    def go2basic2(self)->None:
        self.master.switchPage(Basic2)

class Basic2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2basic1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="연산자",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2basic3)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=4,pady=0)
        self.text.pack(side=tk.TOP)
        
        self.text.insert(tk.END,btext2)
        self.hyl = tk.Button(con2,text="더 많은 연산자 보기",command=self.hyl1)
        self.hyl.pack(side=tk.LEFT,anchor=tk.S,pady=0)

        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.CENTER)
        
        image = Image.open(os.getcwd()+"/src/static/operator.png")
        image = image.resize((450,450))
        self.photo = ImageTk.PhotoImage(image)

        self.canvas = tk.Canvas(con3,width=450,height=450)
        self.canvas.pack(side=tk.TOP,pady=10)

        self.canvas.create_image(0,0,anchor=tk.NW,image=self.photo)
    
    def hyl1(self)->None:
        import webbrowser
        webbrowser.open("https://sdc-james.gitbook.io/onebook/3./3.4./1.1.1.")

    def go2basic1(self)->None:
        self.master.switchPage(Basic1)
    def go2basic3(self)->None:
        self.master.switchPage(Basic3)

class Basic3(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2basic2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="기본 입출력",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2control1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=4,pady=0)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,btext3)
        
        self.pri = tk.Text(con2,font=("Helvetica", 13),height=10,pady=0)
        self.pri.pack(side=tk.TOP)
        self.pri.insert(tk.END,btext4)

        self.pt1 = tk.Label(con2,text='print("',font=("Helvetica", 13))
        self.pt1.pack(side=tk.LEFT)
        self.testPrint = tk.Entry(con2)
        self.testPrint.pack(side=tk.LEFT)
        self.pt2 = tk.Label(con2,text='")',font=("Helvetica", 13))
        self.pt2.pack(side=tk.LEFT)
        self.eBtn = tk.Button(con2,text="출력",command=self.popup1)
        self.eBtn.pack(side=tk.LEFT)

        # 컨테이너2
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.inp = tk.Text(con3,font=("Helvetica", 13),height=7,pady=0)
        self.inp.pack(side=tk.TOP)
        self.inp.insert(tk.END,btext5)

        self.pt1 = tk.Label(con3,text='변수 = input("',font=("Helvetica", 13))
        self.pt1.pack(side=tk.LEFT)
        self.testPrint = tk.Entry(con3)
        self.testPrint.pack(side=tk.LEFT)
        self.pt2 = tk.Label(con3,text='")',font=("Helvetica", 13))
        self.pt2.pack(side=tk.LEFT)
        self.eBtn = tk.Button(con3,text="입력",command=self.popup2)
        self.eBtn.pack(side=tk.LEFT)

    def popup1(self)->None:
        from tkinter import messagebox
        messagebox.showinfo("print() 예시",f"출력 : {self.testPrint.get()}")
    def popup2(self)->None:
        from tkinter import messagebox
        messagebox.showinfo("input() 예시",f"출력 : {self.testPrint.get()}\n키보드로 입력하면 입력한 값이 문자열로 변수에 저장됩니다.")

    def go2basic2(self)->None:
        self.master.switchPage(Basic2)
    def go2control1(self)->None:
        self.master.switchPage(Control1)

from static.control import *
class Control1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2basic3)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="조건문: if, elif, if-else",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=150)

        self.next = tk.Button(con1,text="다음으로",command=self.go2control2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=7,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext1)
        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con3,font=("Helvetica", 13),height=7,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext2)
        # 컨테이너4
        con4 = tk.Frame(self)
        con4.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con4,font=("Helvetica", 13),height=13,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext3)

    def go2basic3(self)->None:
        self.master.switchPage(Basic3)
    def go2control2(self)->None:
        self.master.switchPage(Control2)

class Control2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2control1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="반복문 : while, for",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=150)

        self.next = tk.Button(con1,text="다음으로",command=self.go2struct1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=4,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext4)
        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con3,font=("Helvetica", 13),height=7,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext5)
        # 컨테이너4
        con4 = tk.Frame(self)
        con4.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con4,font=("Helvetica", 13),height=7,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext6)
        # 컨테이너5
        con5 = tk.Frame(self)
        con5.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con5,font=("Helvetica", 13),height=10,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ctext7)

    def go2control1(self)->None:
        self.master.switchPage(Control1)
    def go2struct1(self)->None:
        self.master.switchPage(Struct1)

from static.struct import *
class Struct1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2control2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="자료형",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2struct2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,stext1)

    def go2control2(self)->None:
        self.master.switchPage(Control2)
    def go2struct2(self)->None:
        self.master.switchPage(Struct2)

class Struct2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2struct1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="자료형 : 정수형,실수형",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=150)

        self.next = tk.Button(con1,text="다음으로",command=self.go2struct3)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=20,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,stext2)

        # 컨테이너3
        con3 = tk.Frame(self)
        con3.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con3,font=("Helvetica", 13),height=12,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,stext3)

    def go2struct1(self)->None:
        self.master.switchPage(Struct1)
    def go2struct3(self)->None:
        self.master.switchPage(Struct3)

class Struct3(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2struct2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="자료형 : 시퀀스1",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=180)

        self.next = tk.Button(con1,text="다음으로",command=self.go2struct4)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,stext4)

    def go2struct2(self)->None:
        self.master.switchPage(Struct2)
    def go2struct4(self)->None:
        self.master.switchPage(Struct4)

class Struct4(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2struct3)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="자료형 : 시퀀스2,기타",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=150)

        self.next = tk.Button(con1,text="다음으로",command=self.go2func1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,stext5)

    def go2struct3(self)->None:
        self.master.switchPage(Struct3)
    def go2func1(self)->None:
        self.master.switchPage(Func1)

from static.func import *
class Func1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2struct4)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="함수1",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2func2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ftext1)

    def go2struct4(self)->None:
        self.master.switchPage(Struct3)
    def go2func2(self)->None:
        self.master.switchPage(Func2)

class Func2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2func1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="함수2",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2class1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,ftext2)

    def go2func1(self)->None:
        self.master.switchPage(Func1)
    def go2class1(self)->None:
        self.master.switchPage(Class1)

from static.cls import *
class Class1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2func2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="클래스 개요",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2class2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,cltext1)

    def go2func2(self)->None:
        self.master.switchPage(Func2)
    def go2class2(self)->None:
        self.master.switchPage(Class2)

class Class2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2class1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="클래스 작성",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2class3)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,cltext2)

    def go2class1(self)->None:
        self.master.switchPage(Class1)
    def go2class3(self)->None:
        self.master.switchPage(Class3)

class Class3(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2class2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="접근지정자",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2class4)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,cltext3)

    def go2class2(self)->None:
        self.master.switchPage(Class2)
    def go2class4(self)->None:
        self.master.switchPage(Class4)

class Class4(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2class3)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="상속",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2class5)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,cltext4)

    def go2class3(self)->None:
        self.master.switchPage(Class3)
    def go2class5(self)->None:
        self.master.switchPage(Class5)

class Class5(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2class4)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="클래스 메소드,정적 메소드",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=100)

        self.next = tk.Button(con1,text="다음으로",command=self.go2etc1)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,cltext5)

    def go2class4(self)->None:
        self.master.switchPage(Class4)
    def go2etc1(self)->None:
        self.master.switchPage(Etc1)

from static.etc import *
class Etc1(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2class5)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="모듈",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2etc2)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=20,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,etext1)

    def go2class5(self)->None:
        self.master.switchPage(Class5)
    def go2etc2(self)->None:
        self.master.switchPage(Etc2)

class Etc2(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2etc1)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="예외처리",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="다음으로",command=self.go2etc3)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=25,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,etext2)

    def go2etc1(self)->None:
        self.master.switchPage(Etc1)
    def go2etc3(self)->None:
        self.master.switchPage(Etc3)

class Etc3(tk.Frame):
    def __init__(self,master)->None:
        super().__init__(master)
        self.master = master
        self.createWidgets()
    
    def createWidgets(self)->None:
        # 컨테이너1
        con1 = tk.Frame(self)
        con1.pack(side=tk.TOP,anchor=tk.CENTER,pady=20)

        self.start = tk.Button(con1,text="이전으로",command=self.go2etc2)
        self.start.pack(side=tk.LEFT,padx=10)

        self.title = tk.Label(con1,text="파일 처리",font=("Helvetica", 24, "bold"))
        self.title.pack(side=tk.LEFT,padx=200)

        self.next = tk.Button(con1,text="처음으로",command=self.go2first)
        self.next.pack(side=tk.LEFT,padx=10)
        
        # 컨테이너2
        con2 = tk.Frame(self)
        con2.pack(side=tk.TOP,anchor=tk.S,pady=0)

        self.text = tk.Text(con2,font=("Helvetica", 13),height=35,pady=10)
        self.text.pack(side=tk.TOP)
        self.text.insert(tk.END,etext3)

    def go2etc2(self)->None:
        self.master.switchPage(Etc2)
    def go2first(self)->None:
        self.master.switchPage(Pagelist)