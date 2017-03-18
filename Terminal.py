# coding:utf8


class Body(object):

    def __init__(self):
        self.root = 'interface/'
        self.main_interface = 'main_interface'
        self.blank_tab = '    '

    def put_from_file(self, file_name):
        with open(self.root + file_name, 'r') as f:
            print f.read()

    def put_main_interface(self):
        self.put_from_file('main_interface')


class Main(object):

    def __init__(self):
        self.put = Body()

    def get_ctrl(self):
        while True:
            try:
                ctrl = int(raw_input('请输入操作：'))
            except ValueError:
                print '指令非法，请重新输入'
            else:
                return ctrl

    def run_in_main_interface(self):
        while True:
            self.put.put_main_interface()
            ctrl = self.get_ctrl()




if __name__ == '__main__':
    test = Main()
    test.run_in_main_interface()