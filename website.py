import webbrowser


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
