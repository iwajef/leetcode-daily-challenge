'''
Feb-23-2021
240. Search a 2D Matrix II
Difficulty: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
'''

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    def binarySearch(arr, start, end, target) -> bool:
      while start <= end:
        mid = int((start + end) / 2)
        if target == arr[mid]:
          return True
        elif target < arr[mid]:
          end = mid - 1
        elif target > arr[mid]:
          start = mid + 1
      return False

    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
      if binarySearch(matrix[i], 0, n-1, target):
        return True
    return False

