class RemoveNodes:
    def removeNodesFunction(self, head):
        stack = []
        for i in range(len(head)):
            while stack and head[i] > head[stack[-1]]:
                print("asdasd")
        return head


head = [5, 3, 7, 4, 2, 1]
obj = RemoveNodes()
obj.removeNodesFunction(head)