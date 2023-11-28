"""test file for 6-max_integer"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    """test the function

    Args:
        unittest (module): _description_
    """    
    def test_max_integer(self):
        result = max_integer([])
        self.assertIsNone(result)
        lst = [1,2,3,4,6,4]
        result = max_integer(lst)
        self.assertEqual(result, max(lst))
        lst = [-1,-5002,-73,-4,-6,-4]
        result = max_integer(lst)
        self.assertEqual(result, max(lst))
