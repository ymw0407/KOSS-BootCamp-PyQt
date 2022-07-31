# KOSS-BootCamp-PyQt5
<h3>KOSS BootCamp 5주차 - PyQt</h3>
<br/>
멘토 - 윤민우, 박진우, 이준혁
<br/>

## What is PyQt5?  

### 기존의 파이썬은?
기존의 파이썬으로는 TUI(Text-based User Interface), 즉 결과를 text로만 출력을 하는 방식으로 결과를 출력해왔다.
```python
print("Hello World!")
Hello World!
```

### GUI?
GUI(Graphical User Interface), 즉 우리가 사용하는 윈도우 창과 같은 그래픽 요소를 통해 사용자와 컴퓨터 간의 인터페이스를 구현한 방식이다. wxPython, TkInter, PyQt 등의 GUI 모듈일 있지만, 우리는 PyQt를 사용해보고자 한다.

### PyQt의 특징
- TkInter와는 다르게 추가적인 모듈 설치가 필요하다. [설치 방법](https://github.com/ymw0407/KOSS-BootCamp-PyQt#how-to-install-pyqt5) 
- Qt라는 GUI 프로그램 개발에 널리 사용되는 크로스 플랫폼 프레임워크(C++)를 Python으로 바인딩한 것이 PyQt!
- 여기서 크로스 플랫폼 프레임워크란... 윈도우나 리눅스와 같은 운영체제에 상관없이 같은 코드로 각 운영체제에서 동작하는 프로그램 개발을 지원하는 것을 의미한다!

## How to install PyQt5?
```bash
$ pip install PyQt5
```
### 해당 오류 발생시...
```python
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
```
<br/>
```bash
$ apt install libxcb-xinerama0
```
