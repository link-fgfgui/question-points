from PyQt5 import QtCore, QtGui, QtWidgets
import json,os,time,requests,threading,sys
version=0.9
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./config/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teach_label = QtWidgets.QLabel(self.centralwidget)
        self.teach_label.setGeometry(QtCore.QRect(150, 110, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.teach_label.setFont(font)
        self.teach_label.setObjectName("teach_label")
        self.stu_label = QtWidgets.QLabel(self.centralwidget)
        self.stu_label.setGeometry(QtCore.QRect(590, 110, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.stu_label.setFont(font)
        self.stu_label.setObjectName("stu_label")
        self.t_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.t_listWidget.setGeometry(QtCore.QRect(160, 170, 300, 600))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.t_listWidget.setFont(font)
        self.t_listWidget.setObjectName("t_listWidget")
        self.s_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.s_listWidget.setGeometry(QtCore.QRect(600, 170, 300, 600))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s_listWidget.setFont(font)
        self.s_listWidget.setObjectName("s_listWidget")
        self.s_listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.t_listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(1210, 610, 200, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(1210, 210, 200, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.outputButton.setFont(font)
        self.outputButton.setObjectName("outputButton")
        self.hitokoto_label = QtWidgets.QLabel(self.centralwidget)
        self.hitokoto_label.setGeometry(QtCore.QRect(500, 20, 1091, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.hitokoto_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.hitokoto_label.setFont(font)
        self.hitokoto_label.setObjectName("hitokoto_label")
        self.t_message_label = QtWidgets.QLabel(self.centralwidget)
        self.t_message_label.setGeometry(QtCore.QRect(0, 0, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.t_message_label.setFont(font)
        self.t_message_label.setObjectName("t_message_label")
        self.pw_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pw_lineEdit.setGeometry(QtCore.QRect(335, 780, 931, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pw_lineEdit.setFont(font)
        self.pw_lineEdit.setInputMask("")
        self.pw_lineEdit.setText("")
        self.pw_lineEdit.setMaxLength(33)
        self.pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineEdit.setObjectName("pw_lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.saveButton.clicked.connect(save)
        self.outputButton.clicked.connect(output)
        self.pw_lineEdit.textChanged.connect(checkpw)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "提问加分-v0.9内部测试版"))
        self.teach_label.setText(_translate("MainWindow", "教："))
        self.stu_label.setText(_translate("MainWindow", "学："))
        self.saveButton.setText(_translate("MainWindow", "确定"))
        self.outputButton.setText(_translate("MainWindow", "导出"))
        self.hitokoto_label.setText(_translate("MainWindow", " "))
        self.t_message_label.setText(_translate("MainWindow", " "))
        self.pw_lineEdit.setPlaceholderText(_translate("MainWindow", "                          在这里输入密码"))
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./config/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 600, 400))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        # self.textBrowser.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        # self.textBrowser.setVerticalScrollBarPolicy(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 480, 200, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(savefile)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "导出&计算"))
        self.pushButton.setText(_translate("Form", "导出为文件"))
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(1000, 300)
        Dialog.setMinimumSize(QtCore.QSize(1000, 300))
        Dialog.setMaximumSize(QtCore.QSize(1000, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./config/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(24)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 251, 981, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 411, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pw_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pw_lineEdit.setGeometry(QtCore.QRect(30, 100, 931, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pw_lineEdit.setFont(font)
        self.pw_lineEdit.setText("")
        self.pw_lineEdit.setMaxLength(33)
        self.pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineEdit.setObjectName("pw_lineEdit")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置密码"))
        self.label.setText(_translate("Dialog", "请设置密码："))
class Ui_updateForm(object):
    def setupUi(self, updateForm):
        updateForm.setObjectName("updateForm")
        updateForm.resize(300, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(updateForm.sizePolicy().hasHeightForWidth())
        updateForm.setSizePolicy(sizePolicy)
        updateForm.setMinimumSize(QtCore.QSize(300, 100))
        updateForm.setMaximumSize(QtCore.QSize(300, 100))
        self.label = QtWidgets.QLabel(updateForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 18))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(updateForm)
        self.progressBar.setGeometry(QtCore.QRect(20, 50, 271, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.retranslateUi(updateForm)
        QtCore.QMetaObject.connectSlotsByName(updateForm)
    def retranslateUi(self, updateForm):
        _translate = QtCore.QCoreApplication.translate
        updateForm.setWindowTitle(_translate("updateForm", "更新"))
        self.label.setText(_translate("updateForm", "更新ing ..........."))
def checkpw():
    if ui.pw_lineEdit.text()==password:
        ui.saveButton.setDisabled(False)
    else:
        ui.saveButton.setDisabled(True)
def output():
    global out
    dic_t,dic_s,gong,nameg,alland={},{},[],[],[]
    for d in dic[todaytime]:
        if d['tea']+d['stu'] in gong or d['tea']==d['stu']:
            continue
        gong.append(d['tea']+d['stu'])
        if d['tea'] not in nameg:
            nameg.append(d['tea'])
        if d['stu'] not in nameg:
            nameg.append(d['stu'])
        try:
            dic_t[d['tea']]
            dic_t[d['tea']]=dic_t[d['tea']]+1
            if dic_t[d['tea']]>5:
                dic_t[d['tea']]=5
        except KeyError:
            dic_t[d['tea']]=2
        try:
            dic_s[d['stu']]
            dic_s[d['stu']]=dic_s[d['stu']]+1
            if dic_s[d['stu']]>5:
                dic_s[d['stu']]=5
        except KeyError:
            dic_s[d['stu']]=2
    out=todaytime+'\n\n'
    for n in namelist:
        if n == '老师':
            continue
        if n not in nameg:
            continue
        if dic_t.get(n)==None:
            tea_count=0
        else:
            tea_count=dic_t.get(n)
        if dic_s.get(n)==None:
            stu_count=0
        else:
            stu_count=dic_s.get(n)
        if tea_count+stu_count>10:
            point=10
        else:
            point=tea_count+stu_count
        out=out+n+'+'+str(point)+'分\n'
    FormWindow.show()
    FormUi.textBrowser.setText(out)
def save():
    global dic
    t=int(time.time()//1)
    stu=namelist[ui.s_listWidget.currentIndex().row()]
    tea=namelist[ui.t_listWidget.currentIndex().row()]
    dic[todaytime].append({'time':t,'stu':stu,'tea':tea})
    with open('./config/config.json','w') as f:
        json.dump(dic,f,indent=4)
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', '记录成功！')
        msg_box.exec_()
def changehitokoto():
    while True:
        while True:
            try:
                hitokoto_dic=requests.get('https://v1.hitokoto.cn/?c=i&encode=json&max_length=16').json()
                if '/' in hitokoto_dic["from"]:
                    y=hitokoto_dic["from"].find('/')
                    hitokoto_dic["from"]=hitokoto_dic["from"][:y]
                    while hitokoto_dic["from"][-1]==' ':
                        hitokoto_dic["from"]=hitokoto_dic["from"][:-2]
                hitokoto=hitokoto_dic["hitokoto"]+'—'+str(hitokoto_dic["from"])+' '+str(hitokoto_dic["from_who"])
                ui.hitokoto_label.setText(hitokoto)
                ui.hitokoto_label.setToolTip(hitokoto_dic['uuid'])
                break
            except:
                pass
        time.sleep(300)
def savefile():
    try:
        filePath=QtWidgets.QFileDialog.getSaveFileName(None,"请选择保存路径",'./','txt Flies(*.txt)')[0]
        outfile=out
        outfile=outfile+'\n\n\n\n记录:\n'
        for d in dic[todaytime]:
            outfile=outfile+f"""{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(d['time']))} {d['tea']} 教 {d['stu']}\n"""
        with open(filePath,'w') as f:
            f.write(outfile)
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '信息', 'Successful')
        msg_box.exec_()
    except:
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '失败！')
        msg_box.exec_()
if not os.path.exists('./config'):
    os.mkdir('./config')
if not os.path.exists('./config/config.json'):
    a=QtWidgets.QApplication([])
    msg=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '没有找到配置文件！')
    msg.show()
    a.exec_()
    sys.exit()
app=QtWidgets.QApplication([])
with open('./config/config.json','r',encoding='utf-8') as f:
    dic=json.load(f)
namelist=dic['names']
while namelist[-1]=='老师':
    del namelist[-1]
    del dic['names'][-1]
    with open('./config/config.json','w',encoding='utf-8') as f:
        json.dump(dic,f,indent=4)
password=dic['password']
todaytime=time.strftime("%Y-%m-%d",time.localtime())
try:
    dic[todaytime]
except KeyError:
    dic[todaytime]=[]
    DialogWindow=QtWidgets.QDialog()
    DialogUi=Ui_Dialog()
    DialogUi.setupUi(DialogWindow)
    while not DialogWindow.exec() or DialogUi.pw_lineEdit.text()=='':
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '请设置密码')
        msg_box.exec_()
    password=DialogUi.pw_lineEdit.text()
    dic['password']=password
    with open('./config/config.json','w',encoding='utf-8') as f:
        json.dump(dic,f,indent=4)
mainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(mainWindow)
ui.s_listWidget.addItems(namelist)
namelist.append('老师')
ui.t_listWidget.addItems(namelist)
FormWindow=QtWidgets.QWidget()
FormUi=Ui_Form()
FormUi.setupUi(FormWindow)
thread = threading.Thread(target=changehitokoto,daemon=True)
thread.start()
mainWindow.show()
app.exec_()
if False:
    dic_up=requests.get('http://my.new.simpost.top/upload/fgfgui/update.txt?i=2').text
    print(dic_up)
    if dic_up['version']>version:
        updateapp=QtWidgets.QApplication([])
        up_FormWindow=QtWidgets.QWidget()
        up_FormUi=Ui_updateForm()
        up_FormUi.setupUi(up_FormWindow)
        up_FormWindow.show()
        for i in range(1,10):
            up_FormUi.progressBar.setValue(i)
        url='https://tenapi.cn/lanzou/?url='+dic_up["url"]
        dic_up=requests.get(url).json()
        up_FormUi.progressBar.setValue(20)
        res=requests.get(dic_up['data']['url']).content
        up_FormUi.progressBar.setValue(50)
        with open(dic_up['data']['name'],'wb') as f:
            f.write(res)
        up_FormUi.progressBar.setValue(80)
        time.sleep(2)
        up_FormUi.progressBar.setValue(100)
        updateapp.exec_()