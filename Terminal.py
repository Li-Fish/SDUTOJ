# coding:utf8


class Body(object):

    def __init__(self):
        self.root = 'interface/'
        self.main_interface = 'main_interface'
        self.blank_tab = '    '

    def put_from_file(self, file_name):
        with open(self.root + file_name, 'r') as f:
            print f.read()

    def show_problem_list(self, problem_list, page):
        print self.blank_tab + '题目列表 ' + page + ' 页'
        cnt = 0
        for problem in problem_list:
            print problem[0], problem[1]


if __name__ == '__main__':
    test = Body()
    test.put_from_file(test.main_interface)