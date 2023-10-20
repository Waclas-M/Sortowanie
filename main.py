import unittest
import sorting_largest_smallest_element_of_set
import sorting_from_smallest_to_largest
import sorting_by_the_choice

class Test(unittest.TestCase):
    def test_Max_and_min_number_in_list(self):
        self.assertEqual(sorting_largest_smallest_element_of_set.Max_min([12,2,12,30,60]),(60, 2))
        self.assertEqual(sorting_largest_smallest_element_of_set.Max_min([1,2,3,4,5,6,1000]),(1000, 1))
    def test_from_smallest_to_largest(self):
        self.assertEqual(sorting_from_smallest_to_largest.sorting_from_smallest_to_largest([20,1,2,200,400]),[1,2,20,200,400])
        self.assertEqual(sorting_from_smallest_to_largest.sorting_from_smallest_to_largest([500,1,2,200,400]),[1,2,200,400,500])
        self.assertEqual(sorting_from_smallest_to_largest.sorting_from_smallest_to_largest([20,1,2,200,400,0]),[0,1,2,20,200,400])

    def test_sorting_by_choice(self):
        self.assertEqual(sorting_by_the_choice.choice_sorting([20,10,30,50,60,80]),[10,20,30,50,60,80])
        self.assertEqual(sorting_by_the_choice.choice_sorting([6,5,4,3,2,1]),[1,2,3,4,5,6])
        self.assertEqual(sorting_by_the_choice.choice_sorting([2,10,3,4,5,3]),[2,3,3,4,5,10])
