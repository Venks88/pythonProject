class Valid_Parentheses:
    def isValid(self, s):
        stack = []  # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in pairs:
                stack.append(i);
            elif len(stack) ==  0 or pairs[stack.pop()] != i:
                return False;
        return len(stack) == 0;


obj = Valid_Parentheses()
obj.isValid('{[]{}()}');