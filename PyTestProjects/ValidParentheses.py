class Solution:
    def validParentheses(self, parentheses):
        paren = list(parentheses)
        stack = []
        mapList = {"]":"[", "}":"{", ")":"("}
        for i in paren:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            if i == "]" or i == "}" or i == ")":
                length = len(stack)-1
                if stack[length] == mapList.get(i):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


obj = Solution()
parentheses = "()[]{}"
obj.validParentheses(parentheses)