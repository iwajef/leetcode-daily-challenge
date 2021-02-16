'''
Feb-07-2021
821. Shortest Distance to a Character
Difficulty: Easy
Link: https://leetcode.com/problems/shortest-distance-to-a-character/
'''

class Solution:
  def shortestToChar(self, s: str, c: str) -> List[int]:
    n = len(s)
    answer = [0 for _ in range(n)]
    indices = []
    for i in range(n):
      if s[i] == c:
        indices.append(i)
    for i in range(n):
      distances = []
      for index in indices:
        distances.append(abs(i-index))
      answer[i] = min(distances)
    
    return answer
