'''
Feb-10-2021
138. Copy List with Random Pointer
Difficulty: Medium
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
'''

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    d = defaultdict(lambda:Node(0))
    d[None] = None
    while node:
      d[node].val = node.val
      d[none].next = d.[node.next]
      d[node].random = d[node.random]
      node = node.next
    return d[head]
