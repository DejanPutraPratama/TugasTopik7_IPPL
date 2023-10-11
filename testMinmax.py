import unittest
from minmax1 import nilai_maksimal,nilai_minimal


class TestNilai(unittest.TestCase):

    def test_nilai_maksimal(self):
        self.assertEqual(nilai_maksimal([3,20,100,-35,50]), 100)
        self.assertEqual(nilai_maksimal([-1,-2,-3,-4,-5]), -1)
        self.assertEqual(nilai_maksimal([0,0,0,0,0]), 0)

    def test_nilai_minimal(self):
        self.assertEqual(nilai_minimal([3,20,100,-35,50]), -35)
        self.assertEqual(nilai_minimal([-1,-2,-3,-4,-5]), -5)
        self.assertEqual(nilai_minimal([0,0,0,0,0]), 0)

if __name__ == '__main__':
    unittest.main()