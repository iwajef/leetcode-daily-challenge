'''
Feb-12-2021
1342. Number of Steps to Reduce a Number to Zero
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
'''

class Solution:
  def numberOfSteps(self, num: int) -> int:
    ans = 0
    while num != 0:
      if num % 2 == 1:
        num -= 1
        ans += 1
      else:
        num /= 2
        ans += 1
    return ans
