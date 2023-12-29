class DailyTemperatures:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
obj = DailyTemperatures()
obj.dailyTemperatures(temperatures)