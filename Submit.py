# coding:utf8
from Down import Down
from Analysis import Analysis


class Submit(object):
    def __init__(self, user, password):
        self.downer = Down(user, password)
        self.analyst = Analysis(user, password, self.downer)

    def submit_contest(self, cid):
        problem_list = self.analyst.get_contest(cid)

        print cid, ':'

        for x in problem_list:
            if self.accepted_problem(x, cid) != "Success":
                print "Submit Fail"
                continue

            result = "Waiting"
            while result == 'Waiting':
                result = self.analyst.get_submit_result(cid)
            print "   ", x, result

    def get_accepted_code(self, pid):
        return self.downer.get_html('http://acmfish.top/' + pid)

    def accepted_problem(self, pid, cid=None, lang='g++'):
        code = self.get_accepted_code(pid)
        if code == 'File not find':
            return 'Code not find'

        self.downer.submit_problem(pid, code, cid, lang)
        return 'Success'

if __name__ == "__main__":
    oj = Submit("test_234", "FS109412")
    for x in range(2071, 2080):
        oj.submit_contest(x)
