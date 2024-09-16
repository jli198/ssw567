import pytest
import unittest

def classify_triangle(a,b,c):
  if(a <= 0 or b <= 0 or c <= 0):
    return "Your shape is not a triangle."
  elif (a == b and b == c):
    return "Your triangle is equilateral."
  elif (a !=b and a != c and b != c):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
      return "Your triangle is a right one."
    return "Your triangle is scalene."
  if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    return "Your triangle is a right one."
  else:
    return "Your triangle is isoceles."
  
class triangleTest(unittest.TestCase):
  def test_zeroes(self):
    self.assertEqual(classify_triangle(0, 0, 0), "Your shape is not a triangle.")
  def test_negatives(self):
    self.assertEqual(classify_triangle(-1,-2,-3), "Your shape is not a triangle.")
  def test_equilateral(self):
    self.assertEqual(classify_triangle(5, 5, 5), "Your triangle is equilateral.")
  def test_right(self):
    self.assertEqual(classify_triangle(3, 4, 5), "Your triangle is a right one.")
  def test_scalene(self):
    self.assertEqual(classify_triangle(4, 5, 6), "Your triangle is scalene.")
  def test_isosceles(self):
    self.assertEqual(classify_triangle(7, 7, 8), "Your triangle is isoceles.")

if __name__ == '__main__':
  unittest.main()