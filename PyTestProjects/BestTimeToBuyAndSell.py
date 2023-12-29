import numpy as np
class Solution:
    def bestTime(self, prices):
        outList = []
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i != j and i < j:
                    if prices[i] < prices[j]:
                        outList.append([i, j, prices[j] - prices[i]])
        val = []
        for i in outList:
            val.append(i[2])
        return np.max(val)


obj = Solution()
prices = [3, 2, 6, 5, 0, 3]
obj.bestTime(prices)