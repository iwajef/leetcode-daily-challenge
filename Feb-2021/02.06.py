'''
Feb-06-2021
199. Binary Tree Right Side View
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-right-side-view/
'''

class Solution:
  def rightSideView(self, root: TreeNode) -> List[int]:
    ans = []
    q = collections.deque()

    if root is None:
      return []
    
    q.append(root)
    while q:
      n = len(q)
      for i in range(1, n+1):
        node = q.popleft()
        if i == n:
          ans.append(node.val)
        if node.left is not None:
          q.append(node.left)
        if node.right is not None:
          q.append(node.right)
    
    return ans
