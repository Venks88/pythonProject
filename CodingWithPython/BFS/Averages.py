from collections import *
from statistics import mean

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
    def average(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            outArray = []
            for _ in range(levelSize):
                currNode = queue.popleft()
                outArray.append(currNode.val)
                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                    queue.append(currNode.right)
            # get the average
            result.append(mean(outArray))
        return result


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Zigzag traversal: " + str(sol.average(root)))


main()