# coding:utf8
import requests


class Down(object):
    def __init__(self, user_name, password):
        # 初始化常用URL
        self.url_home = 'http://acm.sdut.edu.cn/onlinejudge2'
        self.url_login = '/index.php/Home/Login/login.html'
        self.url_submit_problem = '/index.php/Home/Solution/submitsolution'
        self.url_submit_contest = '/index.php/Home/Contest/contestsubmit/cid/'

        # 初始化配置
        self.user_name = user_name
        self.password = password
        self.session = requests.session()
        self.session.get(self.url_home)
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.login()

    def login(self):
        self.session.post(url=self.url_home + self.url_login,
                          data={'user_name':self.user_name, 'password':self.password},
                          headers=self.headers)

    def submit_problem(self, pid, code, cid=None, lang='g++'):
        post_data = {'pid': pid, 'lang': lang, 'code': code}

        # 反馈信息
        information = 'pid:' + str(pid) + ' Success'

        # 区分在Problems提交和Contest里提交
        if cid is None:
            url = self.url_home + self.url_submit_problem
        else:
            url = self.url_home + self.url_submit_contest + str(cid)
            information += ' in cid:' + str(cid)
            post_data['cid'] = cid

        self.session.post(url, post_data, headers=self.headers)

        return information

    def get_html(self, url):
        return self.session.get(url, headers=self.headers).content

    def add_discuss(self, title, content, pid=1000):
        self.session.get(url=self.url_home + '/index.php/Home/Discuss/addtopic',
                         params={'pid': str(pid), 'title': title, 'content': content},
                         headers=self.headers)
        return "Success"

    def get_accepted_code(self, pid):
        return self.session.get('http://acmfish.top/' + pid).content

    def accepted_problem(self, pid, cid=None, lang='g++'):
        code = self.get_accepted_code(pid)
        if code == 'File not find':
            return 'Code not find'

        self.submit_problem(pid, code, cid, lang)
        return 'Accepted'

if __name__ == '__main__':
    pass
