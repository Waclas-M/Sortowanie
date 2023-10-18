import unittest
import sorting_largest_smallest_element_of_set

class Test(unittest.TestCase):
    def test_Max_and_min_number_in_list(self):
        self.assertEqual(sorting_largest_smallest_element_of_set.Max_min([12,2,12,30,60]),(60, 2))
        self.assertEqual(sorting_largest_smallest_element_of_set.Max_min([1,2,3,4,5,6,1000]),(1000, 1))

