import os
from PyQt5.QtWidgets import QMessageBox
from security import encrypt, decrypt


def urlload(self):
    if os.path.isfile(r".\MainWeb.rbs"):
        f = open(r".\MainWeb.rbs", 'rb')
        data = f.read()
        data = decrypt(data)
        f.close()
        return data

    else:
        err = QMessageBox()
        err.about(self, "파일 존재 오류", "다시 실행해주세요")
        w = open(r'.\MainWeb.rbs', mode='a', encoding='utf-8')
        w.close()
        w1 = open(r'.\MainWeb.rbs', 'wb')
        txt = "https://vclock.kr/embed/time/"
        txt = encrypt(txt)
        w1.write(txt)
        w1.close()


def fileload(self, loca):
    f = open(loca, 'rb')
    data = f.read()
    try:
        data = decrypt(data)
    except KeyError:
        err = QMessageBox()
        err.about(self, "Warning", "Load Error - 암호키를 확인하세요.(only scripted in RBP)")
    f.close()
    return data

