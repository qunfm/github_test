#coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    @classmethod  #所有case运行前只运行一次
    def setUpClass(cls):
        print("start!")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print("end!jj")

    def test01(self):
        u'''测试登录用例，账号：xx 密码xx'''  #报告中的注释
        print u"执行测试用例01"
    def test03(self):
        print u"执行测试用例03"
    def test3(self):
        print("3 case")
    def test_add(self):
        print("add")
    def test_dev(self):
        print("dev")
    def test02(self):
        print("case 02")
    def add_test(self):  #只执行test开头的case
        print("add method")
if __name__=="__main__":
    unittest.main()

#01-02-03-3 根据用例名称来顺序执行