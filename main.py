from PyQt5 import QtCore, QtGui, QtWidgets,Qt,QtNetwork
import json, os, time, requests, sys

serverName = 'question-point'
socket = QtNetwork.QLocalSocket()
socket.connectToServer(serverName)

# 如果连接成功，表明server已经存在，当前已有实例在运行
if socket.waitForConnected(500):
    sys.exit(-1)
# 没有实例运行，创建服务器
localServer = QtNetwork.QLocalServer()
localServer.listen(serverName)


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
    if dic.get('maxtime') is None:
        dic['maxtime'] = 300
    if dic.get('mainidea') is None:
        dic['mainidea'] = 0
    if dic.get('countmode')is None:
        dic['countmode']=0
    if dic.get("onceadd")is None:
        dic["onceadd"]=1
    if dic.get("color")is None:
        dic["color"]="rgb(0,85,255);"
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
        if dic.get('maxtell') is None:
            dic['maxtell'] = 2
        if dic.get('maxtime') is None:
            dic['maxtime'] = 300
        if dic.get('mainidea') is None:
            dic['mainidea'] = 0
        if dic.get('countmode')is None:
            dic['countmode']=0
        if dic.get("onceadd")is None:
            dic["onceadd"]=1
        if dic.get("color")is None:
            dic["color"]="rgb(0,85,255);"
        json.dump(dic, f, indent=4)
canshu = sys.argv
if len(canshu) < 2:
    canshu.append('')
if canshu[1] == 'old':
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1600, 900)
            MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
            MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
            self.saveButton.setGeometry(QtCore.QRect(1210, 610, 200, 80))
            font = QtGui.QFont()
            font.setFamily("宋体")
            font.setPointSize(20)
            self.saveButton.setFont(font)
            self.saveButton.setObjectName("saveButton")
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.saveButton.clicked.connect(save)
            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "提问加分-OLD"))
            self.teach_label.setText(_translate("MainWindow", "教："))
            self.stu_label.setText(_translate("MainWindow", "学："))
            self.saveButton.setText(_translate("MainWindow", "确定"))


    def save():
        global dic
        t = int(time.time() // 1)
        stu = namelist[ui.s_listWidget.currentIndex().row()]
        if ui.t_listWidget.currentIndex().row() >= len(namelist):
            tea = '老师'
        else:
            tea = namelist[ui.t_listWidget.currentIndex().row()]
        dic[todaytime].append({'time': t, 'stu': stu, 'tea': tea})
        with open('./config/config.json', 'w') as f:
            json.dump(dic, f, indent=4)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', '记录成功！')
            msg_box.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
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
    except:
        pass
    try:
        todaytime = time.strftime("%Y-%m-%d", time.localtime())
        password = dic['password']

    except:
        pass
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
    password = dic['password']
    allpoint = dic['allpoint']
    onepoint = dic['onepoint']
    mainWindow.show()
    app.exec_()
    sys.exit(0)
elif canshu[1] == 'debug':
    class Ui_debugForm(QtWidgets.QWidget):
        def __init__(self):
            super(Ui_debugForm, self).__init__()
            self.setupUi(self)
            with open('./config/config.json', 'r') as f:
                self.dic = json.load(f)
            self.password = self.dic['password']
            self.allpoint = self.dic['allpoint']
            self.onepoint = self.dic['onepoint']
            self.maxtell = self.dic['maxtell']
            self.maxtime = self.dic['maxtime']
            self.mainidea = self.dic['mainidea']
            self.countmode = self.dic['countmode']
            self.onceadd = self.dic['onceadd']
            self.names = self.dic['names']
            self.color=self.dic['color']
            self.colorlistname=["默认蓝","汉白玉","河豚灰","春梅红","石蕊红","卵石紫","尼罗蓝","竹绿","薄荷绿","香蕉黄","玫瑰粉","极光红","胭脂红","玫瑰灰"]
            self.colorlistrgb=["rgb(0,85,255);","rgb(248,244,237)","rgb(57,55,51)","rgb(241,147,156);","rgb(240,201,207);","rgb(48,22,28);","rgb(36,116,181);","rgb(27,167,132);","rgb(32,127,76);","rgb(228,191,17);","rgb(248,179,127);","rgb(243,59 31);","rgb(240,63,36);","rgb(175,46 43);"]
            try:
                self.xuan=self.colorlistrgb.index(self.color)
            except ValueError:
                self.xuan=0
            self.comboBox_3.addItems(self.colorlistname)
            self.comboBox_3.setCurrentIndex(self.xuan)
            self.comboBox.setCurrentIndex(self.mainidea)
            if int(self.countmode)==0:
                self.comboBox_2.setCurrentIndex(1)
            elif int(self.countmode)==1:
                self.comboBox_2.setCurrentIndex(0)
            self.listWidget.addItems(self.names)
            self.lineEdit_2.setText(str(self.password))
            self.lineEdit_7.setText(str(self.allpoint))
            self.lineEdit_8.setText(str(self.onepoint))
            self.lineEdit_9.setText(str(self.maxtime))
            self.lineEdit_10.setText(str(self.onceadd))
            self.lineEdit_11.setText(str(self.maxtell))
            self.show()

        def sav(self):
            self.dic['password'] = self.lineEdit_3.text()
            with open('./config/config.json', 'w') as f:
                json.dump(self.dic, f, indent=4)

        def sa(self):
            with open('./config/config.json', 'w') as f:
                json.dump(self.dic, f, indent=4)

        def add(self):
            self.dic['names'].append(self.lineEdit.text())
            self.listWidget.addItem(self.lineEdit.text())
            self.sa()

        def delll(self):
            xuan = self.listWidget.currentIndex().row()
            if xuan >= 0:
                del self.dic['names'][xuan]
                self.listWidget.takeItem(xuan)
                self.sa()

        def saapoint(self):
            try:
                num = int(self.lineEdit_7.text())
                self.dic['allpoint'] = num
                self.allpoint = num
                self.sa()
            except:
                pass

        def sac(self):
            xuan=self.comboBox_2.currentIndex()
            if xuan==0:
                self.dic["countmode"]="1"
            elif xuan==1:
                self.dic['countmode']="0"
            self.sa()

        def samti(self):
            try:
                num = int(self.lineEdit_9.text())
                self.dic['maxtime'] = num
                self.maxtime = num
                self.sa()
            except:
                pass

        def samte(self):
            try:
                num = int(self.lineEdit_11.text())
                self.dic['maxtell'] = num
                self.maxtell = num
                self.sa()
            except:
                pass

        def sacolor(self):
            xuan=self.comboBox_3.currentIndex()
            self.dic['color']=self.colorlistrgb[xuan]
            self.sa()

        def saoa(self):
            try:
                num = int(self.lineEdit_10.text())
                self.dic['onceadd'] = num
                self.onceadd = num
                self.sa()
            except:
                pass

        def sai(self):
            xuan=self.comboBox.currentIndex()
            self.dic["mainidea"]=xuan
            self.sa()

        def saopoint(self):
            try:
                num = int(self.lineEdit_8.text())
                self.dic['onepoint'] = num
                self.onepoint = num
                self.sa()
            except:
                pass

        def setupUi(self, debugForm):
            debugForm.setObjectName("debugForm")
            debugForm.setWindowModality(QtCore.Qt.ApplicationModal)
            debugForm.resize(800, 600)
            debugForm.setMinimumSize(QtCore.QSize(800, 600))
            debugForm.setMaximumSize(QtCore.QSize(800, 600))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            debugForm.setWindowIcon(icon)
            self.tabWidget = QtWidgets.QTabWidget(debugForm)
            self.tabWidget.setGeometry(QtCore.QRect(20, 10, 761, 561))
            self.tabWidget.setObjectName("tabWidget")
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
            self.lineEdit.setGeometry(QtCore.QRect(410, 70, 171, 31))
            self.lineEdit.setObjectName("lineEdit")
            self.tabWidget.addTab(self.tab_2, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_7.setGeometry(QtCore.QRect(120, 90, 221, 31))
            self.lineEdit_7.setObjectName("lineEdit_7")
            self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_8.setGeometry(QtCore.QRect(390, 90, 211, 31))
            self.lineEdit_8.setObjectName("lineEdit_8")
            self.label_3 = QtWidgets.QLabel(self.tab_3)
            self.label_3.setGeometry(QtCore.QRect(120, 60, 121, 16))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.tab_3)
            self.label_4.setGeometry(QtCore.QRect(390, 60, 111, 16))
            self.label_4.setObjectName("label_4")
            self.comboBox = QtWidgets.QComboBox(self.tab_3)
            self.comboBox.setGeometry(QtCore.QRect(120, 180, 131, 22))
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.label_2 = QtWidgets.QLabel(self.tab_3)
            self.label_2.setGeometry(QtCore.QRect(120, 140, 101, 16))
            self.label_2.setObjectName("label_2")
            self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
            self.comboBox_2.setGeometry(QtCore.QRect(390, 180, 271, 22))
            self.comboBox_2.setObjectName("comboBox_2")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.label_5 = QtWidgets.QLabel(self.tab_3)
            self.label_5.setGeometry(QtCore.QRect(390, 140, 101, 16))
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.tab_3)
            self.label_6.setGeometry(QtCore.QRect(120, 220, 121, 16))
            self.label_6.setObjectName("label_6")
            self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_9.setGeometry(QtCore.QRect(120, 250, 221, 31))
            self.lineEdit_9.setObjectName("lineEdit_9")
            self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_10.setGeometry(QtCore.QRect(390, 250, 221, 31))
            self.lineEdit_10.setText("")
            self.lineEdit_10.setObjectName("lineEdit_10")
            self.label_7 = QtWidgets.QLabel(self.tab_3)
            self.label_7.setGeometry(QtCore.QRect(390, 220, 151, 16))
            self.label_7.setObjectName("label_7")
            self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
            self.comboBox_3.setObjectName(u"comboBox_3")
            self.comboBox_3.setGeometry(QtCore.QRect(390, 350, 131, 22))
            self.label_10 = QtWidgets.QLabel(self.tab_3)
            self.label_10.setObjectName(u"label_10")
            self.label_10.setGeometry(QtCore.QRect(390, 310, 101, 16))
            self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
            self.lineEdit_11.setObjectName("lineEdit_11")
            self.lineEdit_11.setGeometry(QtCore.QRect(120, 340, 221, 31))
            self.label_9 = QtWidgets.QLabel(self.tab_3)
            self.label_9.setObjectName("label_9")
            self.label_9.setGeometry(QtCore.QRect(120, 310, 221, 16))
            self.tabWidget.addTab(self.tab_3, "")
            self.tab_4 = QtWidgets.QWidget()
            self.tab_4.setObjectName("tab_4")
            self.label_8 = QtWidgets.QLabel(self.tab_4)
            self.label_8.setGeometry(QtCore.QRect(30, 20, 301, 16))
            self.label_8.setObjectName("label_8")
            self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
            self.lineEdit_4.setGeometry(QtCore.QRect(290, 20, 261, 21))
            self.lineEdit_4.setReadOnly(True)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.frame = QtWidgets.QFrame(self.tab_4)
            self.frame.setEnabled(False)
            self.frame.setGeometry(QtCore.QRect(40, 50, 691, 441))
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.treeWidget = QtWidgets.QTreeWidget(self.frame)
            self.treeWidget.setGeometry(QtCore.QRect(20, 10, 256, 401))
            self.treeWidget.setObjectName("treeWidget")
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            self.tabWidget.addTab(self.tab_4, "")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
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
            self.pushButton = QtWidgets.QPushButton(self.tab)
            self.pushButton.setGeometry(QtCore.QRect(430, 210, 93, 28))
            self.pushButton.setObjectName("pushButton")
            self.tabWidget.addTab(self.tab, "")
            self.pushButton.clicked.connect(self.sav)
            self.ApushButton.clicked.connect(self.add)
            self.DpushButton.clicked.connect(self.delll)
            self.lineEdit_7.editingFinished.connect(self.saapoint)
            self.lineEdit_8.editingFinished.connect(self.saopoint)
            self.lineEdit_9.editingFinished.connect(self.samti)
            self.lineEdit_10.editingFinished.connect(self.saoa)
            self.lineEdit_11.editingFinished.connect(self.samte)
            self.comboBox.currentIndexChanged.connect(self.sai)
            self.comboBox_2.currentIndexChanged.connect(self.sac)
            self.comboBox_3.currentIndexChanged.connect(self.sacolor)

            self.retranslateUi(debugForm)
            self.tabWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(debugForm)

        def retranslateUi(self, debugForm):
            _translate = QtCore.QCoreApplication.translate
            debugForm.setWindowTitle(_translate("debugForm", "调试/设置"))
            self.ApushButton.setText(_translate("debugForm", "加"))
            self.DpushButton.setText(_translate("debugForm", "删"))
            self.lineEdit.setPlaceholderText(_translate("debugForm", "输入你要加入的名字"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("debugForm", "名字"))
            self.label_3.setText(_translate("debugForm", "加分总上限"))
            self.label_4.setText(_translate("debugForm", "单方面上限"))
            self.comboBox.setItemText(0, _translate("debugForm", "白"))
            self.comboBox.setItemText(1, _translate("debugForm", "黑"))
            self.label_2.setText(_translate("debugForm", "主题色选择"))
            self.comboBox_2.setItemText(0, _translate("debugForm", "1次1单位分"))
            self.comboBox_2.setItemText(1, _translate("debugForm", "首次加2倍分，之后“1次1单位分”"))
            self.label_5.setText(_translate("debugForm", "计算方式"))
            self.label_6.setText(_translate("debugForm", "上限时间"))
            self.label_7.setText(_translate("debugForm", "“1单位分”的数量"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("debugForm", "参数"))
            self.label_8.setText(_translate("debugForm", "请输入管理员密码：（见README.md)"))
            self.lineEdit_4.setText(_translate("debugForm", "敬请期待"))
            self.treeWidget.headerItem().setText(0, _translate("debugForm", "敬请期待"))
            self.label_9.setText(_translate("debugForm","最多几组同学同时讲题"))
            self.label_10.setText(_translate('debugForm',"主题色选择"))
            __sortingEnabled = self.treeWidget.isSortingEnabled()
            self.treeWidget.setSortingEnabled(False)
            self.treeWidget.topLevelItem(0).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(1).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(2).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("debugForm", "敬请期待"))
            self.treeWidget.setSortingEnabled(__sortingEnabled)
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("debugForm", "管理记录"))
            self.label.setText(_translate("debugForm", "Now PassWord："))
            self.pushButton.setText(_translate("debugForm", "OK"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("debugForm", "密码（废弃）"))

    debugapp = QtWidgets.QApplication([])
    deui = Ui_debugForm()
    debugapp.exec_()
    sys.exit(0)
elif canshu[1] == 'setconfig':
    if os.path.exists('./setconfig.exe') and os.name == 'nt':
        os.system('start "" ./setconfig.exe')
    elif os.path.exists('./setconfig.py'):
        os.system('setconfig.py')
    sys.exit()
qmut_1, qmut_2 = QtCore.QMutex(), QtCore.QMutex()
version = "0.9.3"
waitlist, inglist = [], []


class Ui_Form_floatlabel(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form_floatlabel, self).__init__()
        self.color=dic['color']
        self.anim=None
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1313, 261)
        Form.setWindowOpacity(0.7)
        Form.setGeometry(800, 10, 1313, 261)
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 261))
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet('color:'+self.color)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                           “一言”正在获取中······"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))



class Ui_Form_float(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form_float, self).__init__()
        self.setupUi(self)
        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.anim=None
        self.m_flag=False
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 150)
        Form.setMinimumSize(QtCore.QSize(150, 150))
        Form.setMaximumSize(QtCore.QSize(150, 150))
        Form.setGeometry(1700,850,150,150)
        Form.setWindowOpacity(0.7)
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 116, 116))
        self.pushButton.setMinimumSize(QtCore.QSize(116, 116))
        self.pushButton.setMaximumSize(QtCore.QSize(116, 116))
        self.pushButton.setStyleSheet("QPushButton{image: url(./config/question.png);border-radius: 57px;background-color: rgb(255, 255, 255);}QPushButton:hover {background-color: rgb(139, 139, 139);}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(showui)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__()

        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.anim = None
        self.color=dic['color']
        self.setupUi(self)
        self.show()

    def setupUi(self, MainWindow):
        QtGui.QFontDatabase.addApplicationFont("./config/zh-cn.ttf")
        font20 = QtGui.QFont()
        font20.setFamily("汉仪文黑-85W")
        font20.setPointSize(20)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        MainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teach_label = QtWidgets.QLabel(self.centralwidget)
        self.teach_label.setGeometry(QtCore.QRect(160, 110, 100, 50))
        self.teach_label.setFont(font20)
        self.teach_label.setObjectName("teach_label")
        self.stu_label = QtWidgets.QLabel(self.centralwidget)
        self.stu_label.setGeometry(QtCore.QRect(540, 110, 100, 50))
        self.stu_label.setFont(font20)
        self.stu_label.setObjectName("stu_label")
        self.t_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.t_listWidget.setGeometry(QtCore.QRect(160, 170, 300, 600))
        self.t_listWidget.setFont(font20)
        self.t_listWidget.setObjectName("t_listWidget")
        self.s_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.s_listWidget.setGeometry(QtCore.QRect(540, 170, 300, 600))
        self.s_listWidget.setFont(font20)
        self.s_listWidget.setObjectName("s_listWidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(1280, 170, 200, 80))
        self.saveButton.setFont(font20)
        self.saveButton.setStyleSheet("QPushButton{border-radius: 20px;}QPushButton:hover {background-color: rgb(64, 230, 255);}QPushButton:disabled {background-color:rgb(189, 189, 189);}")
        self.saveButton.setObjectName("saveButton")
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(990, 170, 200, 80))
        self.outputButton.setFont(font20)
        self.outputButton.setStyleSheet("QPushButton{border-radius: 20px;}QPushButton:hover {background-color: rgb(64, 230, 255);}QPushButton:disabled {background-color:rgb(189, 189, 189);}")
        self.outputButton.setObjectName("outputButton")
        self.hitokoto_label = QtWidgets.QLabel(self.centralwidget)
        self.hitokoto_label.setGeometry(QtCore.QRect(400, 50, 1091, 50))
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.hitokoto_label.setFont(font)
        self.hitokoto_label.setObjectName("hitokoto_label")
        self.hitokoto_label.setStyleSheet('color:'+self.color)
        self.t_message_label = QtWidgets.QLabel(self.centralwidget)
        self.t_message_label.setGeometry(QtCore.QRect(0, 0, 100, 50))
        self.t_message_label.setFont(font20)
        self.t_message_label.setText("")
        self.t_message_label.setObjectName("t_message_label")
        self.ingList = QtWidgets.QListWidget(self.centralwidget)
        self.ingList.setGeometry(QtCore.QRect(1000, 350, 280, 100))
        self.ingList.setFont(font20)
        self.ingList.setObjectName("ingList")
        self.waitList = QtWidgets.QListWidget(self.centralwidget)
        self.waitList.setGeometry(QtCore.QRect(1000, 470, 280, 300))
        self.waitList.setFont(font20)
        self.waitList.setObjectName("waitList")
        self.stu_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.stu_label_2.setGeometry(QtCore.QRect(860, 350, 120, 50))
        self.stu_label_2.setFont(font20)
        self.stu_label_2.setObjectName("stu_label_2")
        self.stu_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.stu_label_3.setGeometry(QtCore.QRect(860, 480, 120, 50))
        self.stu_label_3.setFont(font20)
        self.stu_label_3.setObjectName("stu_label_3")
        self.saveButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton_2.setEnabled(True)
        self.saveButton_2.setGeometry(QtCore.QRect(1350, 370, 160, 71))
        self.saveButton_2.setFont(font20)
        self.saveButton_2.setStyleSheet("QPushButton{border-radius: 20px;}QPushButton:hover {background-color: rgb(64, 230, 255);}QPushButton:disabled {background-color:rgb(189, 189, 189);}")
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
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 820, 72, 15))
        self.label2.setObjectName("label")
        self.saveButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton_3.setEnabled(True)
        self.saveButton_3.setGeometry(QtCore.QRect(1350, 500, 160, 71))
        self.saveButton_3.setFont(font20)
        self.saveButton_3.setStyleSheet("QPushButton{border-radius: 20px;}QPushButton:hover {background-color: rgb(64, 230, 255);}QPushButton:disabled {background-color:rgb(189, 189, 189);}")
        self.saveButton_3.setObjectName("saveButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.saveButton.clicked.connect(addtowaitlist)
        self.outputButton.clicked.connect(output)
        self.saveButton_2.clicked.connect(stopandsave)
        self.saveButton_3.clicked.connect(juststop)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 1601, 51))
        self.frame.setStyleSheet(".QFrame{background-color: rgb(0, 170, 255);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(1550, 0, 50, 50))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet(".QPushButton{image: url(./config/close.ico);border-radius: 25px;}QPushButton:hover {background-color: rgb(255, 0, 0);}")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.minButton = QtWidgets.QPushButton(self.frame)
        self.minButton.setGeometry(QtCore.QRect(1440, 0, 81, 50))
        self.minButton.setStyleSheet("QPushButton{image: url(./config/min.ico);border-radius: 25px;}QPushButton:hover {background-color: rgb(0, 0, 255);}")
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.stopcheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.stopcheckbox.setObjectName(u"stopcheckbox")
        self.stopcheckbox.setEnabled(True)
        self.stopcheckbox.setGeometry(QtCore.QRect(1370, 710, 160, 71))
        self.stopcheckbox.setFont(font20)
        self.stopcheckbox.setCheckable(True)
        self.stopcheckbox.setAutoRepeat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.closeButton.clicked.connect(self.close)
        self.minButton.clicked.connect(minwindow)
        self.stopcheckbox.stateChanged.connect(wait)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "提问加分-v0.9.3内部测试版"))
        self.teach_label.setText(_translate("MainWindow", "教："))
        self.stu_label.setText(_translate("MainWindow", "学："))
        self.saveButton.setText(_translate("MainWindow", "排队"))
        self.outputButton.setText(_translate("MainWindow", "导出"))
        self.hitokoto_label.setText(_translate("MainWindow", "                           “一言”正在获取中······"))
        self.stu_label_2.setText(_translate("MainWindow", "讲题中："))
        self.stu_label_3.setText(_translate("MainWindow", "排队中："))
        self.saveButton_2.setText(_translate("MainWindow", "讲完了"))
        self.label2.setText(_translate("MainWindow", "By link"))
        self.label.setText(_translate("MainWindow", "提问加分-v0.9.3内部测试版"))
        self.saveButton_3.setText(_translate("MainWindow", "点错了"))
        self.stopcheckbox.setText(_translate("MainWindow","暂停"))

    def closeEvent(self, event):
        if self.anim is None:
            self.anim = QtCore.QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
            self.anim.setDuration(150)  # 设置动画时长
            self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
            self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
            self.anim.finished.connect(self.hide)  # 动画结束时，关闭窗口
            self.anim.start()  # 开始动画
            event.ignore()  # 忽略事件

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton :
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            if self.m_Position.y()<51:
                event.accept()
                self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            if self.m_Position.y()<51:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./config/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 600, 400))
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        # self.textBrowser.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        # self.textBrowser.setVerticalScrollBarPolicy(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 480, 200, 80))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(750, 0, 50, 50))
        self.pushButton_2.setStyleSheet(".QPushButton{image: url(./config/close.ico);border-radius: 25px;}QPushButton:hover {background-color: rgb(139, 139, 139);}")
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(savefile)
        self.pushButton_2.clicked.connect(lambda:FormWindow.close())
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


waitcode,waittime=False,0.0
def wait():
    global waitcode,waittime,temptime
    if waitcode==True:
        ui.saveButton.setDisabled(not waitcode)
        ui.saveButton_2.setDisabled(not waitcode)
        ui.saveButton_3.setDisabled(not waitcode)
        ui.outputButton.setDisabled(not waitcode)
        waitcode=False
        waittime=time.perf_counter()-temptime

    elif waitcode==False:
        ui.saveButton.setDisabled(not waitcode)
        ui.saveButton_2.setDisabled(not waitcode)
        ui.saveButton_3.setDisabled(not waitcode)
        ui.outputButton.setDisabled(not waitcode)
        waitcode=True
        temptime=time.perf_counter()-waittime




def output():
    global out
    dic_t, dic_s, gong, nameg, alland = {}, {}, [], [], []
    if countmode =="0":
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
                dic_t[d['tea']] = dic_t[d['tea']] + onceadd
                if dic_t[d['tea']] > onepoint:
                    dic_t[d['tea']] = onepoint
            except KeyError:
                dic_t[d['tea']] = 2*onceadd
            try:
                dic_s[d['stu']]
                dic_s[d['stu']] = dic_s[d['stu']] + onceadd
                if dic_s[d['stu']] > onepoint:
                    dic_s[d['stu']] = onepoint
            except KeyError:
                dic_s[d['stu']] = 2*onceadd
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
        if countmode=='1':
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
                    dic_t[d['tea']] = dic_t[d['tea']] + onceadd
                    if dic_t[d['tea']] > onepoint:
                        dic_t[d['tea']] = onepoint
                except KeyError:
                    dic_t[d['tea']] = onceadd
                try:
                    dic_s[d['stu']]
                    dic_s[d['stu']] = dic_s[d['stu']] + onceadd
                    if dic_s[d['stu']] > onepoint:
                        dic_s[d['stu']] = onepoint
                except KeyError:
                    dic_s[d['stu']] = onceadd
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


def juststop():
    xuan = ui.waitList.currentIndex().row()
    if xuan >= 0:
        qmut_1.lock()
        dic = waitlist[xuan]
        del waitlist[xuan]
        ui.waitList.takeItem(xuan)
        qmut_1.unlock()


def minwindow():
    fForm.show()
    flForm.show()
    ui.hide()


def showui():
    ui.show()
    flForm.hide()
    fForm.hide()


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
        msgBox.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        msgBox.exec_()
        qmut_1.unlock()


def update():
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


def addtowaitlist():
    global waitlist, inglist
    t = int(time.time() // 1)
    stu = namelist[ui.s_listWidget.currentIndex().row()]
    if ui.t_listWidget.currentIndex().row() >= len(namelist):
        tea = '老师'
        qmut_1.lock()
        dic_wait = ({'time': t, 'stu': stu, 'tea': tea})
        save(dic_wait)
        msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', '保存成功！', QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(1000 * 5)
        msgBox.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        msgBox.exec_()
        qmut_1.unlock()
    else:
        tea = namelist[ui.t_listWidget.currentIndex().row()]
        qmut_1.lock()
        dic_wait = ({'time': t, 'stu': stu, 'tea': tea})
        waitlist.append(dic_wait)
        ui.waitList.addItem(tea + stu)
        qmut_1.unlock()


class MyObject(QtCore.QObject):
    global thread_1,waittime

    def __init__(self):
        global thread_1, ci
        super().__init__()
        ci = 1
        thread_1 = Thread_1()
        thread_1.start()
        thread_1._Signal.connect(self.sendmsg)

    def sendmsg(self):
        global ci
        if ci == 1:
            ci = 2
            msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', tex, QtWidgets.QMessageBox.Ok)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
            msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(1000 * 15)
            msgBox.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
            msgBox.exec_()
        else:
            ci = 1
            msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, '提示', tex, QtWidgets.QMessageBox.Ok)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)
            msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(1000 * 10)
            msgBox.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
            msgBox.exec_()


class Thread_1(QtCore.QThread):
    global tex, waitlist, inglist
    _Signal = QtCore.pyqtSignal()

    def __init__(self):
        global tex
        super().__init__()

    def run(self):
        global tex, waitlist, inglist
        while True:
            if ui.isHidden() and fForm.isHidden():
                update()
                sys.exit(0)
            if len(inglist) < maxtell and len(waitlist) > 0:
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
                if (time.perf_counter() - d['start'] - waittime >= maxtime) and (not waitcode):
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
                        hitokoto_dic["from_who"] = '佚名'
                    hitokoto = hitokoto_dic["hitokoto"] + '—《' + str(hitokoto_dic["from"]) + '》 ' + str(
                        hitokoto_dic["from_who"])
                    if len(hitokoto) < 20:
                        hitokoto = ('  ' * 10) + hitokoto
                    ui.hitokoto_label.setText(hitokoto)
                    ui.hitokoto_label.setToolTip(hitokoto_dic['uuid'])
                    flForm.label.setText(hitokoto)
                    flForm.label.setToolTip(hitokoto_dic['uuid'])
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
        msg_box.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        msg_box.exec_()
    except:
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '失败！')
        msg_box.setWindowFlags(Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        msg_box.exec_()


def getmainpalette():
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
    return palette


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
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
ui.s_listWidget.addItems(namelist)
ui.t_listWidget.addItems(namelist)
ui.t_listWidget.addItem('老师')
FormWindow = QtWidgets.QWidget()
FormUi = Ui_Form()
FormUi.setupUi(FormWindow)
fForm=Ui_Form_float()
flForm=Ui_Form_floatlabel()
password = dic['password']
allpoint = dic['allpoint']
onepoint = dic['onepoint']
maxtell = dic['maxtell']
maxtime = dic['maxtime']
mainidea = dic['mainidea']
countmode=dic['countmode']
onceadd=dic['onceadd']
Palette = getmainpalette()
if mainidea == 1:
    ui.setPalette(Palette)
    FormWindow.setPalette(Palette)
    ui.saveButton.setStyleSheet("QPushButton{color:white;border-radius: 20px;background-color: black;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.saveButton_2.setStyleSheet("QPushButton{color:white;border-radius: 20px;background-color: black;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.saveButton_3.setStyleSheet("QPushButton{color:white;border-radius: 20px;background-color: black;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.outputButton.setStyleSheet("QPushButton{color:white;border-radius: 20px;background-color: black;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
else:
    ui.saveButton.setStyleSheet("QPushButton{color:black;border-radius: 20px;background-color: white;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.saveButton_2.setStyleSheet("QPushButton{color:black;border-radius: 20px;background-color: white;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.saveButton_3.setStyleSheet("QPushButton{color:black;border-radius: 20px;background-color: white;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")
    ui.outputButton.setStyleSheet("QPushButton{color:black;border-radius: 20px;background-color: white;border:5px solid yellow;}QPushButton:hover {background-color: rgb(64, 230, 255);}")

thread_2 = Thread_2()
thread_2.start()
obj = MyObject()
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
