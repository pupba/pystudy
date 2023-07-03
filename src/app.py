from pages import *
# 페이지 리스트        
PAGE = [MainPage,Pagelist,Overview1,Overview2,Overview3,
        Basic1,Basic2,Basic3,Control1,Control2,
        Struct1,Struct2,Struct3,Struct4,Func1,Func2,
        Class1,Class2,Class3,Class4,Class5,Etc1,Etc2,Etc3]

class App(tk.Tk):
    def __init__(self)->None:
        super().__init__()
        self.title("파이썬 Basic 훈련 프로그램")
        self.geometry("720x640")
        self.pages = {}

        self.createPages()
        self.switchPage(MainPage)

    def createPages(self)->None:
        self.grid_rowconfigure(0, weight=5)  # 첫 번째 행을 확장하여 중앙에 위치하도록 설정
        self.grid_columnconfigure(0, weight=1)  # 첫 번째 열을 확장하여 중앙에 위치하도록 설정

        for Page in PAGE:
            page = Page(self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
    
    def switchPage(self,Page:tk.Frame)->None:
        page = self.pages[Page]
        page.tkraise()