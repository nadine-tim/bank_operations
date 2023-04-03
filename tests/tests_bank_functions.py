import json
import unittest

from utils import bank_functions


class TestBankFunctions(unittest.TestCase):

    def test_mask_bill(self):
        value = "Счет 15351391408911677994"
        self.assertEqual(bank_functions.mask_bill(value), "Счет **7994")

    def test_mask_from(self):
        value_from = "MasterCard 9175985085449563"
        self.assertEqual(bank_functions.mask_from(value_from), "MasterCard 9175 98** **** 9563")

    def test_filter_and_sort_transactions(self):
        with open('../operations.json') as f:
            data = json.load(f)
            with open('../test_sorted_filtered.json') as tf:
                test_data = json.load(tf)
            self.assertEqual(bank_functions.filter_and_sort_transactions(data), test_data)

    def test_open_file(self):
        with open("../operations.json") as f:
            data = json.load(f)
            self.assertEqual(bank_functions.open_file(), data)


if __name__ == '__main__':
    unittest.main()