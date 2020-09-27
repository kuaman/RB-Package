import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtWebEngineWidgets
from cryptography.fernet import Fernet
import base64
import hashlib
import webbrowser

form_Main = uic.loadUiType(r".\UI\RB_Package.ui")[0]  # 메인창 불러옴


def gotowebsite(site):
    webbrowser.open(site)


def whatweb_g(row, col):
    if row == 0:
        if col == 0:
            site = "https://google.com"
            gotowebsite(site)
        if col == 1:
            site = "https://youtube.com"
            gotowebsite(site)
    elif row == 1:
        if col == 1:
            site = "https://mail.google.com"
            gotowebsite(site)
    elif row == 2:
        if col == 1:
            site = "https://drive.google.com"
            gotowebsite(site)
    elif row == 3:
        if col == 1:
            site = "https://translate.google.com"
            gotowebsite(site)
    elif row == 4:
        if col == 1:
            site = "https://google.com/maps"
            gotowebsite(site)


def whatweb_n(row, col):
    if row == 0:
        if col == 0:
            site = "https://naver.com"
            gotowebsite(site)
        elif col == 1:
            site = "https://mail.naver.com"
            gotowebsite(site)
    elif row == 1:
        if col == 1:
            site = "https://blog.naver.com"
            gotowebsite(site)
    elif row == 2:
        if col == 1:
            site = "https://cafe.naver.com"
            gotowebsite(site)


def whatweb_d(row, col):
    if row == 0:
        if col == 0:
            site = "https://daum.net"
            gotowebsite(site)
        elif col == 1:
            site = "https://tistory.com"
            gotowebsite(site)
    elif row == 1:
        if col == 1:
            site = "https://potplayer.daum.net"
            gotowebsite(site)


def encrypt(txt):
    m = hashlib.sha256()
    m.update(
        b"v*8+DpVHD9Ny9JrJt^kG#G3n=@!8z3_GuZ%9ke*@6Xs621Yxq-buC^s-R4vqe!1Te8?TbaSVj$+AyWT332pj4s=uZ2FKdWU-@^E7A2v!@zUp")
    key = base64.urlsafe_b64encode(m.digest())
    txt = bytes(txt, 'utf-8')
    result = Fernet(key)
    return result.encrypt(txt)


def decrypt(enc):
    m = hashlib.sha256()
    m.update(
        b"v*8+DpVHD9Ny9JrJt^kG#G3n=@!8z3_GuZ%9ke*@6Xs621Yxq-buC^s-R4vqe!1Te8?TbaSVj$+AyWT332pj4s=uZ2FKdWU-@^E7A2v!@zUp")
    key = base64.urlsafe_b64encode(m.digest())
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(enc)
    return decoded_text.decode('utf-8')


class Info(QDialog):
    def __init__(self, parent):
        super(Info, self).__init__(parent)
        uic.loadUi(r".\UI\Information.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Info.png"))
        self.setWindowTitle("Information [정보]")
        self.show()


class InTBM(QDialog):
    def __init__(self, parent):
        super(InTBM, self).__init__(parent)
        uic.loadUi(r".\UI\InTBM.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Bookmark.png"))
        self.setWindowTitle("RB InTBM [인터넷 북마크]")
        self.Naver.hide()
        self.Daum.hide()
        self.Google.cellDoubleClicked.connect(whatweb_g)
        self.Naver.cellDoubleClicked.connect(whatweb_n)
        self.Daum.cellDoubleClicked.connect(whatweb_d)
        self.chk_google.stateChanged.connect(self.swhid)
        self.chk_naver.stateChanged.connect(self.swhid)
        self.chk_daum.stateChanged.connect(self.swhid)
        self.show()

    def _reset(self):
        self.Google.hide()
        self.Naver.hide()
        self.Daum.hide()

    def swhid(self):
        self._reset()
        if self.chk_google.isChecked():
            self.Google.show()
        if self.chk_naver.isChecked():
            self.Naver.show()
        if self.chk_daum.isChecked():
            self.Daum.show()


class RBBlogs(QDialog):
    def __init__(self, parent):
        super(RBBlogs, self).__init__(parent)
        uic.loadUi(r".\UI\Blogs.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Blog.png"))
        self.naver.clicked.connect(self.naverblog)
        self.tistory.clicked.connect(self.tistoryblog)
        self.setWindowTitle("RB Blogs [빨파 블로그]")
        self.show()

    def naverblog(self):
        site = "http://naver.redblue.kro.kr/"
        gotowebsite(site)

    def tistoryblog(self):
        site = "http://tistory.redblue.kro.kr"
        gotowebsite(site)


class RBMeM(QDialog):
    def __init__(self, parent):
        super(RBMeM, self).__init__(parent)
        uic.loadUi(r".\UI\MeM.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Password.png"))
        self.save.clicked.connect(self.slot1_save)
        self.setWindowTitle("RB MeM [RBS]")
        self.show()

        filename = os.path.abspath("IDPW.rbs")
        filename1 = os.path.abspath("Web.rbs")
        if filename.split(".")[-1] != "rbs":
            err = QMessageBox()
            err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .rbs file)")
            return
        f = open("Web.rbs", 'rb')
        data = f.read()
        try:
            data = decrypt(data)
        except:
            err = QMessageBox()
            err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .rbs file)")
            return
        f.close()
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(data)

        if filename1.split(".")[-1] != "rbs":
            err = QMessageBox()
            err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .rbs file)")
            return
        f1 = open("IDPW.rbs", 'rb')
        data1 = f1.read()
        try:
            data1 = decrypt(data1)
        except:
            err = QMessageBox()
            err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .rbs file)")
            return
        f1.close()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_2.setPlainText(data1)

    def slot1_save(self):
        txt = self.plainTextEdit.toPlainText()
        txt = encrypt(txt)
        f = open("Web.rbs", "wb")
        f.write(txt)
        f.close()

        txt1 = self.plainTextEdit_2.toPlainText()
        txt1 = encrypt(txt1)
        f1 = open("IDPW.rbs", "wb")
        f1.write(txt1)
        f1.close()


class Option(QDialog):
    def __init__(self, parent):
        super(Option, self).__init__(parent)  # 자식 상속
        uic.loadUi(r".\UI\Option.ui", self)  # 설정창 불러옴
        self.setWindowIcon(QIcon(r".\Icon\Setting.png"))
        self.setWindowTitle("RBP 설정")
        self.show()


class MainClass(QMainWindow, form_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(r".\Icon\Main.png"))
        self.action_Options.setShortcut("Ctrl+O")
        self.action_Informations.setShortcut("Ctrl+I")
        self.action_Options.triggered.connect(self.optionfunction)  # 설정 클릭 함수 연결
        self.action_Informations.triggered.connect(self.infofunction)
        self.MeM.clicked.connect(self.memfunction)
        self.Blogs.clicked.connect(self.blogsfunction)
        self.InTBM.clicked.connect(self.intbmfunction)
        self.IntBlock.clicked.connect(self.intmanfunction)
        self.show()

    def optionfunction(self):  # 설정창 실행 함수
        Option(self)

    def infofunction(self):
        Info(self)

    def memfunction(self):
        RBMeM(self)

    def blogsfunction(self):
        RBBlogs(self)

    def intbmfunction(self):
        InTBM(self)

    def intmanfunction(self):
        webbrowser.open("http://172.30.1.254")


if __name__ == "__main__":  # 끝 함수
    app = QApplication(sys.argv)
    ex = MainClass()
    ex.show()
    app.exec_()
