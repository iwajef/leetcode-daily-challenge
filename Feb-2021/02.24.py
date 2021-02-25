'''
Feb-24-2021
856. Score of Parentheses
Difficulty: Medium
Link: https://leetcode.com/problems/score-of-parentheses/
'''

class Solution:
  def scoreOfParentheses(self, S: str) -> int:
    if S == "()":
      return 1
    n = len(S)
    layer = 0
    for i in range(n):
      if S[i] == '(':
        layer += 1
      elif S[i] == ')':
        layer -= 1
        if layer == 0 and i < n-1:
          return self.scoreOfParentheses(S[:i+1]) + self.scoreOfParentheses(S[i+1:])
    else:
      return 2 * self.scoreOfParentheses(S[1:n-1])

