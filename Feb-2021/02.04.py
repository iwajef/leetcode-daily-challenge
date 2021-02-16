'''
Feb-04-2021
594. Longest Harmonious Subsequence
Difficulty: Easy
Link: https://leetcode.com/problems/longest-harmonious-subsequence/
'''

class Solution:
  def findLHS(self, nums: List[int]) -> int:
    myMap = collections.Counter(nums)
    keys = set(nums)
    ansMap = {}
    for key in keys:
      if key-1 not in keys and key+1 not in keys:
        ansMap[key] = 0
      else:
        ansMap[key] = max(myMap[key] + myMap[key-1], myMap[key] + myMap[key+1])
    return max(ansMap.values())
