'''
Feb-05-2021
71. Simplify Path
Difficulty: Medium
Link: https://leetcode.com/problems/simplify-path/
'''

class Solution:
  def simplifyPath(self, path: str) -> str:
    arr = []
    for item in path.split('/'):
      if item != '.' and item != '':
        arr.append(item)
    
    arr2 = collections.deque()
    for i in range(len(arr)):
      if arr[i] != '..':
        arr2.append(arr[i])
      elif arr[i] == '..' and len(arr2) >= 1:
        arr2.pop()
      elif arr[i] == '..' and len(arr2) == 0:
        continue
    
    if len(arr2) == 0:
      return '/'
    else:
      s = ''
      for item in arr2:
        s += '/' + item
      return s
