from collections import *


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
    def zigzagTravel(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            sizeLevel = len(queue)
            outArray = deque()
            leftRight = True
            for _ in range(sizeLevel):
                currNode = queue.popleft()
                if leftRight:
                    outArray.append(currNode.val)
                else:
                    outArray.appendleft(currNode.val)

                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                        queue.append(currNode.right)

            result.append(list(outArray))
            leftRight = not leftRight

        return result


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(sol.zigzagTravel(root)))


main()