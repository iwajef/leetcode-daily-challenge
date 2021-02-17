'''
Feb-16-2021
784. Letter Case Permutation
Difficulty: Medium
Link: https://leetcode.com/problems/letter-case-permutation/
'''

class Solution:
  def letterCasePermutation(self, S: str) -> List[str]:
    ans = []
    def split(s):
      return [char for char in s]
    s = split(S)

    def permutation(s, i):
      if i == len(s):
        ans.append(''.join(s))
        return

      ch = s[i]
      if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z':
        s[i] = ch.lower()
        permutation(s, i+1)
        s[i] = ch.upper()
        permutation(s, i+1)
        s[i] = ch
      else:
        permutation(s, i+1)
    
    permutation(s, 0)
    return ans
