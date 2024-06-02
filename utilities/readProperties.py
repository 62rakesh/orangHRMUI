import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class readConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('basic info', 'baseURL')
        return url

    @staticmethod
    def getuserName():
        userName = config.get('basic info', 'username')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('basic info', 'password')
        return password

    @staticmethod
    def createPassword():
        createPass = config.get('basic info', 'empPwd')
        return createPass

    @staticmethod
    def read_configurations(category, key):
        config = configparser.ConfigParser()
        config.read(".\\configurations\\config.ini")
        return config.get(category, key)
