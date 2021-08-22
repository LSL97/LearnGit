import unittest
#导入测试代码
from register import register

class TestRegister(unittest.TestCase):
    
    def setUp(self):
        # 每条用例执行之前都会执行
        print("用例{}开始执行--".format(self))

    def tearDown(self):
        # 每条用例执行之后都会执行
        print("用例{}执行结束--".format(self))

    @classmethod	# 指明这是个类方法以类为维度去执行的
    def setUpClass(cls):
        # 整个测试用例类中的用例执行之前，会先执行此方法
        print("-----setup---class-----")

    @classmethod
    def tearDownClass(cls):
        # 整个测试用例类中的用例执行完之后，会执行此方法
        print("-----teardown---class-----")

    def test_register_success(self):
        data = ('mikitest','miki123','miki123')
        expected = {'code':1, 'msg':'注册成功'}
        result = register(*data)
        self.assertEqual(expected,result)

    def test_username_isnull(self):
        data = ('','miki123','mii123')
        expected = {'code':0, 'msg':'所有参数不能为空'}
        result = register(*data)
        self.assertEqual(expected,result)

    def test_pwd1_not_pwd2(self):
        data = ('miki123','test123','123test')
        expected = {'code':0, 'msg':'两次密码不一致'}
        result = register(*data)
        self.assertEqual(expected,result)        

if __name__ == '__main__':
    unittest.main()
        
