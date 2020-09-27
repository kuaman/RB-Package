import configparser


def readconfig(big, small):
    config = configparser.ConfigParser()
    config.read(r'./config.ini', encoding='UTF-8')
    conf = config[big][small]
    return conf


def writeconfig(big, small, data):
    config = configparser.ConfigParser()
    config.read(r'./config.ini', encoding='UTF-8')
    config.set(big, small, data)
    with open(r".\config.ini", "w") as configfile:
        config.write(configfile)
