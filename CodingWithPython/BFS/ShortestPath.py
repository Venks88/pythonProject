from collections import *


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def shortestPath(self, root):
        result = []

        if root is None:
            return result

        if root.left is None and root.right is None:
            return 1;

        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            levelsize = len(queue)
            count = count + 1
            for _ in range(levelsize):
                currNode = queue.popleft()

                if currNode.left == None and currNode.right == None:
                    return count

                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                    queue.append(currNode.right)
        return count


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(sol.shortestPath(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(sol.shortestPath(root)))


main()
