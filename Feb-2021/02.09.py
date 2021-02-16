'''
Feb-09-2021
538. Convert BST to Greater Tree
Difficulty: Medium
Link: https://leetcode.com/problems/convert-bst-to-greater-tree/
'''

class Solution:
  def __init__(self):
    self.suffSum = 0
  
  def reverseInorder(self, root: TreeNode) -> None:
    if root is None:
      return
    self.reverseInorder(root.right)
    root.val = root.val + self.suffSum
    self.suffSum = root.val
    self.reverseInorder(root.left)
  
  def convertBST(self, root: TreeNode) -> TreeNode:
    self.reverseInorder(root)
    return root
