#coding:utf-8
import unittest
import os
import HTMLTestRunner

# python2.7要是报编码问题，就加这三行，python3不用加

import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

# 用例路径
case_path = os.path.join(os.getcwd(), "case")
print(case_path)
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
print(report_path)
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    print(report_abspath)


    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()