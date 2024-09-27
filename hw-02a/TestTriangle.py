# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(33,33,33),'Equilateral','33,33,33 should be equilateral')
    
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5,6,6),'Isosceles','5,6,6 is an Isosceles triangle')
    
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(8,9,10),'Scalene','8,9,10 is a Scalene triangle')
    
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(12,57,15),'NotATriangle','12,400,15 is Not a triangle')
    
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(43, 37, 0),'InvalidInput','43,37,0 is an Invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(1,1,305),'InvalidInput','1,1,305 is an Invalid input')
    
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(25,50,-1),'InvalidInput','25,50,-1 is an Invalid input')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(89, 76, 0.45),'InvalidInput', '89,76,0.1 is an Invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

