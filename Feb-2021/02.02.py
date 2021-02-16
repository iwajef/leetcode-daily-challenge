'''
Feb-02-2021
669. Trim a Binary Search Tree
Difficulty: Medium
Link: https://leetcode.com/problems/trim-a-binary-search-tree/
'''

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
    if root is None:
      return
    if root.val >= low:
      root.left = self.trimBST(root.left, low, high)
    else:
      root = self.trimBST(root.right, low, high)
    
    if root is None:
      return
    if root.val <= high:
      root.right = self.trimBST(root.right, low, high)
    else:
      root = self.trimBST(root.left, low, high)
    
    return root

