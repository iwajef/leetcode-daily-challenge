'''
Feb-17-2021
11. Container With Most Water
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
  def maxArea(self, height: List[int]) -> int:
    n = len(height)
    i = 0
    j = n - 1
    ans = 0
    while i < j:
      area = min(height[i], height[j]) * (j - i)
      ans = max(ans, area)
      if height[i] < height[j]:  # move pointer i
        i += 1
      else:  # move pointer j
        j -= 1
    return ans

