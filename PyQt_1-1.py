import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) #PyQt5 QApplication 클래스의 인스턴스를 생성하여 app이라는 변수로 바인딩한다. 인자 값으로 파이썬 파일의 절대 경로를 받음
#event start
label = QLabel("Hello PyQt") #QLabel 클래스의 인스턴스를 생성하여, label이라는 변수로 바인딩
label.show() #label의 내용을 보여주는 해당 과정이 이벤트
#event end
app.exec_() #이벤트 루프(무한 반복하면서 이벤트를 처리하는 상태)에 진입한다. -> 실행하면 계속 실행 창이 출력된 상태인 것을 확인할 수 있음
