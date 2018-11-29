#coding:utf-8
import unittest
class Test(unittest.TestCase):
    def test01(self):
        u"""assert a==b"""
        a = 1
        b = 1
        self.assertEqual(a,b)
    def test02(self):
        u"""assert a in b"""
        a = "hello"
        b = "hello world"
        self.assertIn(a,b)
    def test03(self):
        u"""a is true"""
        a = True
        self.assertTrue(a)
    def test04(self):
        u"""failed case"""
        a = "lix"
        b = "yoy"
        self.assertEqual(a,b)
if __name__ == "__main__":
    unittest.main()
