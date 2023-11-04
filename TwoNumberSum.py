class TwoNumberSum:
    def twoNumberSum(self, array, targetSum):
        finArray = [];
        for i in range(0, len(array)):
            for j in range(0, len(array)):
                if i == j:
                    """No-Op"""
                else:
                    out = array[i] + array[j]
                    if out == targetSum:
                        finArray.append(array[i])
                        finArray.append(array[j])

        finArray = set(finArray)
        return finArray
    pass


obj = TwoNumberSum()
array = [4, 6]
targetSum = 10
obj.twoNumberSum(array, targetSum)