'''
Feb-20-2021
13. Roman to Integer
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
  def romanToInt(self, s: str) -> int:
    n = len(s)
    ans = 0
    roman_map = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    for i in range(n):
      if i+1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
        # combined number
        ans -= roman_map[s[i]]
      else:
        ans += roman_map[s[i]]
    
    return ans
