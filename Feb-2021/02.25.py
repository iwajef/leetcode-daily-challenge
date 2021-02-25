'''
Feb-25-2021
581. Shortest Unsorted Continuous Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
'''

class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    start = -1
    end = -2
    maxn = -float('inf')
    minn = float('inf')
    for i in range(n):
      if nums[i] >= maxn:
        maxn = nums[i]
      else:
        end = i
    for j in range(n-1, -1, -1):
      if nums[j] <= minn:
        minn = nums[j]
      else:
        start = j
    
    return end - start + 1
