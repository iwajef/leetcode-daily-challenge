'''
Feb-13-2021
1091. Shortest Path in Binary Matrix
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    size = len(grid)
    if grid == [[0]]:
      return 1
    if grid[0][0] == 1 or grid[size-1][size-1] == 1:
      return -1
    new_x = [-1,-1,-1,0,0,1,1,1]
    new_y = [-1,0,1,-1,1,-1,0,1]
    ans = [[0 for _ in range(size)] for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]
    q = collections.deque()
    def isIndexValid(index):
      return index >= 0 and index < size
    
    q.append([0,0])
    while q:
      [i, j] = q.popleft()
      visited[i][j] = True
      for k in range(8):
        new_i = i + new_x[k]
        new_j = j + new_y[k]
        if isIndexValid(new_i) and isIndexValid(new_j) and grid[new_i][new_j] == 0 and not visited[new_i][new_j]:
          q.append([new_i, new_j])
          ans[new_i][new_j] = ans[i][j] + 1
          visited[new_i][new_j] = True
    
    if ans[size-1][size-1] == 0:
      return -1
    return ans[size-1][size-1] + 1
