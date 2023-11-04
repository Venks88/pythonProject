from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def lvlOrder(self, root):
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            outArray = []
            lensize = len(queue)
            for _ in range(lensize):
                currnode = queue.popleft()
                outArray.append(currnode.val)

                if currnode.left != None:
                    queue.append(currnode.left)
                if currnode.right != None:
                    queue.append(currnode.right)
            result.append(outArray)
        return result


def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("SIbling traversal: " + str(sol.lvlOrder(root)))

main()