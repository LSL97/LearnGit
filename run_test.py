# import unittest
# import test_register
# from HTMLTestRunner import HTMLTestRunner

# # 创建测试套件
# suite = unittest.TestSuite()

# # 通过模块加载测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_register))

# # 创建测试运行程序启动器
# runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
#                         description="注册接口测试报告",        # 报告中显示的描述信息
#                         title=u"自动化测试报告",
#                         tester = 'miki')
                                     

# # 使用启动器去执行测试套件里的用例
# runner.run(suite)
import unittest
import test_register
import HTMLTestRunnerCN

suite = unittest.TestSuite()

# # 通过模块加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))

runner = HTMLTestRunnerCN.HTMLTestReportCN(
    stream = open("report.html", "wb"),
    title=u'自动化测试报告', 
    description='详细测试用例结果',    #不传默认为空
    tester=u"Findyou"     #测试人员名字，不传默认为QA
    )
    #运行测试用例
runner.run(suite)