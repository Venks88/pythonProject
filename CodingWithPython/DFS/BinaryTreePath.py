class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
  def hasPath(self, root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True

    return self.hasPath(root.left, sum-root.val) or self.hasPath(root.right, sum-root.val)


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(sol.hasPath(root, 23)))
  #print("Tree has path: " + str(sol.hasPath(root, 16)))


main()