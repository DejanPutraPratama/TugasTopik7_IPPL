import unittest
from kalkulator import hitung

class TestKalkulator(unittest. TestCase):
    def test_penjumlahan(self):
        self.assertEqual(hitung('1', 6, 3), 9)

    def test_pengurangan(self):
        self.assertEqual(hitung('2', 6, 3), 3)

    def test_perkalian(self):
        self.assertEqual(hitung('3', 6, 3), 18)

    def test_pembagian(self):
        self.assertEqual(hitung('4', 6, 3),  2)

    def test_operasi_tidak_valid(self):
        with self.assertRaises(ValueError):
            hitung('5', 6, 2)

if __name__ == '__main__':
    unittest.main()