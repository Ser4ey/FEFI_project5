import os
import unittest



def f1(a, b):
    return a/b


class TestAuthInterface(unittest.TestCase):
    # def setUp(self):
    #     self.db = AuthAPI('test.db')
    #
    # def tearDown(self):
    #     if os.path.exists('test.db'):
    #         os.remove('test.db')
    #     else:
    #         print("The file does not exist")

    def test_some(self):
        self.assertEqual(2/4, f1(2, 4))

    def test_some2(self):
        with self.assertRaises(ZeroDivisionError):
            f1(99, 0)



