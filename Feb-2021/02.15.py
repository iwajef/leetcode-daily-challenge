'''
Feb-15-2021
1337. The K Weakest Rows in a Matrix
Difficulty: Eazy
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    y = len(mat)
    x = len(mat[0])
    vis = [0] * y
    ans = []
    for j in range(x + 1):
      for i in range(y):
        if not vis[i] and (j == x or not mat[i][j]):
          ans.append(i)
          vis[i] = 1
        if len(ans) == k:
          return ans
