import os
from PyQt5.QtWidgets import QMessageBox
from security import encrypt, decrypt


def Urlload(self):
    if os.path.isfile(r".\MainWeb.rbs"):
        f = open(r".\MainWeb.rbs", 'rb')
        data = f.read()
        data = decrypt(data)
        f.close()
        print(data)
        return data

    else:
        err = QMessageBox()
        err.about(self, "파일 존재 오류", "다시 실행해주세요")
        W = open(r'.\MainWeb.rbs', mode='a', encoding='utf-8')
        W.close()
        W1 = open(r'.\MainWeb.rbs', 'wb')
        txt = "https://vclock.kr/embed/time/"
        txt = encrypt(txt)
        W1.write(txt)
        W1.close()
