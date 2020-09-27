import sys
import webbrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import uic, QtWebEngineWidgets
from security import encrypt
from website import whatweb_g, whatweb_n, whatweb_d, gotowebsite
from rw import fileload, urlload
from config import readconfig, writeconfig

Main = uic.loadUiType(r".\UI\RB_Package.ui")[0]    # Code Start


class Option(QDialog):
    def __init__(self, parent):
        super(Option, self).__init__(parent)  # 자식 상속
        uic.loadUi(r".\UI\Option.ui", self)  # 설정창 불러옴
        self.setWindowIcon(QIcon(r".\Icon\setting.png"))
        self.setWindowTitle("RBP 설정")
        self.Option_Btn.accepted.connect(self.save)
        if urlload(self) != "https://vclock.kr/embed/time/":
            self.URL_Check.setChecked(True)
            self.URL.setEnabled(True)
            self.URL.setPlainText(urlload(self))
        self.URL_reset.clicked.connect(self.urlreset)
        self.Editor_Btn.clicked.connect(self.editorload)
        self.Editor_reset.clicked.connect(self.editorreset)
        self.Editor.setPlainText(readconfig('Option', 'editorfileaddress'))
        self.File_Btn.clicked.connect(self.filelinkload)
        self.Folder_Btn.clicked.connect(self.folderlinkload)
        self.Link_reset.clicked.connect(self.linkreset)
        self.Link.setPlainText(readconfig('Option', 'filelink'))
        self.show()

    def save(self):
        writeconfig('Option', 'editorfileaddress', self.Editor.toPlainText())
        writeconfig('Option', 'filelink', self.Link.toPlainText())
        if self.URL_Check.isChecked():
            txt = self.URL.toPlainText()
            txt = encrypt(txt)
            f = open(r".\MainWeb.rbs", "wb")
            f.write(txt)
            f.close()
        else:
            w = open(r'.\MainWeb.rbs', 'wb')
            txt = "https://vclock.kr/embed/time/"
            txt = encrypt(txt)
            w.write(txt)
            w.close()

    def urlreset(self):
        self.URL_Check.setChecked(False)
        self.URL.clear()
        self.URL.setEnabled(False)

    def editorload(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "RB Security Files(*.rbs)")
        if fname[0] == "":
            return
        self.Editor.setPlainText(fname[0])

    def editorreset(self):
        self.Editor.clear()
        writeconfig('Option', 'editorfileaddress', '')

    def filelinkload(self):
        fname1 = QFileDialog.getOpenFileName(self, "Open File", "", "All File(*)")
        if fname1[0] == "":
            return
        self.Link.clear()
        self.Link.setPlainText(fname1[0])

    def folderlinkload(self):
        fname1 = QFileDialog.getExistingDirectory(self, "Select directory")
        if fname1 == "":
            return
        self.Link.setPlainText(fname1)

    def linkreset(self):
        self.Link.clear()
        writeconfig('Option', 'filelink', '')


class Hidden(QDialog):
    def __init__(self, parent):
        super(Hidden, self).__init__(parent)
        uic.loadUi(r".\UI\Hidden.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\setting.png"))
        self.setWindowTitle("Hidden Settings [고급 설정]")
        if readconfig('Option', 'language') == 'Korean':
            self.select_lang.setCurrentIndex(1)
        elif readconfig('Option', 'language') == 'English':
            self.select_lang.setCurrentIndex(2)
        self.buttonBox.accepted.connect(self.lang)
        self.show()

    def lang(self):
        if self.select_lang.currentIndex() == 1:
            writeconfig('Option', 'language', 'Korean')
        elif self.select_lang.currentIndex() == 2:
            writeconfig('Option', 'language', 'English')


class Info(QDialog):
    def __init__(self, parent):
        super(Info, self).__init__(parent)
        uic.loadUi(r".\UI\Info.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Info.png"))
        self.setWindowTitle("Information [정보]")
        self.show()


class RBEditor(QDialog):
    def __init__(self, parent):
        super(RBEditor, self).__init__(parent)
        uic.loadUi(r".\UI\Editor.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\Password.png"))
        self.setWindowTitle("RB Editor [보안 에디터]")
        writeconfig('Option', 'editorlastfa', '')
        self.save_btn.clicked.connect(self.save)
        self.load_btn.clicked.connect(self.load)
        a = readconfig('Option', 'editorfileaddress')
        if a != "":
            data = fileload(self, a)
            self.plainTextEdit.clear()
            self.plainTextEdit.setPlainText(data)
            self.label.setText("RB Editor - " + a)
            writeconfig('Option', 'editorlastfa', a)
        self.show()

    def load(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "RB Security Files(*.rbs)")
        if fname[0] == "":
            return
        elif fname[0].split(".")[-1] != "rbs":
            err = QMessageBox()
            err.about(self, "Warning", "Load Error - 열 수 없는 파일 포맷입니다.(only .rbs file)")
            return
        data = fileload(self, fname[0])
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(data)
        self.label.setText("RB Editor - " + fname[0])
        writeconfig('Option', 'editorlastfa', fname[0])

    def save(self):
        txt = self.plainTextEdit.toPlainText()
        txt = encrypt(txt)
        a = readconfig('Option', 'editorlastfa')
        if a != "":
            f = open(a, 'wb')
        else:
            fname = QFileDialog.getSaveFileName(self, "Save File", "", "RB Security Files(*.rbs)")
            if fname[0] == "":
                return
            f = open(fname[0], "wb")
        f.write(txt)
        f.close()
        

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

    def reset(self):
        self.Google.hide()
        self.Naver.hide()
        self.Daum.hide()

    def swhid(self):
        self.reset()
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
        self.naver.clicked.connect(self.naverb)
        self.tistory.clicked.connect(self.tistoryb)
        self.github.clicked.connect(self.githubp)
        self.setWindowTitle("RB Blogs [빨파 블로그]")
        self.show()

    def naverb(self):
        site = "http://naver.redblue.kro.kr/"
        gotowebsite(site)

    def tistoryb(self):
        site = "http://tistory.redblue.kro.kr"
        gotowebsite(site)

    def githubp(self):
        site = "https://github.com/kuaman/RB-Package"
        gotowebsite(site)


class RBInTman(QDialog):
    def __init__(self, parent):
        super(RBInTman, self).__init__(parent)
        uic.loadUi(r".\UI\InTman.ui", self)
        self.setWindowIcon(QIcon(r".\Icon\InTman.png"))
        self.KT.clicked.connect(self.kt)
        self.SKT.clicked.connect(self.skt)
        self.LGUP.clicked.connect(self.lgup)
        self.show()

    def kt(self):
        webbrowser.open("http://172.30.1.254")

    def skt(self):
        webbrowser.open("http://192.168.35.1")

    def lgup(self):
        webbrowser.open("http://192.168.219.1")


class MainClass(QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(r".\Icon\Main.png"))
        self.action_Options.setShortcut("Ctrl+O")
        self.action_Hidden.setShortcut("Ctrl+H")
        self.action_Info.setShortcut("Ctrl+I")
        self.action_Options.triggered.connect(self.rboption)
        self.action_Info.triggered.connect(self.rbinfo)
        self.action_Hidden.triggered.connect(self.rbhidden)
        self.Editor.clicked.connect(self.rbeditor)
        self.InTBM.clicked.connect(self.rbintbm)
        self.Blogs.clicked.connect(self.rbblogs)
        self.Links.clicked.connect(self.rblinks)
        self.InTman.clicked.connect(self.rbintman)
        if readconfig('Option', 'language') != 'Korean':
            self.InTman.hide()
        a = urlload(self)
        if a != "https://vclock.kr/embed/time/":
            self.Maintab.setTabText(0, "사용자 지정")
        self.TimeNow.load(QUrl(a))
        self.show()

    def rboption(self):
        Option(self)

    def rbhidden(self):
        Hidden(self)

    def rbinfo(self):
        Info(self)

    def rbeditor(self):
        RBEditor(self)

    def rbintbm(self):
        InTBM(self)

    def rbblogs(self):
        RBBlogs(self)

    def rblinks(self):
        a = readconfig('Option', 'filelink')
        if a != "":
            webbrowser.open(a)
        else:
            err = QMessageBox()
            err.about(self, "Warning", "NoFileExisted - 존재하지 않는 경로입니다.(바로가기 설정 오류)")

    def rbintman(self):
        print(1)
        RBInTman(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainClass()
    ex.show()
    app.exec_()  # Code End
