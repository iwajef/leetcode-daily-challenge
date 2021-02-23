'''
Feb-21-2021
524. Longest Word in Dictionary through Deleting
Difficulty: Medium
Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
'''

class Solution:
  def findLongestWord(self, s: str, d: List[str]) -> str:
    n = len(s)
    ans = []
    ans2 = []
    for word in d:
      i = 0  # points to s
      j = 0  # points to word
      wordLength = len(word)
      while i < n:
        if j == wordLength:
          ans.append(word)
          break
        elif s[i] != word[j]:
          i += 1
        elif s[i] == word[j]:
          i += 1
          j += 1
          if i == n and j == wordLength:
            ans.append(word)
    if not len(ans):
      return ""
    ans.sort(key=len, reverse=True)
    maxLen = len(ans[0])
    for word in ans:
      if len(word) == maxLen:
        ans2.append(word)
      else:
        break
    ans2.sort()
    return ans2[0]

