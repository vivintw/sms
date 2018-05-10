import requests
import time

class sms:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.token = None
        self.s = requests.session()
        self.s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        self.login = True

    def __login(self):
        url = "http://www.way2sms.com/Login1.action"
        p = {
        "username": self.username,
        "password": self.password
        }
        res = self.s.post(url,data=p)
        self.token = res.url.split('=')[1].split('?')[0]

    def send_message(self,to,msg):
        if self.login:
            self.__login()
            self.login = False

        url = "http://www.way2sms.com/smstoss.action"
        p = {
        "ssaction": "ss",
        "Token": self.token,
        "mobile": to,
        "message": msg,
        "msgLen": '135',
        }
        res = self.s.post(url,data=p)
        time.sleep(1)
        if res.status_code == '200':
            return True
        return False

if __name__ == "__main__":
    # sms through way2sms
    s = sms('regestered_mob_no','password')
    s.send_message('to-mob-no','test message 1')
    s.send_message('to-mob-no','test message 2')
