####---------This is script is my mini-work project during the 2021 in my third year second semester in KNUST.
####------The porject is about designing a simple chatroom application called chatbox for a firm..It uses the python sockect programming to send
### messages to another script called a server.. the server then emit or broadcast the message to individual clients connected using its port
## and local IP address..i completed this project on 21-07-2021..
##--challenges-- sending picture messages was really disburbing and it took much of my time which was completely resolve on 24-07-21.....
import os
import sys
import time
import book
import string
import random
import socket
import pathlib
import bookbox
import datetime
import importlib
import threading
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from playsound import *


HOST = socket.gethostbyname(socket.gethostname())
PORT = 4545
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))

class vero():
    def __init__(self):

        app=QApplication(sys.argv)
        self.win = QMainWindow()
        self.win.setWindowOpacity(0.97)
        self.win.setWindowTitle("granny")
        self.win.setFixedSize(1100,600)
        self.win.move(170,70)
        self.win.setWindowIcon(QIcon(':win'))
        self.win.setStyleSheet("background-color:rgb(5%,5%,5%);")

#----------settting frame-----------------------------------------------------------------------------------------------------------------
        self.setingframe=QFrame(self.win)
        self.setingframe.move(0,0)
        self.setingframe.resize(50,600)
        self.setingframe.setStyleSheet("background-color:rgb(10%,10%,10%);")

        self.menubtn=QPushButton(self.win)
        self.menubtn.move(10,150)
        self.menubtn.setFlat(True)
        self.menubtn.resize(30,30)
        self.menubtn.setIcon(QIcon(':menu'))
        self.menubtn.setToolTip('menu')
        self.menubtn.setIconSize(QSize(30,30))
        self.menubtn.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.menubtn.clicked.connect(self.menubtnfun)

        self.setingbtn=QPushButton(self.win)
        self.setingbtn.move(10,200)
        self.setingbtn.setFlat(True)
        self.setingbtn.resize(30,30)
        self.setingbtn.setToolTip('settings')
        self.setingbtn.setIcon(QIcon(':settings'))
        self.setingbtn.setIconSize(QSize(30,30))
        self.setingbtn.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.setingbtn.clicked.connect(self.settingbtnfun)      

        self.calbtn=QPushButton(self.win)
        self.calbtn.move(10,250)
        self.calbtn.setFlat(True)
        self.calbtn.resize(30,30)
        self.calbtn.setToolTip('calendar')
        self.calbtn.setIcon(QIcon(':calendar'))
        self.calbtn.setIconSize(QSize(30,30))
        self.calbtn.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.calbtn.clicked.connect(self.calbtnfun)
        
        self.notesbtn=QPushButton(self.win)
        self.notesbtn.move(10,300)
        self.notesbtn.setFlat(True)
        self.notesbtn.resize(30,30)
        self.notesbtn.setToolTip('note')
        self.notesbtn.setIcon(QIcon(':note'))
        self.notesbtn.setIconSize(QSize(30,30))
        self.notesbtn.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.notesbtn.clicked.connect(self.notebtnfun)

        self.start=QLabel('start',self.win)
        self.start.resize(40,30)
        self.start.move(10,330)
        self.start.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:15px;color:#DDDDDD;")
        
        self.onlinebtn=QPushButton(self.win)
        self.onlinebtn.move(10,360)
        self.onlinebtn.setFlat(True)
        self.onlinebtn.resize(30,30)
        self.onlinebtn.setToolTip('on/off')
        self.onlinebtn.setIcon(QIcon(':feed'))
        self.onlinebtn.setIconSize(QSize(30,30))
        self.onlinebtn.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.onlinebtn.clicked.connect(self.engine)

        self.theml=QLabel('-theme-',self.win)
        self.theml.resize(50,30)
        self.theml.move(0,525)
        self.theml.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:13px;color:#DDDDDD;")

        self.bradio = QRadioButton('Dark',self.win)
        self.bradio.resize(50,30)
        self.bradio.move(0,550)
        self.bradio.setChecked(True)
        self.bradio.setStyleSheet("background-color:rgb(10%,10%,10%);color:tomato;font-size:11px;")
        self.bradio.toggled.connect(self.theme)

        self.wradio = QRadioButton('white',self.win)
        self.wradio.resize(50,30)
        self.wradio.move(0,570)
        self.wradio.setStyleSheet("background-color:rgb(10%,10%,10%);color:tomato;font-size:11px;")
        self.wradio.toggled.connect(self.theme)
##-------------------------------------------------------------Active Frame ------------------------------------------    
        self.activeframe=QFrame(self.win)
        self.activeframe.move(60,20)
        self.activeframe.resize(200,570)
        self.activeframe.setFrameShadow(QFrame.Raised)
        self.activeframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:5px 5px 5px 5px;")
        
        self.activeicon=QLabel(self.win,text='☃')
        self.activeicon.move(220,25)
        self.activeicon.resize(40,40)
        self.activeicon.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:30px;font-weight:bold")

        self.activename=QLabel(self.win)
        self.activename.move(70,30)
        self.activename.resize(155,40)
        self.activename.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:30px;font-weight:bold;"
                                      "font-family:monospace,lobster;color:#CCCCCC;")
        self.profr=QLabel(self.win)
        self.profr.move(70,80)
        self.profr.resize(180,100)
        self.profr.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px 5px 5px 5px;border:1px solid #191970;")
        
        self.activelabel=QLabel(self.win,text='<center>offline</center>')
        self.activelabel.move(70,200)
        self.activelabel.resize(180,40)
        self.activelabel.setStyleSheet("background-color:#2B65EC;border-radius:20px 20px 20px 20px;font-family:monospace;font-size:15px;color:white;font-weight:bold;")
        
        self.listscreen=QTextEdit(self.win)
        self.listscreen.move(70,250)
        self.listscreen.resize(180,330)
        self.listscreen.setReadOnly(True)
        self.listscreen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listscreen.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listscreen.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:2px;color:#83a8c3;font-size:17px;")
#----------------------------------------------------Chat Frame----------------------------------------------------------------------
        self.lname=QLabel(self.win,text='..chaTBox..')
        self.lname.move(270,5)
        self.lname.setStyleSheet("color:tomato;font-size:18px;font-family:monospace;font-weight:bold;")

        self.l1=QLabel(self.win)
        self.l1.move(753,10)
        self.l1.resize(17,17)
        self.l1.setStyleSheet("background-color:rgb(200,0,0);border-radius:8px;")

        self.l2=QLabel(self.win)
        self.l2.move(775,10)
        self.l2.resize(17,17)
        self.l2.setStyleSheet("background-color:rgb(255,0,255);border-radius:8px;")

        self.l3=QLabel(self.win)
        self.l3.move(797,10)
        self.l3.resize(17,17)
        self.l3.setStyleSheet("background-color:rgb(255,192,03);border-radius:8px;")

        self.l4=QLabel(self.win)
        self.l4.move(819,10)
        self.l4.resize(17,17)
        self.l4.setStyleSheet("background-color:green;border-radius:8px;")

        self.l5=QLabel(self.win)
        self.l5.move(841,10)
        self.l5.resize(17,17)
        self.l5.setStyleSheet("background-color:rgb(98,176,255);border-radius:8px;")

        self.l6=QLabel(self.win)
        self.l6.move(863,10)
        self.l6.resize(17,17)
        self.l6.setStyleSheet("background-color:rgb(255,228,225);border-radius:8px;")

        self.chatframe=QTextEdit(self.win)
        self.chatframe.move(265,30)
        self.chatframe.resize(620,520)
        self.chatframe.setReadOnly(True)
        self.chatframe.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatframe.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatframe.setStyleSheet("Background-color:rgb(5%,5%,5%);border-radius:2px;font-size:15px;color:#83a8c3;")
#--------------------------------------------------------------------------Text Frame-------------------------------------------
        self.textframe=QFrame(self.win)
        self.textframe.move(320,525)
        self.textframe.resize(345,65)
        self.textframe.setFrameShadow(QFrame.Raised)
        self.textframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-top-left-radius:10px;border-bottom-left-radius:10px;")

        self.textframe=QFrame(self.win)
        self.textframe.move(670,525)
        self.textframe.resize(155,65)
        self.textframe.setFrameShadow(QFrame.Raised)
        self.textframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-top-right-radius:10px;border-bottom-right-radius:10px;")
    
        self.textpad=QTextEdit(self.win)
        self.textpad.move(323,528)
        self.textpad.resize(340,60)
        self.textpad.setPlaceholderText('\n ✍  Type something here......')
        self.textpad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textpad.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textpad.textChanged.connect(self.textpadtch)
        self.textpad.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:15px;color:#DDDDDD;font-family:monospace;border-radius:1px;font-weight:bold;")                    

        self.sendbtn=QPushButton(self.win)
        self.sendbtn.move(788,540)
        self.sendbtn.resize(35,35)
        self.sendbtn.setToolTip('send')
        self.sendbtn.setIcon(QIcon(':send'))
        self.sendbtn.setFlat(True)
        self.sendbtn.setIconSize(QSize(30,30))
        self.sendbtn.clicked.connect(self.sendbtnfun)
        
        self.filebtn=QPushButton(self.win)
        self.filebtn.move(750,540)
        self.filebtn.resize(35,35)
        self.filebtn.setToolTip('choose file')
        self.filebtn.setIcon(QIcon(':file'))
        self.filebtn.setFlat(True)
        self.filebtn.setIconSize(QSize(30,30))
        self.filebtn.clicked.connect(self.filebtnfun)

        self.emojbtn=QPushButton(self.win)
        self.emojbtn.move(713,540)
        self.emojbtn.resize(35,35)
        self.emojbtn.setToolTip('icons')
        self.emojbtn.setIcon(QIcon(':emoji'))
        self.emojbtn.setFlat(True)
        self.emojbtn.setIconSize(QSize(30,30))
        self.emojbtn.clicked.connect(self.emojibtnfun)

        self.mikebtn=QPushButton(self.win)
        self.mikebtn.move(678,540)
        self.mikebtn.resize(35,35)
        self.mikebtn.setToolTip('speech-to-text')
        self.mikebtn.setIcon(QIcon(':tspeech'))
        self.mikebtn.setFlat(True)
        self.mikebtn.setIconSize(QSize(30,30))
#-------------------------------------------------------------------------------------------Status frame-------------------
        self.statusframe=QFrame(self.win)
        self.statusframe.move(890,20)
        self.statusframe.resize(200,570)
        self.statusframe.setFrameShadow(QFrame.Raised)
        self.statusframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:5px 5px 5px 5px;")

        self.timelabel=QLabel(self.win)
        self.timelabel.move(895,25)
        self.timelabel.resize(190,40)
        self.timelabel.setStyleSheet("background-color:rgb(5%,5%,5%);")
        
        self.clockicon=QLabel(self.win)
        self.clockicon.setPixmap(QPixmap(':clock'))
        self.clockicon.move(892,25)
        self.clockicon.resize(50,40)
        self.clockicon.show()

        self.time =QLabel(self.win)
        self.time.move(935,25)
        self.time.resize(153,40)
        self.time.setText(datetime.datetime.now().strftime('%a %b %d,%Y-%H:%M:%S'))
        self.time.setStyleSheet("color:#EEEEEE;font-size:13px;")                      

        self.to_dol=QLabel(self.win,text='<h2><b>To Do List</b></h2>')
        self.to_dol.move(900,85)
        self.to_dol.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:11px;font-family:monospace;")

        self.to_do=QTextEdit(self.win)
        self.to_do.move(900,110)
        self.to_do.resize(180,200)
        self.to_do.setReadOnly(True)
        self.to_do.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.to_do.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.to_do.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px;")
        
        self.dailyg=QLabel(self.win,text='<h2><b>Daily Grow</b></h2>')
        self.dailyg.move(900,310)
        self.dailyg.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:11px;font-family:monospace;")
        
        self.inspire=QTextEdit(self.win)
        self.inspire.move(900,335)
        self.inspire.resize(180,245)
        self.inspire.setReadOnly(True)
        self.inspire.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inspire.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inspire.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px;font-size:15px;")

        self.loginpage = QWidget(self.win)
        self.loginpage.setFixedSize(1100,600)
        self.loginpage.move(0,0)
        self.loginpage.setStyleSheet("background-color:#EEEEEE;")
        self.loglabel=QLabel('..chaTBox..',self.loginpage)
        self.loglabel.move(320,150)
        self.loglabel.setStyleSheet("color:tomato;font-family:monospace,lobster;font-size:100px;")
        self.logname = QLineEdit(self.loginpage)
        self.logname.resize(300,30)
        self.logname.move(400,350)
        self.logname.setPlaceholderText('Username')
        self.logname.setStyleSheet("font-size:15px;")
        self.logbtn=QPushButton('login',self.loginpage)
        self.logbtn.resize(100,35)
        self.logbtn.move(500,400)
        self.logbtn.setFlat(False)
        self.logbtn.setStyleSheet("background-color:#2B65EC;font-size:17px;color:white;")
        self.logbtn.clicked.connect(self.loginfun)
        self.logcola=QLabel('twumwaa.org copyright © v2021',self.loginpage)
        self.logcola.move(915,580)
####--------------------------------------emoji widget--------------------------------------------------------------------------------
        self.message=''
        self.emdock = QWidget(self.win)
        self.emdock.setFixedSize(315,257)
        self.emdock.move(570,258)
        self.emdock.setStyleSheet("background-color:rgb(5%,5%,5%);")
        self.emdock.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.emdock.setWindowOpacity(0.1)

        self.em1= QPushButton(self.emdock)
        self.em1.resize(30,30)
        self.em1.move(2,2)
        self.em1.setIcon(QIcon(':em1'))
        self.em1.setFlat(True)
        self.em1.setIconSize(QSize(30,30))
        self.em1.clicked.connect(lambda:self.sendmessage(':em1'))

        self.em2= QPushButton(self.emdock)
        self.em2.resize(30,30)
        self.em2.move(32,2)
        self.em2.setIcon(QIcon(':em2'))
        self.em2.setFlat(True)
        self.em2.setIconSize(QSize(30,30))
        self.em2.clicked.connect(lambda:self.sendmessage(':em2'))

        self.em3= QPushButton(self.emdock)
        self.em3.resize(30,30)
        self.em3.move(64,2)
        self.em3.setIcon(QIcon(':em3'))
        self.em3.setFlat(True)
        self.em3.setIconSize(QSize(30,30))
        self.em3.clicked.connect(lambda:self.sendmessage(':em3'))

        self.em4= QPushButton(self.emdock)
        self.em4.resize(30,30)
        self.em4.move(96,2)
        self.em4.setIcon(QIcon(':em3'))
        self.em4.setFlat(True)
        self.em4.setIconSize(QSize(30,30))
        self.em4.clicked.connect(lambda:self.sendmessage(':em4'))

        self.em5= QPushButton(self.emdock)
        self.em5.resize(30,30)
        self.em5.move(128,2)
        self.em5.setIcon(QIcon(':em5'))
        self.em5.setFlat(True)
        self.em5.setIconSize(QSize(30,30))
        self.em5.clicked.connect(lambda:self.sendmessage(':em5'))

        self.em6= QPushButton(self.emdock)
        self.em6.resize(30,30)
        self.em6.move(160,2)
        self.em6.setIcon(QIcon(':em6'))
        self.em6.setFlat(True)
        self.em6.setIconSize(QSize(30,30))
        self.em6.clicked.connect(lambda:self.sendmessage(':em6'))

        self.em7= QPushButton(self.emdock)
        self.em7.resize(30,30)
        self.em7.move(192,2)
        self.em7.setIcon(QIcon(':em7'))
        self.em7.setFlat(True)
        self.em7.setIconSize(QSize(30,30))
        self.em7.clicked.connect(lambda:self.sendmessage(':em7'))

        self.em8= QPushButton(self.emdock)
        self.em8.resize(30,30)
        self.em8.move(224,2)
        self.em8.setIcon(QIcon(':em8'))
        self.em8.setFlat(True)
        self.em8.setIconSize(QSize(30,30))
        self.em8.clicked.connect(lambda:self.sendmessage(':em8'))

        self.em9= QPushButton(self.emdock)
        self.em9.resize(30,30)
        self.em9.move(256,2)
        self.em9.setIcon(QIcon(':em9'))
        self.em9.setFlat(True)
        self.em9.setIconSize(QSize(30,30))
        self.em9.clicked.connect(lambda:self.sendmessage(':em9'))

        self.em10= QPushButton(self.emdock)
        self.em10.resize(30,30)
        self.em10.move(288,2)
        self.em10.setIcon(QIcon(':em10'))
        self.em10.setFlat(True)
        self.em10.setIconSize(QSize(30,30))
        self.em10.clicked.connect(lambda:self.sendmessage(':em10'))

        self.em11= QPushButton(self.emdock)
        self.em11.resize(30,30)
        self.em11.move(2,32)
        self.em11.setIcon(QIcon(':em11'))
        self.em11.setFlat(True)
        self.em11.setIconSize(QSize(30,30))
        self.em11.clicked.connect(lambda:self.sendmessage(':em11'))

        self.em12= QPushButton(self.emdock)
        self.em12.resize(30,30)
        self.em12.move(32,32)
        self.em12.setIcon(QIcon(':em12'))
        self.em12.setFlat(True)
        self.em12.setIconSize(QSize(30,30))
        self.em12.clicked.connect(lambda:self.sendmessage(':em12'))

        self.em13= QPushButton(self.emdock)
        self.em13.resize(30,30)
        self.em13.move(64,32)
        self.em13.setIcon(QIcon(':em13'))
        self.em13.setFlat(True)
        self.em13.setIconSize(QSize(30,30))
        self.em13.clicked.connect(lambda:self.sendmessage(':em13'))

        self.em14= QPushButton(self.emdock)
        self.em14.resize(30,30)
        self.em14.move(96,32)
        self.em14.setIcon(QIcon(':em14'))
        self.em14.setFlat(True)
        self.em14.setIconSize(QSize(30,30))
        self.em14.clicked.connect(lambda:self.sendmessage(':em14'))

        self.em15= QPushButton(self.emdock)
        self.em15.resize(30,30)
        self.em15.move(128,32)
        self.em15.setIcon(QIcon(':em15'))
        self.em15.setFlat(True)
        self.em15.setIconSize(QSize(30,30))
        self.em15.clicked.connect(lambda:self.sendmessage(':em15'))

        self.em16= QPushButton(self.emdock)
        self.em16.resize(30,30)
        self.em16.move(160,32)
        self.em16.setIcon(QIcon(':em16'))
        self.em16.setFlat(True)
        self.em16.setIconSize(QSize(30,30))
        self.em16.clicked.connect(lambda:self.sendmessage(':em16'))

        self.em17= QPushButton(self.emdock)
        self.em17.resize(30,30)
        self.em17.move(192,32)
        self.em17.setIcon(QIcon(':em17'))
        self.em17.setFlat(True)
        self.em17.setIconSize(QSize(30,30))
        self.em17.clicked.connect(lambda:self.sendmessage(':em17'))

        self.em18= QPushButton(self.emdock)
        self.em18.resize(30,30)
        self.em18.move(224,32)
        self.em18.setIcon(QIcon(':em18'))
        self.em18.setFlat(True)
        self.em18.setIconSize(QSize(30,30))
        self.em18.clicked.connect(lambda:self.sendmessage(':em18'))

        self.em19= QPushButton(self.emdock)
        self.em19.resize(30,30)
        self.em19.move(256,32)
        self.em19.setIcon(QIcon(':em19'))
        self.em19.setFlat(True)
        self.em19.setIconSize(QSize(30,30))
        self.em19.clicked.connect(lambda:self.sendmessage(':em19'))

        self.em20= QPushButton(self.emdock)
        self.em20.resize(30,30)
        self.em20.move(288,32)
        self.em20.setIcon(QIcon(':em20'))
        self.em20.setFlat(True)
        self.em20.setIconSize(QSize(30,30))
        self.em20.clicked.connect(lambda:self.sendmessage(':em20'))

        self.em21= QPushButton(self.emdock)
        self.em21.resize(30,30)
        self.em21.move(2,64)
        self.em21.setIcon(QIcon(':em21'))
        self.em21.setFlat(True)
        self.em21.setIconSize(QSize(30,30))
        self.em21.clicked.connect(lambda:self.sendmessage(':em21'))

        self.em22= QPushButton(self.emdock)
        self.em22.resize(30,30)
        self.em22.move(32,64)
        self.em22.setIcon(QIcon(':em22'))
        self.em22.setFlat(True)
        self.em22.setIconSize(QSize(30,30))
        self.em22.clicked.connect(lambda:self.sendmessage(':em22'))

        self.em23= QPushButton(self.emdock)
        self.em23.resize(30,30)
        self.em23.move(64,64)
        self.em23.setIcon(QIcon(':em23'))
        self.em23.setFlat(True)
        self.em23.setIconSize(QSize(30,30))
        self.em23.clicked.connect(lambda:self.sendmessage(':em23'))

        self.em24= QPushButton(self.emdock)
        self.em24.resize(30,30)
        self.em24.move(96,64)
        self.em24.setIcon(QIcon(':em24'))
        self.em24.setFlat(True)
        self.em24.setIconSize(QSize(30,30))
        self.em24.clicked.connect(lambda:self.sendmessage(':em24'))

        self.em25= QPushButton(self.emdock)
        self.em25.resize(30,30)
        self.em25.move(128,64)
        self.em25.setIcon(QIcon(':em25'))
        self.em25.setFlat(True)
        self.em25.setIconSize(QSize(30,30))
        self.em25.clicked.connect(lambda:self.sendmessage(':em25'))

        self.em26= QPushButton(self.emdock)
        self.em26.resize(30,30)
        self.em26.move(160,64)
        self.em26.setIcon(QIcon(':em26'))
        self.em26.setFlat(True)
        self.em26.setIconSize(QSize(30,30))
        self.em26.clicked.connect(lambda:self.sendmessage(':em26'))

        self.em27= QPushButton(self.emdock)
        self.em27.resize(30,30)
        self.em27.move(192,64)
        self.em27.setIcon(QIcon(':em27'))
        self.em27.setFlat(True)
        self.em27.setIconSize(QSize(30,30))
        self.em27.clicked.connect(lambda:self.sendmessage(':em27'))

        self.em28= QPushButton(self.emdock)
        self.em28.resize(30,30)
        self.em28.move(224,64)
        self.em28.setIcon(QIcon(':em28'))
        self.em28.setFlat(True)
        self.em28.setIconSize(QSize(30,30))
        self.em28.clicked.connect(lambda:self.sendmessage(':em28'))

        self.em29= QPushButton(self.emdock)
        self.em29.resize(30,30)
        self.em29.move(256,64)
        self.em29.setIcon(QIcon(':em29'))
        self.em29.setFlat(True)
        self.em29.setIconSize(QSize(30,30))
        self.em29.clicked.connect(lambda:self.sendmessage(':em29'))

        self.em30= QPushButton(self.emdock)
        self.em30.resize(30,30)
        self.em30.move(288,64)
        self.em30.setIcon(QIcon(':em30'))
        self.em30.setFlat(True)
        self.em30.setIconSize(QSize(30,30))
        self.em30.clicked.connect(lambda:self.sendmessage(':em30'))

        self.em31= QPushButton(self.emdock)
        self.em31.resize(30,30)
        self.em31.move(2,96)
        self.em31.setIcon(QIcon(':em31'))
        self.em31.setFlat(True)
        self.em31.setIconSize(QSize(30,30))
        self.em31.clicked.connect(lambda:self.sendmessage(':em31'))

        self.em32= QPushButton(self.emdock)
        self.em32.resize(30,30)
        self.em32.move(32,96)
        self.em32.setIcon(QIcon(':em32'))
        self.em32.setFlat(True)
        self.em32.setIconSize(QSize(30,30))
        self.em32.clicked.connect(lambda:self.sendmessage(':em32'))

        self.em33= QPushButton(self.emdock)
        self.em33.resize(30,30)
        self.em33.move(64,96)
        self.em33.setIcon(QIcon(':em33'))
        self.em33.setFlat(True)
        self.em33.setIconSize(QSize(30,30))
        self.em33.clicked.connect(lambda:self.sendmessage(':em33'))

        self.em34= QPushButton(self.emdock)
        self.em34.resize(30,30)
        self.em34.move(96,96)
        self.em34.setIcon(QIcon(':em34'))
        self.em34.setFlat(True)
        self.em34.setIconSize(QSize(30,30))
        self.em34.clicked.connect(lambda:self.sendmessage(':em34'))

        self.em35= QPushButton(self.emdock)
        self.em35.resize(30,30)
        self.em35.move(128,96)
        self.em35.setIcon(QIcon(':em35'))
        self.em35.setFlat(True)
        self.em35.setIconSize(QSize(30,30))
        self.em35.clicked.connect(lambda:self.sendmessage(':em35'))

        self.em36= QPushButton(self.emdock)
        self.em36.resize(30,30)
        self.em36.move(160,96)
        self.em36.setIcon(QIcon(':em36'))
        self.em36.setFlat(True)
        self.em36.setIconSize(QSize(30,30))
        self.em36.clicked.connect(lambda:self.sendmessage(':em36'))

        self.em37= QPushButton(self.emdock)
        self.em37.resize(30,30)
        self.em37.move(192,96)
        self.em37.setIcon(QIcon(':em37'))
        self.em37.setFlat(True)
        self.em37.setIconSize(QSize(30,30))
        self.em37.clicked.connect(lambda:self.sendmessage(':em37'))

        self.em38= QPushButton(self.emdock)
        self.em38.resize(30,30)
        self.em38.move(224,96)
        self.em38.setIcon(QIcon(':em38'))
        self.em38.setFlat(True)
        self.em38.setIconSize(QSize(30,30))
        self.em38.clicked.connect(lambda:self.sendmessage(':em38'))

        self.em39= QPushButton(self.emdock)
        self.em39.resize(30,30)
        self.em39.move(256,96)
        self.em39.setIcon(QIcon(':em39'))
        self.em39.setFlat(True)
        self.em39.setIconSize(QSize(30,30))
        self.em39.clicked.connect(lambda:self.sendmessage(':em39'))

        self.em40= QPushButton(self.emdock)
        self.em40.resize(30,30)
        self.em40.move(288,96)
        self.em40.setIcon(QIcon(':em40'))
        self.em40.setFlat(True)
        self.em40.setIconSize(QSize(30,30))
        self.em40.clicked.connect(lambda:self.sendmessage(':em40'))

        self.em41= QPushButton(self.emdock)
        self.em41.resize(30,30)
        self.em41.move(2,128)
        self.em41.setIcon(QIcon(':em41'))
        self.em41.setFlat(True)
        self.em41.setIconSize(QSize(30,30))
        self.em41.clicked.connect(lambda:self.sendmessage(':em41'))

        self.em42= QPushButton(self.emdock)
        self.em42.resize(30,30)
        self.em42.move(32,128)
        self.em42.setIcon(QIcon(':em42'))
        self.em42.setFlat(True)
        self.em42.setIconSize(QSize(30,30))
        self.em42.clicked.connect(lambda:self.sendmessage(':em42'))

        self.em43= QPushButton(self.emdock)
        self.em43.resize(30,30)
        self.em43.move(64,128)
        self.em43.setIcon(QIcon(':em43'))
        self.em43.setFlat(True)
        self.em43.setIconSize(QSize(30,30))
        self.em43.clicked.connect(lambda:self.sendmessage(':em43'))

        self.em44= QPushButton(self.emdock)
        self.em44.resize(30,30)
        self.em44.move(96,128)
        self.em44.setIcon(QIcon(':em44'))
        self.em44.setFlat(True)
        self.em44.setIconSize(QSize(30,30))
        self.em44.clicked.connect(lambda:self.sendmessage(':em44'))

        self.em45= QPushButton(self.emdock)
        self.em45.resize(30,30)
        self.em45.move(128,128)
        self.em45.setIcon(QIcon(':em25'))
        self.em45.setFlat(True)
        self.em45.setIconSize(QSize(30,30))
        self.em45.clicked.connect(lambda:self.sendmessage(':em25'))

        self.em46= QPushButton(self.emdock)
        self.em46.resize(30,30)
        self.em46.move(160,128)
        self.em46.setIcon(QIcon(':em46'))
        self.em46.setFlat(True)
        self.em46.setIconSize(QSize(30,30))
        self.em46.clicked.connect(lambda:self.sendmessage(':em46'))

        self.em47= QPushButton(self.emdock)
        self.em47.resize(30,30)
        self.em47.move(192,128)
        self.em47.setIcon(QIcon(':em47'))
        self.em47.setFlat(True)
        self.em47.setIconSize(QSize(30,30))
        self.em47.clicked.connect(lambda:self.sendmessage(':em47'))

        self.em48= QPushButton(self.emdock)
        self.em48.resize(30,30)
        self.em48.move(224,128)
        self.em48.setIcon(QIcon(':em48'))
        self.em48.setFlat(True)
        self.em48.setIconSize(QSize(30,30))
        self.em48.clicked.connect(lambda:self.sendmessage(':em48'))

        self.em49= QPushButton(self.emdock)
        self.em49.resize(30,30)
        self.em49.move(256,128)
        self.em49.setIcon(QIcon(':em49'))
        self.em49.setFlat(True)
        self.em49.setIconSize(QSize(30,30))
        self.em49.clicked.connect(lambda:self.sendmessage(':em49'))

        self.em50= QPushButton(self.emdock)
        self.em50.resize(30,30)
        self.em50.move(288,128)
        self.em50.setIcon(QIcon(':em50'))
        self.em50.setFlat(True)
        self.em50.setIconSize(QSize(30,30))
        self.em50.clicked.connect(lambda:self.sendmessage(':em50'))

        self.em51= QPushButton(self.emdock)
        self.em51.resize(30,30)
        self.em51.move(2,160)
        self.em51.setIcon(QIcon(':em51'))
        self.em51.setFlat(True)
        self.em51.setIconSize(QSize(30,30))
        self.em51.clicked.connect(lambda:self.sendmessage(':em51'))

        self.em52= QPushButton(self.emdock)
        self.em52.resize(30,30)
        self.em52.move(32,160)
        self.em52.setIcon(QIcon(':em52'))
        self.em52.setFlat(True)
        self.em52.setIconSize(QSize(30,30))
        self.em52.clicked.connect(lambda:self.sendmessage(':em52'))

        self.em53= QPushButton(self.emdock)
        self.em53.resize(30,30)
        self.em53.move(64,160)
        self.em53.setIcon(QIcon(':em53'))
        self.em53.setFlat(True)
        self.em53.setIconSize(QSize(30,30))
        self.em53.clicked.connect(lambda:self.sendmessage(':em53'))

        self.em54= QPushButton(self.emdock)
        self.em54.resize(30,30)
        self.em54.move(96,160)
        self.em54.setIcon(QIcon(':em54'))
        self.em54.setFlat(True)
        self.em54.setIconSize(QSize(30,30))
        self.em54.clicked.connect(lambda:self.sendmessage(':em54'))

        self.em55= QPushButton(self.emdock)
        self.em55.resize(30,30)
        self.em55.move(128,160)
        self.em55.setIcon(QIcon(':em55'))
        self.em55.setFlat(True)
        self.em55.setIconSize(QSize(30,30))
        self.em55.clicked.connect(lambda:self.sendmessage(':em55'))

        self.em56= QPushButton(self.emdock)
        self.em56.resize(30,30)
        self.em56.move(160,160)
        self.em56.setIcon(QIcon(':em56'))
        self.em56.setFlat(True)
        self.em56.setIconSize(QSize(30,30))
        self.em56.clicked.connect(lambda:self.sendmessage(':em56'))

        self.em57= QPushButton(self.emdock)
        self.em57.resize(30,30)
        self.em57.move(192,160)
        self.em57.setIcon(QIcon(':em57'))
        self.em57.setFlat(True)
        self.em57.setIconSize(QSize(30,30))
        self.em57.clicked.connect(lambda:self.sendmessage(':em57'))

        self.em58= QPushButton(self.emdock)
        self.em58.resize(30,30)
        self.em58.move(224,160)
        self.em58.setIcon(QIcon(':em58'))
        self.em58.setFlat(True)
        self.em58.setIconSize(QSize(30,30))
        self.em58.clicked.connect(lambda:self.sendmessage(':em58'))

        self.em59= QPushButton(self.emdock)
        self.em59.resize(30,30)
        self.em59.move(256,160)
        self.em59.setIcon(QIcon(':em59'))
        self.em59.setFlat(True)
        self.em59.setIconSize(QSize(30,30))
        self.em59.clicked.connect(lambda:self.sendmessage(':em59'))

        self.em60= QPushButton(self.emdock)
        self.em60.resize(30,30)
        self.em60.move(288,160)
        self.em60.setIcon(QIcon(':em60'))
        self.em60.setFlat(True)
        self.em60.setIconSize(QSize(30,30))
        self.em60.clicked.connect(lambda:self.sendmessage(':em60'))

        self.em61= QPushButton(self.emdock)
        self.em61.resize(30,30)
        self.em61.move(2,192)
        self.em61.setIcon(QIcon(':em61'))
        self.em61.setFlat(True)
        self.em61.setIconSize(QSize(30,30))
        self.em61.clicked.connect(lambda:self.sendmessage(':em61'))

        self.em62= QPushButton(self.emdock)
        self.em62.resize(30,30)
        self.em62.move(32,192)
        self.em62.setIcon(QIcon(':em62'))
        self.em62.setFlat(True)
        self.em62.setIconSize(QSize(30,30))
        self.em62.clicked.connect(lambda:self.sendmessage(':em62'))

        self.em63= QPushButton(self.emdock)
        self.em63.resize(30,30)
        self.em63.move(64,192)
        self.em63.setIcon(QIcon(':em63'))
        self.em63.setFlat(True)
        self.em63.setIconSize(QSize(30,30))
        self.em63.clicked.connect(lambda:self.sendmessage(':em63'))

        self.em64= QPushButton(self.emdock)
        self.em64.resize(30,30)
        self.em64.move(96,192)
        self.em64.setIcon(QIcon(':em64'))
        self.em64.setFlat(True)
        self.em64.setIconSize(QSize(30,30))
        self.em64.clicked.connect(lambda:self.sendmessage(':em64'))

        self.em65= QPushButton(self.emdock)
        self.em65.resize(30,30)
        self.em65.move(128,192)
        self.em65.setIcon(QIcon(':em65'))
        self.em65.setFlat(True)
        self.em65.setIconSize(QSize(30,30))
        self.em65.clicked.connect(lambda:self.sendmessage(':em65'))

        self.em66= QPushButton(self.emdock)
        self.em66.resize(30,30)
        self.em66.move(160,192)
        self.em66.setIcon(QIcon(':em66'))
        self.em66.setFlat(True)
        self.em66.setIconSize(QSize(30,30))
        self.em66.clicked.connect(lambda:self.sendmessage(':em66'))

        self.em67= QPushButton(self.emdock)
        self.em67.resize(30,30)
        self.em67.move(192,192)
        self.em67.setIcon(QIcon(':em67'))
        self.em67.setFlat(True)
        self.em67.setIconSize(QSize(30,30))
        self.em67.clicked.connect(lambda:self.sendmessage(':em67'))

        self.em68= QPushButton(self.emdock)
        self.em68.resize(30,30)
        self.em68.move(224,192)
        self.em68.setIcon(QIcon(':em68'))
        self.em68.setFlat(True)
        self.em68.setIconSize(QSize(30,30))
        self.em68.clicked.connect(lambda:self.sendmessage(':em68'))

        self.em69= QPushButton(self.emdock)
        self.em69.resize(30,30)
        self.em69.move(256,192)
        self.em69.setIcon(QIcon(':em69'))
        self.em69.setFlat(True)
        self.em69.setIconSize(QSize(30,30))
        self.em69.clicked.connect(lambda:self.sendmessage(':em69'))

        self.em70= QPushButton(self.emdock)
        self.em70.resize(30,30)
        self.em70.move(288,192)
        self.em70.setIcon(QIcon(':em70'))
        self.em70.setFlat(True)
        self.em70.setIconSize(QSize(30,30))
        self.em70.clicked.connect(lambda:self.sendmessage(':em70'))

        self.em71= QPushButton(self.emdock)
        self.em71.resize(30,30)
        self.em71.move(2,224)
        self.em71.setIcon(QIcon(':em71'))
        self.em71.setFlat(True)
        self.em71.setIconSize(QSize(30,30))
        self.em71.clicked.connect(lambda:self.sendmessage(':em71'))

        self.em72= QPushButton(self.emdock)
        self.em72.resize(30,30)
        self.em72.move(32,224)
        self.em72.setIcon(QIcon(':em72'))
        self.em72.setFlat(True)
        self.em72.setIconSize(QSize(30,30))
        self.em72.clicked.connect(lambda:self.sendmessage(':em72'))

        self.em73= QPushButton(self.emdock)
        self.em73.resize(30,30)
        self.em73.move(64,224)
        self.em73.setIcon(QIcon(':em73'))
        self.em73.setFlat(True)
        self.em73.setIconSize(QSize(30,30))
        self.em73.clicked.connect(lambda:self.sendmessage(':em73'))

        self.em74= QPushButton(self.emdock)
        self.em74.resize(30,30)
        self.em74.move(96,224)
        self.em74.setIcon(QIcon(':em74'))
        self.em74.setFlat(True)
        self.em74.setIconSize(QSize(30,30))
        self.em74.clicked.connect(lambda:self.sendmessage(':em74'))

        self.em75= QPushButton(self.emdock)
        self.em75.resize(30,30)
        self.em75.move(128,224)
        self.em75.setIcon(QIcon(':em75'))
        self.em75.setFlat(True)
        self.em75.setIconSize(QSize(30,30))
        self.em75.clicked.connect(lambda:self.sendmessage(':em75'))

        self.em76= QPushButton(self.emdock)
        self.em76.resize(30,30)
        self.em76.move(160,224)
        self.em76.setIcon(QIcon(':em76'))
        self.em76.setFlat(True)
        self.em76.setIconSize(QSize(30,30))
        self.em76.clicked.connect(lambda:self.sendmessage(':em76'))

        self.em77= QPushButton(self.emdock)
        self.em77.resize(30,30)
        self.em77.move(192,224)
        self.em77.setIcon(QIcon(':em77'))
        self.em77.setFlat(True)
        self.em77.setIconSize(QSize(30,30))
        self.em77.clicked.connect(lambda:self.sendmessage(':em77'))

        self.em78= QPushButton(self.emdock)
        self.em78.resize(30,30)
        self.em78.move(224,224)
        self.em78.setIcon(QIcon(':em78'))
        self.em78.setFlat(True)
        self.em78.setIconSize(QSize(30,30))
        self.em78.clicked.connect(lambda:self.sendmessage(':em78'))

        self.em79= QPushButton(self.emdock)
        self.em79.resize(30,30)
        self.em79.move(256,224)
        self.em79.setIcon(QIcon(':em79'))
        self.em79.setFlat(True)
        self.em79.setIconSize(QSize(30,30))
        self.em79.clicked.connect(lambda:self.sendmessage(':em79'))

        self.em80= QPushButton(self.emdock)
        self.em80.resize(30,30)
        self.em80.move(288,224)
        self.em80.setIcon(QIcon(':em80'))
        self.em80.setFlat(True)
        self.em80.setIconSize(QSize(30,30))
        self.em80.clicked.connect(lambda:self.sendmessage(':em80'))

        self.emdock.setVisible(False)
###----------------------------------------------menu----------------------------------------------------------------------------------
        self.medock = QWidget(self.win)
        self.medock.resize(200,45)
        self.medock.move(60,150)
        self.medock.setStyleSheet("background-color:#b1bed2;")

        self.medocklab=QPushButton('Exit',self.medock)
        self.medocklab.resize(50,25)
        self.medocklab.move(70,15)
        self.medocklab.clicked.connect(self.meexitfun)
        self.medocklab.setStyleSheet("background-color:tomato;font-size:15px;color:black;font-family:monospace;")
        self.medock.setVisible(False)
####-----------------------------------------------settings-----------------------------------------------------------------------------
        self.setdock = QWidget(self.win)
        self.setdock.resize(200,50)
        self.setdock.move(60,200)
        self.setdock.setWindowTitle('menu')
        self.setdock.setStyleSheet("background-color:#DDDDDD;font-size:17px;")
        self.setdock.setVisible(False)

        self.menubar = QMenuBar(self.setdock)
        self.menubar.move(50,0)
        self.menu = QMenu("settings")
        self.menubar.addMenu(self.menu)

        self.setname=QAction("Reset Name")
        self.chpic=QAction("Change Picture")
        self.dfpic=QAction("Default Picture")
        self.menu.addAction(self.setname)
        self.menu.addAction(self.chpic)
        self.menu.addAction(self.dfpic)

        self.setname.triggered.connect(self.setnamefun)
        self.chpic.triggered.connect(self.chpicfun)
        self.dfpic.triggered.connect(self.dfpicfun)
##-----------------------------------------------calendar widget------------------------------------------------------------------------      
        self.caldock = QWidget(self.win)
        self.caldock.resize(350,210)
        self.caldock.move(60,250)
        self.caldock.setWindowTitle('calendar')
        self.caldock.setStyleSheet("background-color:#DDDDDD;")
        
        self.calendar = QCalendarWidget(self.caldock)
        self.calendar.resize(350,210)
        self.caldock.setVisible(False)
##-----------------------------------------------note widget--------------------------------------------------------------------------------------
        self.notdock = QWidget(self.win)
        self.notdock.resize(290,200)
        self.notdock.move(60,300)
        self.notdock.setStyleSheet("background-color:#b1bed2;")
        self.notdock.setWindowTitle('notebook')

        self.menubar =QMenuBar(self.notdock)
        self.menubar.setStyleSheet("font-size:16px;")
        self.menubar.move(10,0)
        self.menubar.resize(20,20)
        self.menubar.setStyleSheet("font-size:13px;")

        self.editmenu =QMenu('Edit',self.notdock)
        self.editmenu.resize(20,20)
        self.menubar.addMenu(self.editmenu)

        self.esave=QAction("Save As",self.notdock)
        self.eopen=QAction("Open",self.notdock)
        self.eundo=QAction("Undo",self.notdock)
        self.eredo=QAction("Redo",self.notdock)
        self.ecopy=QAction("Copy",self.notdock)
        self.ecut=QAction("Cut",self.notdock)
        self.epaste=QAction("Paste",self.notdock)
        self.eexit=QAction("Exit",self.notdock)

        self.editmenu.addAction(self.eopen)
        self.editmenu.addAction(self.esave)
        self.editmenu.addAction(self.eundo)
        self.editmenu.addAction(self.eredo)
        self.editmenu.addAction(self.ecopy)
        self.editmenu.addAction(self.ecut)
        self.editmenu.addAction(self.epaste)
        self.editmenu.addAction(self.eexit)

        self.eopen.triggered.connect(self.openfun)
        self.esave.triggered.connect(self.saveasfun)
        self.eexit.triggered.connect(self.exitfun)
        self.eundo.triggered.connect(self.undofun)
        self.eredo.triggered.connect(self.redofun)
        self.ecut.triggered.connect(self.cutfun)
        self.ecopy.triggered.connect(self.copyfun)
        self.epaste.triggered.connect(self.pastefun)
        
        self.note = QTextEdit(self.notdock)
        self.note.resize(290,180)
        self.note.move(0,20)
        self.note.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.note.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.note.setStyleSheet('background-color:#EEEEEE;font-size:13px;')
        self.notdock.setVisible(False)
##----------------------------------------------common variables ---------------------------------------------------------------------------      
        self.messg=''
        self.name=''
        self.media=''
        self.image=''
        self.file=''
        self.imagetext=''
        self.flag=False
        self.emcnt=0
        self.inmesgcnt=0
        self.filecnt=0
        self.calcnt=0
        self.setcnt=0
        self.mecnt=0
        self.notcnt=0
        self.flag=False
        self.bflag=False
        self.oncnt=0
        #making list of colors
        self.cca='#FFB6C1'
        self.ccb='#2B65EC'
        self.ccc='green'
        self.ccd='tomato'
        self.cce='#6A5ACD'
        self.ccf='#E6E6FA'
        self.ccg='orange'
        self.cch='#649baa'
        self.cci='#eeb4b4'
        self.ccj='#9fb6cd'
        self.cck='#6c7189'
        self.ccls=[self.cca,self.ccb,self.ccc,self.ccd,self.cce,self.ccf,self.ccg,self.cch,self.cci,self.ccj,self.cck]
        self.win.show()
        sys.exit(app.exec())
##-----------------------------------------------------Functions-----------------------------------------------------------------------------       
    def calbtnfun(self):
        self.calcnt=self.calcnt+1
        self.medock.close()
        self.notdock.close()
        self.emdock.close()
        self.setdock.close()
        if self.calcnt%2==0:
            self.caldock.close()
        else:
            self.caldock.show()

    def notebtnfun(self):
        self.emdock.close()
        self.medock.close()
        self.caldock.close()
        self.setdock.close()
        self.notcnt=self.notcnt+1
        if self.notcnt%2==0:
            self.notdock.close()
        else:
            self.notdock.show()

    def settingbtnfun(self):
        self.medock.close()
        self.emdock.close()
        self.notdock.close()
        self.caldock.close()
        self.setdock.close()
        self.setcnt=self.setcnt+1
        if self.setcnt%2==0:
            self.setdock.close()
        else:
            self.setdock.show()

    def menubtnfun(self):
        self.emdock.close()
        self.notdock.close()
        self.caldock.close()
        self.setdock.close()
        self.mecnt=self.mecnt+1
        if self.mecnt%2==0:
            self.medock.close()
        else:
            self.medock.show()
            
    def loginfun(self):
        if self.logname.text()=='':
            self.logname.setPlaceholderText('surname is invalid....try again')
        elif len(self.logname.text())>10:
            self.logname.setText('')
            self.logname.setPlaceholderText('name must not be more than 10')
        else:    
             self.name=self.logname.text()
             self.activename.setText(self.name)
             self.loginpage.close()
             
    def textpadtch(self):
        self.emdock.close()
        self.notdock.close()
        self.caldock.close()
        self.medock.close()
        self.setdock.close()

    def sendbtnfun(self):
        self.emdock.close()
        self.notdock.close()
        self.caldock.close()
        self.medock.close()
        self.bflag = True
      
        if self.flag is True:
           self.textpad.selectAll()
           self.textpad.cut()
           clipboard=QApplication.clipboard()
           self.messg=clipboard.text()
           clipboard.clear()
           sendth= threading.Thread(target=self.sendtextmessg)
           sendth.start()
           self.sendtextmessg(self.messg)
        else:
            QMessageBox.information(self.win,'startchat','<p style="color:#fac0a2">start chat by clicking on the start</p>',QMessageBox.Ok)
                 
    def emojibtnfun(self):
        self.emcnt=self.emcnt+1
        self.medock.close()
        self.notdock.close()
        self.caldock.close()
        if self.emcnt%2==0:
            self.emdock.close()
        elif self.flag is False:
            self.emdock.close()
        else:
            self.emdock.show()        
            
    def filebtnfun(self):
        self.notdock.close()
        self.caldock.close()
        self.emdock.close()
        if self.flag is False:
            QMessageBox.information(self.win,'startchat','<p style="color:#fac0a2">start chat by clicking on the start</p>',QMessageBox.Ok)
        else:   
            self.filedialog = QFileDialog(self.win)
            self.filedialog.setAcceptMode(QFileDialog.AcceptOpen)
            self.file=self.filedialog.getOpenFileName(self.win,'Open file',"C:\\")[0]
            if str(self.file) !='':
                self.file=pathlib.Path(self.file)
                self.sendmessagex(str(self.file))
       
    def engine(self):
        self.w1 = worker1()
        self.w1.sig.connect(self.labelstyle)
        self.w1.start()
       
        self.w2 = worker2()
        self.w2.sig1.connect(self.inspirecol)
        self.w2.sig2.connect(self.inspiretex)
        self.w2.sig3.connect(self.inspirecln)
        self.w2.start()

        self.w3 = worker3()
        self.w3.sig1.connect(self.tonotice)
        self.w3.sig2.connect(self.tolistscreen)
        self.w3.sig3.connect(self.incomingmessg)
        self.w3.sig4.connect(self.incomingmessgx)
        self.w3.start()
        
        self.sendnamemessg(self.name)
        self.flag = True
        self.activelabel.setText('<center>Active</center>')
        self.onlinebtn.setEnabled(False)
###----------------------------------------------receiving data-------------------------       
    def tonotice(self,inmesg):
        self.to_do.append(inmesg)
    def tolistscreen(self,inmesg):
        self.listscreen.setText(inmesg+'\n')
    def incomingmessg(self,inmesg):
        self.chatframe.setAlignment(Qt.AlignLeft)
        self.chatframe.append(inmesg)
        self.bflag = False
    def incomingmessgx(self,inmesg):
        self.inmesgcnt=self.inmesgcnt+1
        l=self.inmesgcnt
        self.chatframe.append(f"<img src='media/image{l}.jpg' height=350 width=400><br>")
###----------------------------------------------sending data------------------------------------------    
    def sendnamemessg(self,name):
        self.name = name
        while True:
            sock.send(name.encode('utf-8'))
            break
    def sendmessagex(self,media):
        f=open(f'{media}','rb')
        while True:
            image=f.read()
            sock.send(image)
            f.close()
            break  
    def sendmessage(self,media):
        self.media = media
        while True:
            sock.send(f"<p>{self.name}</p><br><img src='{media}' height=50 width=50><br>".encode('utf-8'))
            break
    def sendtextmessg(self,messg):
        self.messg=self.messg
        while True:
            self.namecol=random.choice(self.ccls)
            self.textcol=random.choice(self.ccls)
            data=f"<table border='1' cellspacing='0.01' cellpadding='2' style='border-color:rgb(15%,15%,15%);background-color:rgb(15%,15%,15%);'><tr><td width='300'><strong><font color={self.namecol}>{self.name}</font></strong><br><strong><font color={self.textcol}>{self.messg}</font></strong></td></tr></table><br>"
            sock.send(data.encode('utf-8'))
            break
        
    def labelstyle(self,dat1,dat2,dat3,dat4,dat5,dat6,dat7):
        self.l1.setStyleSheet(dat1)
        self.l2.setStyleSheet(dat2)
        self.l3.setStyleSheet(dat3)
        self.l4.setStyleSheet(dat4)
        self.l5.setStyleSheet(dat5)
        self.l6.setStyleSheet(dat6)
        self.time.setText(dat7)
        
    def inspirecol(self,data):
        self.inspire.setStyleSheet(data)
    def inspiretex(self,data):
        self.inspire.append(data)
    def inspirecln(self,data):
        self.inspire.setText(data)
    ###--------dock widgets-----------    
    def meexitfun(self):
        sys.exit()
    def setnamefun(self):
        self.line = QLineEdit(self.setdock)
        self.line.resize(150,20)
        self.line.move(5,27)

        self.sndbtn = QPushButton(self.setdock)
        self.sndbtn.resize(30,20)
        self.sndbtn.move(160,27)
        self.sndbtn.setStyleSheet('background-color:#2B65EC;')
        self.sndbtn.clicked.connect(self.newname)
        self.sndbtn.show()
        self.line.show()
    def newname(self):
        self.name=self.line.text()
        self.activename.setText(self.name)
        self.sndbtn.close()
        self.line.close()
        self.setdock.close() 
    def chpicfun(self):
        filed = QFileDialog(self.win)
        file = filed.getOpenFileName(self.win,'Open file','C:\\',"Image file(*jpg)")[0]
        if file != '':
           file=pathlib.Path(file)
           self.pixmap=QPixmap(str(file))
           self.pixmap.scaled(1,1)
           self.profr.setPixmap(self.pixmap)
        self.setdock.close()
    def dfpicfun(self):
        self.profr.setPixmap(QPixmap(''))
        self.setdock.close()
    ##----notebook----    
    def cutfun(self):
        self.note.cut()
    def pastefun(self):
        self.note.paste()   
    def copyfun(self):
        self.note.copy()
    def undofun(self):
        self.note.undo()
    def redofun(self):
        self.note.redo()
    def exitfun(self):
        self.notdock.close()    
    def openfun(self):
        filedialog =QFileDialog(self.notdock)
        file=filedialog.getOpenFileName(self.notdock,"Opnen Text","C:\\","text(*txt)")[0]
        if str(file) != '':
           file=pathlib.Path(file)
           f=open(file,'r')
           while True:
               line=f.read()
               f.close()
               break
           self.note.append(line)
    def saveasfun(self):
        filedialog = QFileDialog(self.notdock)
        self.sfile=filedialog.getSaveFileName(self.notdock,"Save As","C:\\")[0]
        if str(self.sfile) != '':
           self.sfile=pathlib.Path(self.sfile)
           f=open(self.sfile,'w')
           while True:
               text=self.note.selectAll()
               self.note.copy()
               f.write(QApplication.clipboard().text())
               f.close()
               break         
    ##--theme--
    def theme(self):
        if self.wradio.isChecked() is True:
            self.win.setStyleSheet("background-color:#DDDDDD;")
            self.setingframe.setStyleSheet("background-color:#191970;")
            self.start.setStyleSheet("background-color:#191970;font-size:15px;color:#DDDDDD;")
            self.theml.setStyleSheet("background-color:#191970;font-size:13px;color:#DDDDDD;")
            self.bradio.setStyleSheet("background-color:#191970;color:tomato;")
            self.wradio.setStyleSheet("background-color:#191970;color:tomato;")
            self.listscreen.setStyleSheet("background-color:#AAAAAA;border-radius:2px;color:#83a8c3;font-size:17px;")
            self.activeframe.setStyleSheet("background-color:#AAAAAA;border-radius:5px;")
            self.activename.setStyleSheet("background-color:#AAAAAA;font-family:monospace,lobster;font-size:30px;font-weight:bold;")
            self.profr.setStyleSheet("background-color:#DDDDDD;border-radius:5px 5px 5px 5px;border:1px solid #191970")
            self.activeicon.setStyleSheet("background-color:#AAAAAA;font-size:30px;font-weight:bold;")
            self.chatframe.setStyleSheet("background-color:#CCCCCC;border-radius:2px;font-size:15px;color:#83a8c3;")
            self.textframe.setStyleSheet("background-color:#AAAAAA;")
            self.textpad.setStyleSheet("background-color:#AAAAAA;font-size:15px;font-family:monospace;border-radius:1px;font-weight:bold")
            self.statusframe.setStyleSheet("background-color:#AAAAAA;border-radius:5px;")
            self.time.setStyleSheet("color:Black;font-size:13px;")
            self.to_dol.setStyleSheet("background-color:#AAAAAA;color:tomato;")
            self.dailyg.setStyleSheet("background-color:#AAAAAA;color:tomato;")
            self.to_do.setStyleSheet("background-color:#DDDDDD;border-radius:5px;")
            self.inspire.setStyleSheet("background-color:#DDDDDD;border-radius:5px;")
            self.emdock.setStyleSheet("background-color:#DDDDDD;")

        if self.wradio.isChecked() is False:
            self.win.setStyleSheet("background-color:rgb(5%,5%,5%);")
            self.setingframe.setStyleSheet("background-color:rgb(10%,10%,10%);")
            self.start.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:15px;color:#DDDDDD;")
            self.theml.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:13px;color:#DDDDDD;")
            self.bradio.setStyleSheet("background-color:rgb(10%,10%,10%);color:tomato;font-size:11px;")
            self.wradio.setStyleSheet("background-color:rgb(10%,10%,10%);color:tomato;font-size:11px;")
            self.activeframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:5px 5px 5px 5px;")
            self.listscreen.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:2px;color:#83a8c3;font-size:17px;")
            self.activename.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:30px;font-weight:bold;font-family:monospace,lobster;")
            self.activeicon.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:30px;font-weight:bold")
            self.profr.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px 5px 5px 5px;border:1px solid #191970;")
            self.activelabel.setStyleSheet("background-color:#2B65EC;border-radius:20px 20px 20px 20px;font-family:monospace;font-size:15px;color:white;font-weight:bold;")
            self.chatframe.setStyleSheet("Background-color:rgb(5%,5%,5%);border-radius:2px;font-size:15px;color:#83a8c3;")
            self.activename.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:30px;font-weight:bold;font-family:monospace,lobster;color:#CCCCCC;")
            self.textframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-top-left-radius:10px;border-bottom-left-radius:10px;")
            self.textframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-top-right-radius:10px;border-bottom-right-radius:10px;")
            self.textpad.setStyleSheet("background-color:rgb(10%,10%,10%);font-size:15px;color:#DDDDDD;font-family:monospace;border-radius:1px;font-weight:bold")  
            self.statusframe.setStyleSheet("background-color:rgb(10%,10%,10%);border-radius:5px 5px 5px 5px;")
            self.timelabel.setStyleSheet("background-color:rgb(5%,5%,5%);")
            self.activeicon.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:30px;font-weight:bold")
            self.time.setStyleSheet("color:#EEEEEE;font-size:13px;")
            self.to_dol.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:11px;font-family:monospace;font-weight:bold;")
            self.to_do.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px;")
            self.inspire.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px")
            self.dailyg.setStyleSheet("background-color:rgb(10%,10%,10%);color:#DDDDDD;font-size:11px;font-family:monospace;font-weight:bold;")
            self.inspire.setStyleSheet("background-color:rgb(5%,5%,5%);border-radius:5px")
            self.emdock.setStyleSheet("background-color:rgb(5%,5%,5%);")        
##-----------------------------------------------------------------------threads---------------------------------------------------------------
class worker1(QThread):
    sig=pyqtSignal(str,str,str,str,str,str,str)
    def __init__(self):
        super().__init__()
        self.textl1="background-color:rgb(200,0,0);border-radius:8px;"
        self.textl2="background-color:rgb(225,0,225);border-radius:8px;"
        self.textl3="background-color:rgb(255,192,03);border-radius:8px;"
        self.textl4="background-color:green;border-radius:8px;"
        self.textl5="background-color:rgb(98,176,255);border-radius:8px;"
        self.textl6="background-color:rgb(255,228,225);border-radius:8px;"
        self.textor="border-radius:8px;"
        self.textnw="background-color:#83a8c3;border-radius:8px;"
    def run(self):
        while True:
            self.textdt=datetime.datetime.now().strftime('%a %b %d,%Y-%H:%M:%S')
            self.sig.emit(self.textnw,self.textor,self.textor,self.textor,self.textor,self.textor,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textnw,self.textor,self.textor,self.textor,self.textor,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textl2,self.textnw,self.textor,self.textor,self.textor,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textl2,self.textl3,self.textnw,self.textor,self.textor,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textl2,self.textl3,self.textl4,self.textnw,self.textor,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textl2,self.textl3,self.textl4,self.textl5,self.textnw,self.textdt)
            time.sleep(0.3)
            self.sig.emit(self.textl1,self.textl2,self.textl3,self.textl4,self.textl5,self.textl6,self.textdt)
            time.sleep(0.3)
            
class worker2(QThread):
    sig1=pyqtSignal(str)
    sig2=pyqtSignal(str)
    sig3=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        # motivational quotes
        self.a = " Blowing someone \nelse's candle \ndoesn't make\nyours  shine\nany brighter"
        self.b = "If you want  \nto be happy,\nthen never expect \nanything from anyone"
        self.c = "love doesn't\nneed to be perfect, \nit just need \nto be true"
        self.d = "Don't let anyone \ntell you, you \nain't beautiful"
        self.e = "Everyone is beautiful\nin his or her own\nway, God makes\nno mistakes"
        self.f = "No matter how bad \nyour life may seem,\n there are millions \nof others who have\nit ten times worse\nthan you"
        self.g = "You will never be \nbrave if you don't hurt\nyou will never learn\n if you don't\nmake mistakes\nyou will never\nbe successful if you\nare not failure"
        self.h = "No matter how poor\nyou think you are,\nif you have a family,\nyou have everything"
        self.i = "No matter what \nknocks you down in life,\nget up and keep going,\nnever give up \ngreat blessings are\nthe results of\nperseverance"
        self.j = "Our greatest glory \nis not in never\nfailling but getting\nup every time we do"
        self.k = "Never ignore a person\nwho cares for you,\nbecause oneday,\nyou'll realise you\nhave lost a diamond\nwhile you were\nbusy collecting\nstones"
        self.l = "Nothing is permanet.\ndon't stress yourself\ntoo much because,\nno matter how bad the\nsituation is,\nthings will change"
        self.m = "Sometimes, you never\nknew the value of a\nmoment until it\nbecomes a memory"
        self.n = "We complain that,\nnothing feels real \nanymore but we\ndon't give anything\ntime to become real"
        self.o = "if you spend your\ntime hoping that,\nsomeone will suffer\nthe consequences\nwhat they do to\nyour heart,\nthen you're allowing\nthem to hurt you\na second time in\nyour mind"
        self.p = "No one is too busy,\nit's just a matter\nof priority"
        self.q = "Be strong enough \nto walk away from \nwhat's hurting you and  \nbe patience enought \nto wait for the\nblessings you deserve"
        self.r = "Speak only when \nyou think your words \nare better than silence"
        self.s = "When someone walks away \nfrom you, \nit's not the end  \nof your story.\nit's the end of \ntheir part in your story"
        self.t = "love didn't hurt you.\nsomeone who doesn't \nknow to love hurt you. \ndon't confuse the two"
        self.u = "Don't ever go to where  \nyou're being tolerated.\njust go to  \nwhere you're being  \ncelebrated and appreciated."
        self.v = "Don't chase people,\nbe yourself,  \ndo your own thing\nand work hard.  \nthe right people,\nthe ones who really\nbelong in your life\nwill come to you\nand stay."
        self.w = "It's true we don't  \nknow what we've  \ngotten until we lose it  \nbut it's also true\nwe don't know what\nwe've been missing  \nuntil it arrives"
        self.x = "Don't forget God  \nwhen you get what you \nhave prayed for"
        self.y = "Everything is temporary, \ndon't get too attached, \njust flow with the moment"
        self.z = "The right one will  \nknow all your weaknesses \nand never use them \nagainst you"
        self.ab= "People who laugh  \nthe most even on  \nthe silly things  \nare actually sad  \nfrom inside"
        self.ac= "Someday someone  \nmight come into your\nlife and love you  \nthe way you've  \nalways wanted"
        self.ad= "When ever you feel  \nsad or alone,  \njust pray,  \nGod is always there  \nfor you."
        self.ae= "Sometimes, you have\nto keep your  \ngood news to yourself.\neveryone is not genuinelly\nhappy for you."
        self.af= "Nothing hurts more  \nthan being disapointed  \nby the person you  \nthought would  \nnever hurt you."
        self.ag= "Focus on what  \nyou have instead  \nof what you don't.\nOn what's right in  \nyour world insted \nof what's wrong"
        self.ah= "I never knew  \nhow strong i was  \nuntil i had to forgive  \nsomeone who wasn't sorry, \nand accept an apology  \ni never received"
        self.ai= "It was sunset that  \ntaught me that  \nbeauty sometimes\nonly last for  \na couple of moments.\nAnd it was sunrises  \nthat showed me that \nall it takes  \nis patience to  \nexperience it all  \nover again."
        self.aj= "I stand with God ,  \nno storm can  \nshake my faith."
        self.ak= "Never regret a day  \nin your life. Good days give\nyou happiness \nand bad days give  \nyou experience" 
        self.al= "I wake up everyday  \nwith a smile because  \ni have something\nto be thankful for."
        self.am= "Remember , \nonly you can change  \nyour life ."
        self.an= "Never give so much\nof ourself to people  \nwho will no do the\nsame for you."
        self.ao= "Stop being defined\nby what others  \nthink of you"
        self.ap= "Never waste your\nfeelings on people  \nwho don't value  \nyour emotion."
        self.aq= "To care for those \nwho ones cared  \nfor you is one of\nthe highest honors."
        self.ar= "Fall asleep with\nnothing but love  \nand forgiveness in  \nyour heart.\nwhats mean't for you  \nwill be for you \ntomorrow or the  \nday after."
        self.ass= "When the wrong people\nleave your life.  \nthe right things\nstart happening."
        self.at= "Stay single until \nyou meet the person\nthat will take care\nof you the most."
        self.au= "Heart is  not a basket\nfor keeping sadness  \nand tension,  \nit is a golden box \nfor keeping roses  \nof happiness and  \nsweet memories."
        self.av= "Kindness makes you\nthe most beautiful person \nin the world no \nmatter what you  \nlook like"
        self.aw= "The person who loves\n you more will   \n fight with you daily  \n without any reason"
        self.ax= "Don't worry,  \ncast all your cares  \non him for he cares  \nfor you \n1 Peter 5:7"
        self.ay= "Don't change yourself\nto win someone's heart,  \nstay true and you will  \nfind someone who likes  \nyou for being you."
        self.az= "Dear God please\nremove all the pains  \nfrom everyone's life\nand keep everyone  \nhappy"
        self.ba= "One day im going \nto have everything \ni have prayed for \ni really believe it."
        self.bb= "Everything is going\nto be ok,\nmaybe not today  \nbut eventually it will,\ntrust God.\nHold fast to your hope.\nGod never fails."
        self.bc= "I'm happy because,\nno matter what i face  \nin life , God has  \nnever left my side"
        self.bd= "If you really love \nthat person,  \nlearn to wait.  \nmaybe you're not meant\nto be together today\nbut someday."
        self.be= "If i fall in love\nwith someone, \nPlease don't tell me\ntheir past.\nI was not there.\ni love what i see now. \nIt's all that matters"
        self.bf= "The most painful  \ntears are not the one\nthat falls from your\neyes and cover your face\nbut the one that\nfalls from your\nheart and cover\nyour soul."
        self.bg= "Your storms are\nonly temporal but the\nblessings of God last  \nforever"
        self.bh= "Everything becomes\nbeautiful if you start\nloving it even\nlonelines"
        self.bi= "Things end. \nPeople change  \nand you know what?.\nlife goes on"
        self.bj= "I believe the hardest\npart of healing after\nyou've lost someone  \nis to recover the  \n'You' that went away\nwith them" 
        self.bk= "There is no limit\nto the power of loving "
        self.bl= "When you love someone,\nage, weight, height,\nand distance is just\na number"
        self.bm= "Nobody will love you\nas much as Jesus loves you"
        self.bn= "Don't waste your time\nworrying about people who\ndon't like you.\nSpend time with those\nwho accept you for whom\nyou are.\nThey are the ones\nworth keeping in your life."
        self.bo= "Save your feelings\nfor the one who cares"
        self.bp= "Let your attitude \n ttract someone,\nBecause beauty is\nnot a lifetime asset."
        self.bq= "When i had no one,\nGod was there for me."
        self.br= "Hiding your feelings \nfrom someone you love\nis like Dying alive"
        self.bs= "Move on \nSomeone better is\nwaiting for you"
        self.bt= "Never push a loyal\nperson to the point\nwhere they no\nlonger care"
        self.bu= "God's plan is always\nthe best.\nSometimes the process\nis painful and hard. \nBut don't forget\nthat when God is \nsilent, He is  \ndoing something \nfor you."
        self.bv= "There is difference\nbetween someone\nwho wants you and  \nsomeone who would do  \nanything to keep you. \nRemember that!"
        self.bw= "If you are born poor\nit's not your mistake, \nbut if you die poor, \nit's your mistake"
        self.bx= "The most precious \nthing you can give someone\nis the gift of your\ntime and attention."
        self.by= "A rich man buying\nyou something doesn't\nmean anything but\na busy man giving you\nhis time means\neverything"
        self.bz= "Just beacuse  \nyou miss someone  \ndoesn't mean you need\nthem back in your life.\nMissing is just a part\nof moving on"
        self.ca= "Just because you\nyou lost me as a\nfriend doesn't mean \nyou gained me as a\nenemy.\nI'm bigger than that\nI still wanna see\nyou eat\njust not at\nmy table\n#Tupac Shakur"
        self.cb= "If you judge a \nfish by the ability\nto climb a tree\nIt will spend it \nwhole life believing\nthat it is stupid."
        self.cc= "When one door of \nhappiness closes\nanother opens\nbut often times, we\nlook so long at\nthe close door\nand we don't know \nwhich has been \nopen for us"
        self.cd= "It takes only a\naminute to get a\ncrush on someone\nan hour to like someone\nand aday to love \nsomeone\nbut it takes\na lifetime to \nto forget someone"
        self.ce= "Whatever you have\nask for in prayer,\nbelieve that you\nhave received it,\nand it will be yours\nMark 11:24"
        self.cf= "The best revenge\nis no revenge.\nMove on.\nBe happy."
        self.cg= "And if I go and\nprepare a place\nfor you,I will\ncome again,and\nreceive you unto\nmyself;that where\nI am,there you may\nbe aslo\nJohn 14:3"
        self.ch= "Once you carry your\nown water,you will\nlearn the value of\nevery drop."
        self.ci= "It hurts but its\nokay...\nBeacause we cannot\nforce someone to\nfeel the same way\nas we feel for them."
        self.cj= "Be with someone \nwho always wants to\nknow how your days\n was"

        #making list of colors
        self.cca='#FFB6C1'
        self.ccb='#2B65EC'
        self.ccc='green'
        self.ccd='tomato'
        self.cce='#6A5ACD'
        self.ccf='#E6E6FA'
        self.ccg='orange'
        self.cch='#649baa'
        self.cci='#eeb4b4'
        self.ccj='#9fb6cd'
        self.cck='#6c7189'
        #making list
        self.motils=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.j,self.k,self.l,self.m,
                self.n,self.o,self.p,self.q,self.r,self.s,self.t,self.u,self.v,self.w,self.x,self.y,
                self.z,self.ab,self.ac,self.ad,self.ae,self.af,self.ag,self.ah,self.aj,self.ak,self.al,
                self.am,self.an,self.ao,self.ap,self.aq,self.ar,self.ass,
                self.at,self.au,self.av,self.aw,self.ax,self.ay,self.az,self.ba,self.bb,self.bc,self.bd,
                self.be,self.bf,self.bg,self.bh,self.bi,self.bj,self.bk,self.bl,self.bm,self.bn,self.bo,
                self.bp,self.bq,self.br,self.bs,self.bt,self.bu,self.bv,self.bw,self.bx,self.by,self.bz,
                self.ca,self.cb,self.cc,self.cd,self.ce,self.cf,self.cg,self.ch,self.ci,self.cj]
        self.ccls=[self.cca,self.ccb,self.ccc,self.ccd,self.cce,self.ccf,self.ccg,self.cch,self.cci,self.ccj,self.cck]
    def run(self): 
        while True:
            self.col=random.choice(self.ccls)
            self.text=random.choice(self.motils)
            
            self.sig1.emit(f"color:{self.col};font-size:17px;border-radius:1px;")
            self.sig2.emit(self.text)
            time.sleep(10)
            self.sig3.emit('')

class worker3(QThread):
    sig1=pyqtSignal(str)
    sig2=pyqtSignal(str)
    sig3=pyqtSignal(str)
    sig4=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.cnt=0
        self.messgst=''
    def run(self):
        while True:
            self.messgbytes=sock.recv(102400)
            try:
                self.messg=self.messgbytes.decode('utf-8')
                if '!!!!' in self.messg:
                    self.sig1.emit(self.messg)
                    playsound('messound.wav')
                if self.messg[0] == '⏹':    
                    self.sig2.emit(self.messg)
                if self.messg.endswith('</table><br>')or'has joined'in self.messg or':em'in self.messg or'cellspacing'in self.messg or '!!!!'in self.messg:
                    self.sig3.emit(self.messg)
                    playsound('messound.wav')
            except:
                self.cnt=self.cnt+1
                l=self.cnt
                f=open(f'media/image{l}.jpg','wb')
                while True:
                    f.write(self.messgbytes)
                    f.close()
                    self.sig4.emit('successfully..cheers williams-27-7-2021..evandy')
                    playsound('messound.wav')
                    break;
            
vero()   
