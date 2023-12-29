class Solution:
    def perfectSquare(self, num: int) -> bool:
        numInt = 0
        while (numInt*numInt < num):
            numInt = numInt + 1
            if num == numInt*numInt:
                return True
        return False


num = 1
obj = Solution()
obj.perfectSquare(num)