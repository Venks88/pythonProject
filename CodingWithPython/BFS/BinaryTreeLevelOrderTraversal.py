from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def traverse(self, root):
        result = deque()
        # step 1: check if root is empty
        if root is None:
            return result

        # step 2: add the root to the queue
        queue = deque()
        queue.append(root)

        # step 3: iterate while queue is not empty
        while queue:
            levelSize = len(queue)
            levelArray = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelArray.append(currentNode.val)

                if currentNode.left != None:
                    queue.append(currentNode.left)
                if currentNode.right != None:
                    queue.append(currentNode.right)

            result.append(levelArray)
        return result

def main():
    sol = Solution()
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(sol.traverse(root)))

main()