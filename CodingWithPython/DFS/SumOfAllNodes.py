class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findSumOfPaths(self, root):
      return self.findPaths(root, 0)

  def findPaths(self, currentNode, pathSum):
    if currentNode is None:
        return 0

    pathSum = 10 * pathSum + currentNode.val

    if currentNode.val == pathSum and currentNode.left is None and currentNode.right is None:
        return pathSum

    return self.findPaths(currentNode.left, pathSum) + self.findPaths(currentNode.right, pathSum)