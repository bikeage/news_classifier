import unittest
import data_prep
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

if __name__ == '__main__':
    unittest.main() 
