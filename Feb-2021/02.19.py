'''
Feb-19-2021
1249. Minimum Remove to Make Valid Parentheses
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''

class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    nleft = 0
    idxleft = []

    for i in range(len(s)):
      if s[i] == ')' and nleft == 0:
        s[i] = ''
      elif s[i] == '(':
        nleft += 1
        idxleft.append(i)
      elif s[i] == ')' and nleft > 0:
        nleft -= 1
        idxleft.pop()
    
    if nleft:
      for i in idxleft:
        s[i] = ''
    
    return ''.join(s)
