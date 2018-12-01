#coding:utf-8
import unittest
import function
from mock import patch
class MyTestCase(unittest.TestCase):
    """
在定义测试用例中，将mock的multiply()函数（对象）重命名为 mock_multiply对象。
mock_multiply.return_value = 15
设定mock_multiply对象的返回值为固定的15。
ock_multiply.assert_called_once_with(3, 5)
检查ock_multiply方法的参数是否正确。
    """
    @patch("function.multiply")
    def test_add_and_multiply(self,mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addi,multiple = function.add_and_multiply(x,y)
        mock_multiply.assert_called_once_with(3,5)

        self.assertEqual(8,addi)
        self.assertEqual(15,multiple)
if __name__ =="__main__":
    unittest.main()