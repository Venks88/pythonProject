class Solution:
    def combinationCandidates(self, candidates, target):
        fullList = []
        tempList = []
        self.createCombinations(fullList, tempList, candidates, target, 0)
        return fullList

    def createCombinations(self, fulllist, templist, candidates, target, start):
        if target == 0:
            fulllist.append(list(templist))
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                continue
            templist.append(candidates[i])
            self.createCombinations(fulllist, templist, candidates, target-candidates[i], i)
            templist.pop()


obj = Solution()
candidates = [2, 3, 6, 7]
target = 7
obj.combinationCandidates(candidates, target)