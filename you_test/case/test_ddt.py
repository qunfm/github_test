#coding:utf-8
import ddt
import unittest
testData = [{"usename":"selenium","psw":"123456"},{"usename":"python","psw":"111111"},{"usename":"appium","psw":"654321"}]
@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start...")
    def tearDown(self):
        print("end...")
    @ddt.data(*testData)
    def test_ddt(self,data):
        print data
if __name__ == "__main__":
    unittest.main()
    #为什么打印的结果是pass 和usename 反的 test