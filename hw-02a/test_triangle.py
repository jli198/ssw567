# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """
    define multiple sets of tests as functions with names that begin
    """

    def test_right_triangle_a(self):
        """
        Right Triangle Test with sides 3, 4, and 5.
        """
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
        Right Triangle Test with sides 5, 3, and 4.
        """
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_right_triangle_c(self):
        """
        Right Triangle Test with sides 4, 5, and 3.
        """
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def test_equilateral_triangles(self):
        """
        Equilteral Triangle Test with sides 33, 33, and 33.
        """
        self.assertEqual(classify_triangle(33,33,33),'Equilateral','33,33,33 should be equilateral')

    def test_isosceles_triangles(self):
        """
        Isosceles Triangle Test with sides 5, 6, and 6.
        """
        self.assertEqual(classify_triangle(5,6,6),'Isosceles','5,6,6 is an Isosceles triangle')

    def test_scalene_triangles(self):
        """
        Scalene Triangle Test with sides 8, 9, and 10.
        """
        self.assertEqual(classify_triangle(8,9,10),'Scalene','8,9,10 is a Scalene triangle')

    def test_not_a_triangle(self):
        """
        Not a Triangle Test with sides 12, 400, and 15.
        """
        self.assertEqual(classify_triangle(12,57,15),'NotATriangle','12,400,15 is Not a triangle')

    def test_invalid_input_a(self):
        """
        Invalid Input Test with sides 43, 37, and 0.
        """
        self.assertEqual(classify_triangle(43, 37, 0),'InvalidInput','43,37,0 is an Invalid input')

    def test_invalid_input_b(self):
        """
        Invalid Input Test with sides 1, 1, and 305.
        """
        self.assertEqual(classify_triangle(1,1,305),'InvalidInput','1,1,305 is an Invalid input')

    def test_invalid_input_c(self):
        """
        Invalid Input Test with sides 25, 50, and -1.
        """
        self.assertEqual(classify_triangle(25,50,-1),'InvalidInput','25,50,-1 is an Invalid input')

    def test_invalid_input_d(self):
        """
        Invalid Input Test with sides 89, 76, and 0.1.
        """
        self.assertEqual(classify_triangle(89, 76, 0.45),'InvalidInput', '89,76,0.1 is Invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
