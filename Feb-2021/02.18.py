'''
Feb-18-2021
413. Arithmetic Slices
Difficulty: Medium
Link: https://leetcode.com/problems/arithmetic-slices/
'''

class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    n = len(A)
    if n < 3:
      return 0
    
    ans = 0
    count = 1
    for i in range(2, n):
      if A[i] - A[i-1] == A[i-1] - A[i-2]:
        ans += count
        count += 1
      else:
        count = 1
    
    return ans
