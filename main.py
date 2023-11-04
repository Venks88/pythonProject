import itertools

class Solution(object):
    def splitNum(self, num):
        """sort the num"""
        x = ''.join(sorted(str(num)));
        a = int(x[::2]);
        b = int(x[1::2]);
        return a+b;

obj = Solution();
obj.splitNum(123456789);