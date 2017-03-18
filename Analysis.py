# coding:utf8
from bs4 import BeautifulSoup
import Down
import re


class Analysis(object):
    def __init__(self, user_name, password):

        self.url_home = 'http://acm.sdut.edu.cn/'
        self.url_contest = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/problemlist/cid/'
        self.url_contest_ranklist = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/contestranklist/cid/'
        self.url_contest_status = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/conteststatus/'
        self.url_user_status = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Solution/status/'
        self.url_state = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Solution/status'

        self.downer = Down.Down(user_name, password)
        self.user_nick, self.uid = self.profile()
        self.user_name = user_name
        self.password = password

    # 获得用户的主页链接及昵称
    def profile(self):
        html = self.downer.get_html("http://acm.sdut.edu.cn/onlinejudge2")
        soup = BeautifulSoup(html, "html5lib").find_all("a")[7]
        nick = soup.text
        uid = re.search(r'\d+.html', soup['href']).group()[:-5]
        return nick, uid

    # 获取比赛的题目列表
    def get_contest(self, cid):
        html = self.downer.get_html(self.url_contest + str(cid))
        soup = BeautifulSoup(html, 'html5lib')
        problem_list = []
        for x in soup.find_all('tr')[2:]:
            problem_list.append(x.td.a['href'][-4:])
        return problem_list

    def read_status(self, url):

        # 传入个人的status页面并解析
        html = self.downer.get_html(url)
        soup = BeautifulSoup(html, 'html5lib')

        # 用来储存数据
        status_list = []
        for tr in soup.find_all(name='tr')[1:-1]:
            tr = tr.find_all(name='td')

            # 解析每一条记录的题号，返回结果和代码链接
            problem = tr[2].text
            result = tr[3].text
            code_url = None

            # 检查每一条记录是否为当前用户提交的，如果是则记录下记录编号用来获取代码链接
            if tr[1].text == self.user_nick:
                code_url = re.search(r'/\d+', tr[6].a['href']).group()[1:]

            status_list.append((problem, result, code_url))

        return status_list

    # 获取一个比赛 status 的 url
    def get_status_url(self, cid=None, total=False):
        # 如果 cid 是 None 并且 total 是 False 则返回个人的,否则如果 cid 不是 None 就返回比赛的，否则返回主页的
        if cid is None and total is False:
            return self.url_user_status + 'username/' + self.user_name + '/uid/' + self.uid
        elif total is False:
            return self.url_contest_status + 'cid/' + str(cid) + '/uid/' + self.uid
        else:
            return self.url_contest_status + 'cid/' + str(cid)

    # 获取最近的一个 status 里提交的信息，判断提交的结果
    def get_submit_result(self, cid=None):
        if cid is not None:
            url = self.get_status_url(cid=cid)
        else:
            url = self.url_state
        problem_list = self.read_status(url)
        for state in problem_list:
            if not (state[2] is None):
                return state[1]

if __name__ == "__main__":
    oj = Analysis("16110543049", "FS109412")
    print oj.get_submit_result(cid=2083)
