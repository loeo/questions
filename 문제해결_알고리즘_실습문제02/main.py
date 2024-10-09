#모든 변수에서 모듈 불러오기
from tkinter import *
#전역변수 photo7, photo8 초기화
photo7, photo8 = None, None
#new_win1() 함수의 정의
def new_win1():
    #전역변수 photo7 선언
    global photo7
    #변수 new_win1을 새롭게 만들어지는 윈도우로 정의
    new_win1 = Toplevel(window)
    #new_win1의 크기 설정
    new_win1.geometry('320x320')
    #new_win1의 제목 설정
    new_win1.title('새롭게 만들어진 이미지 윈도우 창')
    #전역변수 photo7을 절대경로 android/android07.gif로 정의
    photo7 = PhotoImage(file='android/android07.gif')
    #변수 label1 선언 및 변수 label1을 new_win1 윈도우 창 내 photo7으로 설정되어 있는 image 특성의 Label로 정의
    label1 = Label(new_win1, image=photo7)
    #변수 button 선언 및 변수 button을 이름이 '종료하기'이며 클릭시 나가기 이벤트를 실행하는 Botton으로 정의
    button = Button(new_win1, text='종료하기', command=quit)
    #label1 배치
    label1.pack()
    #button 배치
    button.pack()

#new_win2() 함수의 정의
def new_win2():
    #전역변수 photo8 선언
    global photo8
    #변수 new_win2을 새롭게 만들어지는 윈도우로 정의
    new_win2 = Toplevel(window)
    #new_win2의 크기 설정
    new_win2.geometry('320x320')
    #new_win2의 제목 설정
    new_win2.title('새롭게 만들어진 메뉴 윈도우 창')
    #전역변수 phot8을 절대경로 android/android08.gif로 정의
    photo8 = PhotoImage(file='android/android08.gif')
    #변수 label2 선언 및 변수 label2을 new_win2 윈도우 창 내 photo8으로 설정되어 있는 image 특성의 Label로 정의
    label2 = Label(new_win2, image=photo8)
    #label2 배치
    label2.pack()
    #new_win2의 메뉴를 생성한다
    menubar = Menu(new_win2)
    #상위메뉴 menu1을 생성한다
    menu1 = Menu(menubar, tearoff=0)
    #menu1에 하위 메뉴를 추가한다
    menu1.add_command(label='하위메뉴 1-1')
    #menu1에 하위 메뉴를 추가한다
    menu1.add_command(label='하위메뉴 1-2')
    #menu1에 하위 메뉴를 추가한다
    menu1.add_command(label='하위메뉴 1-3', command=quit)
    #menubar에 상위메뉴를 연결한다
    menubar.add_cascade(label='상위메뉴 1', menu=menu1)
    #new_win2에 메뉴를 등록한다
    new_win2.config(menu=menubar)

#길이가 6인 btnList 배열 선언 및 초기화
btnList = [None] * 6
#길이가 6인 frameList 배열 선언 및 정의
fnameList = ['android01.gif', 'android02.gif', 'android03.gif'
    , 'android04.gif', 'android05.gif', 'android06.gif']
#길이가 6인 photoList 배열 선언 및 초기화
photoList = [None] * 6

#변수 xPos, yPos를 각각 0으로 초기화
xPos, yPos = 0, 0
#변수 num 선언 및 초기화
num = 0
#여기까지는 초기 설정


#코드시작(실행시): 윈도우창을 띄운다
window = Tk()
#윈도우창의 제목을 안드로이드로 설정
window.title('안드로이드')
#윈도우 창의 크기를 540*360으로 설정
window.geometry('540x360')

#i가 0~5까지의 범위일 떄 실행
for i in range(6):
    #i번 photoList배열에 frameLIst[i]이미지로 이미지 설정
    photoList[i] = PhotoImage(file='android/' + fnameList[i])
    #만약, i가 1(2번째 사진)일 때 new_win1을 실행하는 image 타입 버튼을 생성
    if i == 1:
        btnList[i] = Button(window, image=photoList[i], command=new_win1)
    #아니면 만약 i가 4(5번째 사진) 일 때, new_win2을 실행하는 image 타입 버튼을 생성
    elif i == 4:
        btnList[i] = Button(window, image=photoList[i], command=new_win2)
    #그 외의 경우, image 타입 버튼 생성
    else:
        btnList[i] = Button(window, image=photoList[i])

#i가 0~1 범위일 때 실행
for i in range(2):
    #j가 0~2 범위일 때 실행
    for j in range(3):
        #num(초기값: 0)번 버튼을 x좌표: xPos(초기값: 0), y좌표: yPos(초기값: 0)에 배치한다.
        btnList[num].place(x=xPos, y=yPos)
        #xPos 값에 180더하기
        xPos += 180
        #num 값에 1 더하기
        num += 1
    #(반복문 탈출 후) xPos를 0으로 정하고 yPos 값에 180 더하기
    xPos = 0
    yPos += 180

#코드 끝
window.mainloop()
