import unittest

def buggy_abs(y):
  if y >= 0: #oops
    y = 0 - y
  return y

# One test case achieves 100% statement coverage...
assertEqual(buggy_abs(0), 0)
assertEqual(buggy_abs(-3), 3) # But code is wrong! BUggy_abs(-3) == -3

def buggy_abs_XxY(x,y):
  if x>=0 and y>=0: # Two test cases achieve 100% branch coverage
    return x*y
  else:
    return -1*x*y # But code is wrong

assertEqual(buggy_abs_XxY(1, 1), 1)
assertEqual(buggy_abs_XxY(-1, 1), 1)
assertEqual(buggy_abs_XxY(-1, -1), 1)