'''
Feb-08-2021
284. Peeking Iterator
Difficulty: Medium
Link: https://leetcode.com/problems/peeking-iterator/
'''

'''
class Iterator:
  def __init__(self, nums):
    """
    Initializes an iterator object to the beginning of a list.
    :type nums: List[int]
    """

  def hasNext(self):
    """
    Returns true if the iteration has more elements.
    :rtype: bool
    """

  def next(self):
    """
    Returns the next element in the iteration.
    :rtype: int
    """
'''

class PeekingIterator:
  def __init__(self, iterator):
    """
    Initialize your data structure here.
    :type iterator: Iterator
    """
    self.iterator = iterator
    self.cache = self.iterator.next() if self.iterator.hasNext() else None

  def peek(self):
    """
    Returns the next element in the iteration without advancing the iterator.
    :rtype: int
    """
    return self.cache

  def next(self):
    """
    :rtype: int
    """
    current_value = self.cache
    self.cache = self.iterator.next() if self.iterator.hasNext() else None
    return current_value

  def hasNext(self):
    """
    :rtype: bool
    """
    return self.cache != None
