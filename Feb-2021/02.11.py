'''
Feb-11-2021
242. Valid Anagram
Difficulty: Eazy
Link: https://leetcode.com/problems/valid-anagram/
'''

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s_c = collections.Counter(s)
    t_c = collections.Counter(t)
    return s_c == t_c
