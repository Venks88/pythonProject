class Solution(object):
    def maxArea(self, height):
        ptr1 = 0
        ptr2 = len(height)-1
        total = []
        while ptr1 != ptr2:
            gap = ptr2 - ptr1
            smallest = min(height[ptr1], height[ptr2])
            total.append(smallest * gap)
            ptr1 = ptr1 + 1
            ptr2 = ptr2 - 1
        return total


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution()
obj.maxArea(height)
