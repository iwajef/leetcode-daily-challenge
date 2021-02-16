'''
Feb-03-2021
141. Linked List Cycle
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/
'''

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    if head is None or head.next is None:
      return False
    
    slow = head
    fast = head.next

    while True:
      if slow == fast:
        return True
      if fast is None or fast.next is None:
        return False
      slow = slow.next
      fast = fast.next.next
