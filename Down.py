# coding:utf8
import requests


class Down(object):
    def __init__(self, user_name, password):
        #初始化常用URL
        self.url_home = 'http://acm.sdut.edu.cn/onlinejudge2'
        self.url_login = '/index.php/Home/Login/login.html'
        self.url_submit_problem = '/index.php/Home/Solution/submitsolution'
        self.url_submit_contest = '/index.php/Home/Contest/contestsubmit/cid/'

        #初始化配置
        self.user_name = user_name
        self.password = password
        self.session = requests.session()
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        self.login()

    def login(self):
        print requests.post(url="http://acm.sdut.edu.cn/onlinejudge2/index.php/Login/login.html",
                          data={'user_name':self.user_name, 'password':self.password},
                          headers=self.headers).url

    def submit_problem(self, pid, code, cid=None, lang='g++'):
        post_data = {'pid': pid, 'lang': lang, 'code': code}

        #反馈信息
        information = 'pid:' + str(pid) + ' Success'

        #区分在Problems提交和Contest里提交
        if cid is None:
            url = self.url_home + self.url_submit_problem
        else:
            url = self.url_home + self.url_submit_contest + str(cid)
            information += ' in cid:' + str(cid)
            post_data['cid'] = cid

        self.session.post(url, post_data, headers=self.headers)

        return information

    def get_html(self, url):
        return requests.get(url, headers=self.headers).content

    def add_discuss(self, title, content, pid=1000):
        self.session.get(url=self.url_home + '/index.php/Home/Discuss/addtopic',
                         params={'pid': str(pid), 'title': title, 'content': content},
                         headers=self.headers)
        return "Success"


if __name__ == '__main__':
    oj = Down("16110543049", "FS109412")
    #print oj.get_html("http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/problemlist/cid/2022")