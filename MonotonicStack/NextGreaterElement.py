class NumGreaterElement:
    def nextGreaterElement(self, nums1, nums2):
        stack, hashMap = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                hashMap[stack.pop()] = num
            stack.append(num)

        list_return = []
        for num in nums1:
            value = hashMap.get(num, -1)
            list_return.append(value)

        return list_return


nums1 = [4, 2, 6]
nums2 = [6, 2, 4, 5, 3, 7]
obj = NumGreaterElement()
obj.nextGreaterElement(nums1, nums2)
