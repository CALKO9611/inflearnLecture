import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Window 메모장")
root.geometry("640x480") 

# 열기, 저장 파일 이름 설정
filename = "mynote.txt"

# 메뉴
def open_file():
  if os.path.isfile(filename) :
    with open(filename, "r", encoding="utf8") as file:
      txt.delete("1.0", END) # 삭제 후
      txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
  with open(filename, "w", encoding="utf8") as file:
    file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator() # 구분자
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식" )
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()