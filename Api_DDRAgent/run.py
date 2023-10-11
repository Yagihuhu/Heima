# import unittest
# import smtplib
# from lib.HTMLTestRunnerCN import HTMLTestRunner
# from config.config import *  # 修改导入路径
# from lib.send_email import send_email  # 修改导入路径
# from test.suite.test_suites import *
#
# def discover():
#     return unittest.defaultTestLoader.discover(test_path)
#
#
# def run(suite):
#     logging.info("================================== 测试开始 ==================================")
#     with open(report_file, 'wb') as f:
#         HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
#
#     send_email(report_file)
#     logging.info("================================== 测试结束 ==================================")
#
#
# #
# # def run_suite(suite_name):  # 运行`test/suite/test_suites.py`文件中自定义的TestSuite
# #     suite = get_suite(suite_name)
# #     if suite:
# #         run(suite)
# #     else:
# #         print("TestSuite不存在")
#
# def run_all():  # 运行所用用例
#     run(discover())


import unittest
from lib.HTMLTestRunnerCN import HTMLTestRunner
from config.config import *  # 修改导入路径
from lib.send_email import send_email  # 修改导入路径

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)  # 从配置文件中读取

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api_agent Test", description="测试描述").run(suite)

send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")
