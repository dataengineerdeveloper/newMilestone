# in order to run test in shell i have to type  on shell comand 'pytest -k and "the name of the file" that i wanna test'

import unittest

from bigger_guy import bigger_guy
#from python.notebooks_xx import three_sum

class alltests(unittest.TestCase):
    def test_bigger_guy(self):
        print('\n\n-----------------')
        print('test function > bigger guy()')
        assert bigger_guy(1,2) == 2
        assert bigger_guy(10,20) == 20
        assert bigger_guy(20,10) == 20
        assert bigger_guy(10,10) == 10
        print('\nAll tests Passed (4/4)')
        print('----------------------')
'''
    def test_three_sum(self):
        print('\n\n-----------------')
        print('test function > three sum()')
        assert three_sum(1,2,3)==5
        print('\nAll tests passed (4/4)')
        print('----------------------')
'''
if __name__ == '__main__':
    unittest.main()