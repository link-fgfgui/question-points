from PyQt5 import QtCore, QtGui, QtWidgets
import json, os, time, requests, sys, threading

if not os.path.exists('./config'):
    os.mkdir('./config')
if os.path.exists('./config/config.json'):
    with open('./config/config.json', 'r') as f:
        dic = json.load(f)
    if dic.get('password') is None:
        dic['password'] = '0'
    if dic.get('allpoint') is None:
        dic['allpoint'] = 20
    if dic.get('onepoint') is None:
        dic['onepoint'] = 10
    if dic.get('maxtell') is None:
        dic['maxtell'] = 2
    with open('./config/config.json', 'w') as f:
        json.dump(dic, f, indent=4)
else:
    with open('./config/config.json', 'w', encoding='utf-8') as f:
        dic = {"names": [], "password": ''}
        if dic.get('password') is None:
            dic['password'] = '0'
        if dic.get('allpoint') is None:
            dic['allpoint'] = 20
        if dic.get('onepoint') is None:
            dic['onepoint'] = 10
        json.dump(dic, f, indent=4)
canshu = sys.argv
if len(canshu) < 2:
    canshu.append('')
if canshu[1] == 'old':
    version = "0.9"


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


    def checkpw():
        if ui.pw_lineEdit.text() == password:
            ui.saveButton.setDisabled(False)
        else:
            ui.saveButton.setDisabled(True)


    def output():
        global out
        dic_t, dic_s, gong, nameg, alland = {}, {}, [], [], []
        for d in dic[todaytime]:
            if d['tea'] + d['stu'] in gong or d['tea'] == d['stu']:
                continue
            gong.append(d['tea'] + d['stu'])
            if d['tea'] not in nameg:
                nameg.append(d['tea'])
            if d['stu'] not in nameg:
                nameg.append(d['stu'])
            try:
                dic_t[d['tea']]
                dic_t[d['tea']] = dic_t[d['tea']] + 1
                if dic_t[d['tea']] > onepoint:
                    dic_t[d['tea']] = onepoint
            except KeyError:
                dic_t[d['tea']] = 2
            try:
                dic_s[d['stu']]
                dic_s[d['stu']] = dic_s[d['stu']] + 1
                if dic_s[d['stu']] > onepoint:
                    dic_s[d['stu']] = onepoint
            except KeyError:
                dic_s[d['stu']] = 2
        out = todaytime + '\n\n'
        for n in namelist:
            if n == '老师':
                continue
            if n not in nameg:
                continue
            if dic_t.get(n) == None:
                tea_count = 0
            else:
                tea_count = dic_t.get(n)
            if dic_s.get(n) == None:
                stu_count = 0
            else:
                stu_count = dic_s.get(n)
            if tea_count + stu_count > allpoint:
                point = allpoint
            else:
                point = tea_count + stu_count
            out = out + n + '+' + str(point) + '分\n'
        FormWindow.show()
        FormUi.textBrowser.setText(out)


    def save():
        global dic
        t = int(time.time() // 1)
        stu = namelist[ui.s_listWidget.currentIndex().row()]
        tea = namelist[ui.t_listWidget.currentIndex().row()]
        dic[todaytime].append({'time': t, 'stu': stu, 'tea': tea})
        with open('./config/config.json', 'w') as f:
            json.dump(dic, f, indent=4)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', '记录成功！')
            msg_box.exec_()


    def changehitokoto():
        while True:
            while True:
                try:
                    hitokoto_dic = requests.get('https://v1.hitokoto.cn/?c=i&c=d&encode=json&max_length=16').json()
                    if '/' in hitokoto_dic["from"]:
                        y = hitokoto_dic["from"].find('/')
                        hitokoto_dic["from"] = hitokoto_dic["from"][:y]
                        while hitokoto_dic["from"][-1] == ' ':
                            hitokoto_dic["from"] = hitokoto_dic["from"][:-2]
                    if hitokoto_dic["from"] == None:
                        hitokoto_dic["from"] = '佚名'
                    if hitokoto_dic["from_who"] == None:
                        hitokoto_dic["from"] = '佚名'
                    hitokoto = hitokoto_dic["hitokoto"] + '—' + str(hitokoto_dic["from"]) + ' ' + str(
                        hitokoto_dic["from_who"])
                    if len(hitokoto) < 20:
                        hitokoto = ('  ' * 10) + hitokoto
                    ui.hitokoto_label.setText(hitokoto)
                    ui.hitokoto_label.setToolTip(hitokoto_dic['uuid'])
                    break
                except:
                    pass
            time.sleep(150)


    def savefile():
        try:
            filePath = QtWidgets.QFileDialog.getSaveFileName(None, "请选择保存路径", './', 'txt Flies(*.txt)')[0]
            outfile = out
            outfile = outfile + '\n\n\n\n记录:\n'
            for d in dic[todaytime]:
                outfile = outfile + f"""{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(d['time']))} {d['tea']} 教 {d['stu']}\n"""
            with open(filePath, 'w') as f:
                f.write(outfile)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '信息', 'Successful')
            msg_box.exec_()
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '失败！')
            msg_box.exec_()


    if not os.path.exists('./config'):
        os.mkdir('./config')
    if not os.path.exists('./config/config.json'):
        a = QtWidgets.QApplication([])
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '没有找到配置文件！')
        msg.show()
        a.exec_()
        sys.exit()
    app = QtWidgets.QApplication([])
    with open('./config/config.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    try:
        namelist = dic['names']
        if namelist[-1] == '老师':
            del namelist[-1]
            del dic['names'][-1]
            with open('./config/config.json', 'w', encoding='utf-8') as f:
                json.dump(dic, f, indent=4)
    except:
        pass
    try:
        password = dic['password']
        todaytime = time.strftime("%Y-%m-%d", time.localtime())
    except:
        pass
    try:
        dic[todaytime]
    except KeyError:
        dic[todaytime] = []
        DialogWindow = QtWidgets.QDialog()
        DialogUi = Ui_Dialog()
        DialogUi.setupUi(DialogWindow)
        while not DialogWindow.exec() or DialogUi.pw_lineEdit.text() == '':
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '请设置密码')
            msg_box.exec_()
        password = DialogUi.pw_lineEdit.text()
        dic['password'] = password
        with open('./config/config.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f, indent=4)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.s_listWidget.addItems(namelist)
    namelist.append('老师')
    ui.t_listWidget.addItems(namelist)
    FormWindow = QtWidgets.QWidget()
    FormUi = Ui_Form()
    FormUi.setupUi(FormWindow)
    thread = threading.Thread(target=changehitokoto, daemon=True)
    thread.start()
    password = dic['password']
    allpoint = dic['allpoint']
    onepoint = dic['onepoint']
    mainWindow.show()
    app.exec_()
    sys.exit(0)
elif canshu[1] == 'debug':
    class Ui_debugForm(object):
        def setupUi(self, debugForm):
            debugForm.setObjectName("debugForm")
            debugForm.setWindowModality(QtCore.Qt.ApplicationModal)
            debugForm.resize(800, 600)
            debugForm.setMinimumSize(QtCore.QSize(800, 600))
            debugForm.setMaximumSize(QtCore.QSize(800, 600))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./config/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            debugForm.setWindowIcon(icon)
            self.tabWidget = QtWidgets.QTabWidget(debugForm)
            self.tabWidget.setGeometry(QtCore.QRect(20, 10, 761, 561))
            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.pushButton = QtWidgets.QPushButton(self.tab)
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setGeometry(QtCore.QRect(430, 210, 93, 28))
            self.label = QtWidgets.QLabel(self.tab)
            self.label.setGeometry(QtCore.QRect(140, 120, 141, 31))
            self.label.setObjectName("label")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
            self.lineEdit_2.setGeometry(QtCore.QRect(310, 130, 113, 21))
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
            self.lineEdit_3.setGeometry(QtCore.QRect(180, 200, 191, 41))
            self.lineEdit_3.setInputMask("")
            self.lineEdit_3.setPlaceholderText("New")
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.tabWidget.addTab(self.tab, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.listWidget = QtWidgets.QListWidget(self.tab_2)
            self.listWidget.setGeometry(QtCore.QRect(90, 50, 256, 411))
            self.listWidget.setObjectName("listWidget")
            self.ApushButton = QtWidgets.QPushButton(self.tab_2)
            self.ApushButton.setGeometry(QtCore.QRect(430, 150, 93, 28))
            self.ApushButton.setObjectName("ApushButton")
            self.DpushButton = QtWidgets.QPushButton(self.tab_2)
            self.DpushButton.setGeometry(QtCore.QRect(430, 300, 93, 28))
            self.DpushButton.setObjectName("DpushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit.setGeometry(QtCore.QRect(410, 70, 131, 31))
            self.tabWidget.addTab(self.tab_2, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_7.setGeometry(QtCore.QRect(120, 130, 471, 61))
            self.lineEdit_7.setObjectName("lineEdit_7")
            self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_8.setGeometry(QtCore.QRect(120, 320, 491, 61))
            self.lineEdit_8.setObjectName("lineEdit_8")
            self.label_3 = QtWidgets.QLabel(self.tab_3)
            self.label_3.setGeometry(QtCore.QRect(120, 60, 72, 15))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.tab_3)
            self.label_4.setGeometry(QtCore.QRect(120, 250, 72, 15))
            self.label_4.setObjectName("label_4")
            self.tabWidget.addTab(self.tab_3, "")
            self.pushButton.clicked.connect(sav)
            self.ApushButton.clicked.connect(add)
            self.DpushButton.clicked.connect(delll)
            self.lineEdit_7.editingFinished.connect(saapoint)
            self.lineEdit_8.editingFinished.connect(saopoint)

            self.retranslateUi(debugForm)
            self.tabWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(debugForm)

        def retranslateUi(self, debugForm):
            _translate = QtCore.QCoreApplication.translate
            debugForm.setWindowTitle(_translate("debugForm", "Debug the program"))
            self.label.setText(_translate("debugForm", "Now PassWord："))
            self.pushButton.setText(_translate("debugForm", "OK"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("debugForm", "password"))
            self.ApushButton.setText(_translate("debugForm", "Add"))
            self.DpushButton.setText(_translate("debugForm", "Del"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("debugForm", "name"))
            self.label_3.setText(_translate("debugForm", "All"))
            self.label_4.setText(_translate("debugForm", "One"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("debugForm", "value"))


    def sav():
        global dic
        dic['password'] = deui.lineEdit_3.text()
        with open('./config/config.json', 'w') as f:
            json.dump(dic, f, indent=4)


    def sa():
        with open('./config/config.json', 'w') as f:
            json.dump(dic, f, indent=4)


    def add():
        global dic, names
        dic['names'].append(deui.lineEdit.text())
        deui.listWidget.addItem(deui.lineEdit.text())
        sa()


    def delll():
        global dic, names
        xuan = deui.listWidget.currentIndex().row()
        if xuan >= 0:
            del dic['names'][xuan]
            deui.listWidget.takeItem(xuan)
            sa()


    def saapoint():
        global allpoint, dic
        try:
            num = int(deui.lineEdit_7.text())
            dic['allpoint'] = num
            allpoint = num
            sa()
        except:
            pass


    def saopoint():
        global onepoint, dic
        try:
            num = int(deui.lineEdit_8.text())
            dic['onepoint'] = num
            onepoint = num
            sa()
        except:
            pass


    debugapp = QtWidgets.QApplication([])
    deform = QtWidgets.QWidget()
    deui = Ui_debugForm()
    deui.setupUi(deform)
    password = dic['password']
    allpoint = dic['allpoint']
    onepoint = dic['onepoint']
    names = dic['names']
    deui.listWidget.addItems(names)
    deui.lineEdit_2.setText(str(password))
    deui.lineEdit_7.setText(str(allpoint))
    deui.lineEdit_8.setText(str(onepoint))
    deform.show()
    debugapp.exec_()
    sys.exit(0)
elif canshu[1] == 'setconfig':
    if os.path.exists('./setconfig.exe') and os.name == 'nt':
        os.system('start "" ./setconfig.exe')
    elif os.path.exists('./setconfig.py'):
        os.system('setconfig.py')
    sys.exit()
qmut_1, qmut_2 = QtCore.QMutex(), QtCore.QMutex()
version = "0.9.2"
waitlist, inglist = [], []


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
        self.teach_label.setGeometry(QtCore.QRect(160, 110, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.teach_label.setFont(font)
        self.teach_label.setObjectName("teach_label")
        self.stu_label = QtWidgets.QLabel(self.centralwidget)
        self.stu_label.setGeometry(QtCore.QRect(540, 110, 100, 50))
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
        self.s_listWidget.setGeometry(QtCore.QRect(540, 170, 300, 600))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s_listWidget.setFont(font)
        self.s_listWidget.setObjectName("s_listWidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(1280, 170, 200, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(990, 170, 200, 80))
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
        self.t_message_label.setText("")
        self.t_message_label.setObjectName("t_message_label")
        self.ingList = QtWidgets.QListWidget(self.centralwidget)
        self.ingList.setGeometry(QtCore.QRect(1000, 350, 280, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ingList.setFont(font)
        self.ingList.setObjectName("ingList")
        self.waitList = QtWidgets.QListWidget(self.centralwidget)
        self.waitList.setGeometry(QtCore.QRect(1000, 470, 280, 300))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.waitList.setFont(font)
        self.waitList.setObjectName("waitList")
        self.stu_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.stu_label_2.setGeometry(QtCore.QRect(900, 350, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.stu_label_2.setFont(font)
        self.stu_label_2.setObjectName("stu_label_2")
        self.stu_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.stu_label_3.setGeometry(QtCore.QRect(900, 480, 100, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.stu_label_3.setFont(font)
        self.stu_label_3.setObjectName("stu_label_3")
        self.saveButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton_2.setEnabled(True)
        self.saveButton_2.setGeometry(QtCore.QRect(1350, 370, 160, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.saveButton_2.setFont(font)
        self.saveButton_2.setObjectName("saveButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.s_listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.t_listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ingList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.waitList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 820, 72, 15))
        self.label.setObjectName("label")
        self.saveButton.clicked.connect(addtowaitlist)
        self.outputButton.clicked.connect(output)
        self.saveButton_2.clicked.connect(stopandsave)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "提问加分-v0.9.1内部测试版"))
        self.teach_label.setText(_translate("MainWindow", "教："))
        self.stu_label.setText(_translate("MainWindow", "学："))
        self.saveButton.setText(_translate("MainWindow", "排队"))
        self.outputButton.setText(_translate("MainWindow", "导出"))
        self.hitokoto_label.setText(_translate("MainWindow", "                           “一言”正在获取中······"))
        self.stu_label_2.setText(_translate("MainWindow", "ing："))
        self.stu_label_3.setText(_translate("MainWindow", "wait："))
        self.saveButton_2.setText(_translate("MainWindow", "Over"))
        self.label.setText(_translate("MainWindow", "By link"))


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


def output():
    global out
    dic_t, dic_s, gong, nameg, alland = {}, {}, [], [], []
    for d in dic[todaytime]:
        if d['tea'] == '老师':
            pass
        elif d['tea'] + d['stu'] in gong or d['tea'] == d['stu']:
            continue
        gong.append(d['tea'] + d['stu'])
        if d['tea'] not in nameg:
            nameg.append(d['tea'])
        if d['stu'] not in nameg:
            nameg.append(d['stu'])
        try:
            dic_t[d['tea']]
            dic_t[d['tea']] = dic_t[d['tea']] + 1
            if dic_t[d['tea']] > onepoint:
                dic_t[d['tea']] = onepoint
        except KeyError:
            dic_t[d['tea']] = 2
        try:
            dic_s[d['stu']]
            dic_s[d['stu']] = dic_s[d['stu']] + 1
            if dic_s[d['stu']] > onepoint:
                dic_s[d['stu']] = onepoint
        except KeyError:
            dic_s[d['stu']] = 2
    out = todaytime + '\n\n'
    for n in namelist:
        if n == '老师':
            continue
        if n not in nameg:
            continue
        if dic_t.get(n) == None:
            tea_count = 0
        else:
            tea_count = dic_t.get(n)
        if dic_s.get(n) == None:
            stu_count = 0
        else:
            stu_count = dic_s.get(n)
        if tea_count + stu_count > allpoint:
            point = allpoint
        else:
            point = tea_count + stu_count
        out = out + n + '+' + str(point) + '分\n'
    FormWindow.show()
    FormUi.textBrowser.setText(out)


def stopandsave():
    xuan = ui.ingList.currentIndex().row()
    if xuan >= 0:
        qmut_1.lock()
        dic = inglist[xuan]
        del inglist[xuan]
        ui.ingList.takeItem(xuan)
        save(dic)
        msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', '保存成功！', QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(1000 * 5)
        msgBox.exec()
        qmut_1.unlock()


def addtowaitlist():
    global waitlist, inglist
    t = int(time.time() // 1)
    stu = namelist[ui.s_listWidget.currentIndex().row()]
    if ui.t_listWidget.currentIndex().row() >= len(namelist):
        tea = '老师'
    else:
        tea = namelist[ui.t_listWidget.currentIndex().row()]
    qmut_1.lock()
    dic_wait = ({'time': t, 'stu': stu, 'tea': tea})
    waitlist.append(dic_wait)
    ui.waitList.addItem(tea + stu)
    qmut_1.unlock()


class MyObject(QtCore.QObject):
    global thread_1

    def __init__(self):
        global thread_1
        super().__init__()
        thread_1 = Thread_1()
        thread_1.start()
        thread_1._Signal.connect(self.sendmsg)

    def sendmsg(self):
        msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', tex, QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(1000 * 10)
        msgBox.exec()


class Thread_1(QtCore.QThread):
    global tex, waitlist, inglist
    _Signal = QtCore.pyqtSignal()

    def __init__(self):
        global tex
        super().__init__()

    def run(self):
        global tex, waitlist, inglist
        while True:
            if len(inglist) < 2 and len(waitlist) > 0:
                qmut_1.lock()
                dic1 = waitlist[0]
                inglist.append(dic1)
                del waitlist[0]
                ui.waitList.takeItem(0)
                ui.ingList.addItem(dic1['tea'] + dic1['stu'])
                tex = '请{}组开始讲题！'.format(dic1['tea'] + dic1['stu'])
                self._Signal.emit()
                inglist[-1]['start'] = time.perf_counter()
                qmut_1.unlock()
            for d in inglist:
                if time.perf_counter() - d['start'] >= 300:
                    qmut_1.lock()
                    tex = '请{}组回到教室！'.format(d['tea'] + d['stu'])
                    xuan = inglist.index(d)
                    inglist.remove(d)
                    ui.ingList.takeItem(xuan)
                    self._Signal.emit()
                    save(d)
                    qmut_1.unlock()
            time.sleep(0.8)


def waitforsave():
    pass


def save(d):
    global dic
    # t=int(time.time()//1)
    # stu=namelist[ui.s_listWidget.currentIndex().row()]
    # if ui.t_listWidget.currentIndex().row()>=len(namelist):
    #     tea='老师'
    # else:
    #     tea=namelist[ui.t_listWidget.currentIndex().row()]
    dic[todaytime].append(d)
    with open('./config/config.json', 'w') as f:
        json.dump(dic, f, indent=4)


class Thread_2(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            while True:
                try:
                    hitokoto_dic = requests.get('https://v1.hitokoto.cn/?c=i&encode=json&max_length=16').json()
                    if '/' in hitokoto_dic["from"]:
                        y = hitokoto_dic["from"].find('/')
                        hitokoto_dic["from"] = hitokoto_dic["from"][:y]
                        while hitokoto_dic["from"][-1] == ' ':
                            hitokoto_dic["from"] = hitokoto_dic["from"][:-2]
                    if hitokoto_dic["from"] == None:
                        hitokoto_dic["from"] = '佚名'
                    if hitokoto_dic["from_who"] == None:
                        hitokoto_dic["from"] = '佚名'
                    hitokoto = hitokoto_dic["hitokoto"] + '—《' + str(hitokoto_dic["from"]) + '》 ' + str(
                        hitokoto_dic["from_who"])
                    if len(hitokoto) < 20:
                        hitokoto = ('  ' * 10) + hitokoto
                    ui.hitokoto_label.setText(hitokoto)
                    ui.hitokoto_label.setToolTip(hitokoto_dic['uuid'])
                    break
                except:
                    pass
            time.sleep(150)


def savefile():
    try:
        filePath = QtWidgets.QFileDialog.getSaveFileName(None, "请选择保存路径", './', 'txt Flies(*.txt)')[0]
        outfile = out
        outfile = outfile + '\n\n\n\n记录:\n'
        for d in dic[todaytime]:
            outfile = outfile + f"""{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(d['time']))} {d['tea']} 教 {d['stu']}\n"""
        with open(filePath, 'w') as f:
            f.write(outfile)
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '信息', 'Successful')
        msg_box.exec_()
    except:
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '失败！')
        msg_box.exec_()


app = QtWidgets.QApplication([])
with open('./config/config.json', 'r', encoding='utf-8') as f:
    dic = json.load(f)
if dic['names'] == '老师':
    del dic['names'][-1]
    with open('./config/config.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, indent=4)
with open('./config/config.json', 'r', encoding='utf-8') as f:
    dic = json.load(f)
namelist = dic['names']
todaytime = time.strftime("%Y-%m-%d", time.localtime())
try:
    dic[todaytime]
except KeyError:
    dic[todaytime] = []
    with open('./config/config.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, indent=4)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
ui.s_listWidget.addItems(namelist)
ui.t_listWidget.addItems(namelist)
ui.t_listWidget.addItem('老师')
FormWindow = QtWidgets.QWidget()
FormUi = Ui_Form()
FormUi.setupUi(FormWindow)
password = dic['password']
allpoint = dic['allpoint']
onepoint = dic['onepoint']
thread_2 = Thread_2()
thread_2.start()
obj = MyObject()
mainWindow.show()
app.exec_()
thread_2.exit()
thread_1.exit()

if os.name == 'nt':  # UPDATE
    res = requests.get('https://link-fgfgui.github.io/question-points/update.json').json()


    def checkup(length, ver, res=requests.get('https://link-fgfgui.github.io/question-points/update.json').json()):
        for i in range(length):
            try:
                if int(res["version"][i]) > int(ver[i]):
                    return True
                elif len(ver) < len(res["version"]):
                    return True
            except:
                pass
        else:
            return False


    if checkup(5, version, res):
        url = res["url"]
        dic_up = requests.get(url).json()
        res = requests.get(dic_up['data']['url']).content
        with open(dic_up['data']['name'], 'wb') as f:
            f.write(res)
        os.system(f"""start "" ./{dic_up['data']['name']}""")
sys.exit(0)
