from collections import deque

class Solution:
    def reverseBST(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            indivArray = []
            for _ in range(levelSize):
                currnode = queue.popleft()
                indivArray.append(currnode.val)
                if currnode.left != None:
                    queue.append(currnode.left)
                if currnode.right != None:
                    queue.append(currnode.right)
            result.appendleft(indivArray)

        return result