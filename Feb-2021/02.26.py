'''
Feb-27-2021
946. Validate Stack Sequences
Difficulty: Medium
Link: https://leetcode.com/problems/validate-stack-sequences/
'''

class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    s = []
    i = 0
    for num in pushed:
      s.append(num)
      while len(s) and s[len(s)-1] == popped[i]:
        s.pop()
        i += 1
    return len(s) == 0
