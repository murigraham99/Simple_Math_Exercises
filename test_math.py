import unittest
import math_exercises

class TestMathExercises(unittest.TestCase):
    def test_sum(self):
        # result = math_exercises.sum(10, 5)
        self.assertEqual(math_exercises.sum(10, 5), 15)
        self.assertEqual(math_exercises.sum(-10, 10), 0)
        self.assertEqual(math_exercises.sum(-10, -5), -15)

    def test_factorial(self):
        self.assertEqual(math_exercises.factorial(5), 120)
        self.assertEqual(math_exercises.factorial(-3), -6)
        self.assertEqual(math_exercises.factorial(0), 1)

    def test_circle_area(self):
        self.assertEqual(math_exercises.circle_area(5), 79)
        with self.assertRaises(ValueError): # checks if in case of 0 as an input Value Error exception is raised
            math_exercises.circle_area(0)

    def test_average(self):
        self.assertEqual(math_exercises.average([1,2,3,4]), 2.5)
        self.assertEqual(math_exercises.average([-1,-2,-3]), -2)
        self.assertEqual(math_exercises.average([-1,-2,-3,0,5]), -0.2)


    def test_even_odd(self):
        self.assertEqual(math_exercises.even_odd(2), 'even')
        self.assertEqual(math_exercises.even_odd(3), 'odd')

    def test_divisible(self):
        self.assertEqual(math_exercises.divisible(10,5), 'It is divisible')
        self.assertEqual(math_exercises.divisible(10,11), 'Not divisible')
        with self.assertRaises(ValueError):
            math_exercises.divisible(2,0)

    def test_distance_points(self):
        self.assertEqual(math_exercises.distance_points(3,5,8,9), 6)
        self.assertEqual(math_exercises.distance_points(-3,5,8,9), 12)
        self.assertEqual(math_exercises.distance_points(-3,5,8,0), 12)






if __name__ == '__main__':
    unittest.main()
