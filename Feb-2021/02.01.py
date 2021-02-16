'''
Feb-01-2021
191. Number of 1 Bits
Difficulty: Easy
Link: https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
  def hammingWeight(self, n: int) -> int:
    binary = [2 ** i for i in range(31, -1, -1)]
    count = 0
    for i in range(32):
      if n >= binary[i]:
        count += 1
        n -= binary[i]
    return count
