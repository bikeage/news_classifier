import unittest
import data_prep, nyt_scrapper
import datetime as dt

import features

class TestBasicFeatures(unittest.TestCase):

    def test_sanity(self):        
        self.assertEqual(1+1, 2)

    def test_sanity_2(self):
        self.assertFalse(False,0)

    def test_count_misspellings(self):
        '''asserts this function returns 0
        '''
        self.assertEqual(features.count_misspellings(), 0)  

    def test_date_to_string(self):
        self.assertEqual(nyt_scrapper.date_to_string(dt.date(1999, 9, 9)), '19990909')

if __name__ == '__main__':
    unittest.main() 
