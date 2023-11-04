from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:
    def levelOrderSuccessor(self, root, key):
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        queue = deque()
        queue.append(root)

        if root.val == key:
            currNode = queue.popleft()
            if  currNode.right != None and currNode.left != None:
                return currNode.left
            elif currNode.right != None and currNode.left == None:
                return currNode.right
            elif currNode.right == None and currNode.left != None:
                return currNode.left

        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currNode = queue.popleft()

                if currNode.val == key:
                    if currNode.right != None and currNode.left != None:
                        return currNode.left
                    elif currNode.right == None and currNode.left == None:
                        return queue.popleft()
                    elif currNode.right != None and currNode.left == None:
                        return currNode.right
                    elif currNode.right == None and currNode.left != None:
                        return currNode.left

                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                    queue.append(currNode.right)


def main():
    sol = Solution()
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left = TreeNode(4);
    root.left.right = TreeNode(5);

    result = sol.levelOrderSuccessor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = sol.levelOrderSuccessor(root, 9)
    if result:
        print(result.val)

    result = sol.levelOrderSuccessor(root, 12)
    if result:
        print(result.val)


main()
