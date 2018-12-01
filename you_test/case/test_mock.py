#coding:utf-8
import mock
import unittest
import sys
#sys.path.append('..')
#from modular import Count
from mock_1.modular import *
"""
class TestCount(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value = 13)
        result = count.add(8,5)
        self.assertEqual(result,13)
        """
class MockDemo(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add=mock.Mock(return_value=13,side_effect=count.add)
        result = count.add(8,8)
        print(result)
        count.add.assert_called_with(8,8)
        self.assertEqual(result,16)
if __name__ == '__main__':
    unittest.main()