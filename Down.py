# coding:utf8
import requests

class Down(object):
    def __init__(self, user_name, password):
        self.url_home = 'http://acm.sdut.edu.cn/onlinejudge2'
        self.url_login = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Login/login.html'
        self.url_submit = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Solution/submitsolution'

        self.user_name = user_name
        self.password = password
        self.session = requests.session()
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    def login(self):
        self.session.post(self.url_login,
                          {'user_name':self.user_name, 'password':self.password},
                          headers=self.headers)

    def get_contest(self):
        response = self.session.get(url='http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/problemlist/cid/2017',
                                    headers=self.headers)
        print response.content

if __name__ == '__main__':
    oj = Down('test_234', 'FS109412')
    oj.login()
    oj.get_contest()