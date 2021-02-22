'''
Feb-21-2021
991. Broken Calculator
Difficulty: Medium
Link: https://leetcode.com/problems/broken-calculator/
'''

class Solution:
  def brokenCalc(self, X: int, Y: int) -> int:
    ans = 0
    while X < Y:
      ans += 1
      if Y % 2:
        Y += 1
      else:
        Y //= 2
    return X - Y + ans
