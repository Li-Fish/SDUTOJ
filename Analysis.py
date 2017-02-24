# coding:utf8
from bs4 import BeautifulSoup
import Down
import re

class Analysis(object):
    def __init__(self, user_name, password):
        self.downer = Down.Down(user_name, password)

    def profile(self):
        html = self.downer.get_html("http://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Contest/problemlist/cid/2022")
        soup = BeautifulSoup(html, "html5lib")
        print soup

if __name__ == "__main__":
    oj = Analysis("16110543049", "FS109412")
    oj.downer.login()
    oj.profile()