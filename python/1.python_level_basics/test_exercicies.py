import unittest

from python.notebooks_01 import bigger_guy
#from python.notebooks_xx import three_sum

class altests(unittest.TestCase):
    def test_bigger_guy(self):
        print('\n\n-----------------')
        print('test function > bigger guy()')
        assert bigger_guy(1,2) == 2
        assert bigger_guy(10,20) == 20
        assert bigger_guy(20,10) == 20
        assert bigger_guy(10,10) == 10
        print('\nAll tests Passed (4/4)')
        print('----------------------')
    
    def test_three_sum(self):
        print('\n\n-----------------')
        print('test function > three sum()')
        assert three_sum(1,2,3)==5
        print('\nAll tests passed (4/4)')
        print('----------------------')

if __name__ == '__main__':
    unittest.amin()