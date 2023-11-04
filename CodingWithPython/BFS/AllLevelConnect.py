from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


class Solution:
  def connect_all_siblings(self, root):
    result = []
    if root is None:
      return result

    queue = deque()
    queue.append(root)
    while queue:
      lenSize = len(queue)
      for i in range(0, lenSize):
        currentNode = queue.popleft()
        if i == 0:
            result.append(currentNode.val)
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  print("Tree Minimum Depth: " + str(sol.connect_all_siblings(root)))


main()
