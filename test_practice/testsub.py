from test_practice.caculator import Count
import unittest
class TestSub(unittest.TestCase):
    def setUp(self):
        print("test sub start")

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)

    def tearDown(self):
        print('test sub end')
if __name__=='__main__':
    unittest.main()