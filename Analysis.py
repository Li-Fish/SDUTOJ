# coding:utf8
from bs4 import BeautifulSoup
import Down
import re


class Analysis(object):
    def __init__(self, user_name, password):
        self.downer = Down.Down(user_name, password)
        self.url_home = 'http://acm.sdut.edu.cn/'
        self.url_contest = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/problemlist/cid/'
        self.url_contest_ranklist = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/contestranklist/cid/'
        self.url_contest_status = 'http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/conteststatus/'
        self.user_nick, self.uid = self.profile()

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

if __name__ == "__main__":
    oj = Analysis("test_234", "FS109412")