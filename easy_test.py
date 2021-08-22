import unittest

class TestString(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
        

if __name__ == "__main__":
    
    unittest.main()

'''
    test case:测试用例
    一个TestCase的实例就是一个测试用例
    unittest 中的测试方法都以test开头，按照方法名的ASC值的顺序执行
'''

'''
    test fixure：测试夹具
    测试环境的搭建和销毁
    测试前需要登录获取token就是测试前环境的搭建
'''

'''
    test suite :测试套件
    需要一起执行的测试用例放到一块执行
'''

'''
    test runner : 执行测试用例
    用来返回测试用例的执行结果，可以是文本或图形
    例如:HTMLTestRunner
'''