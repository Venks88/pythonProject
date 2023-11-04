class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findSequence(self, root, sequence):
    if root is None:
      return False

    return self.findAllSequence(root, sequence, 0)

  def findAllSequence(self, currNode, sequence, idx):
    if currNode is None:
      return False
    