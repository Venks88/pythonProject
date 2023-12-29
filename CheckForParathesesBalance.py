def checkForBalance(parentheses):
    parenStack = []
    for i in range(len(parentheses)):
        out = checkForParens(parentheses[i], parenStack)
        if out is False:
            return False

    if len(parenStack) == 0:
        print("Equal")


def checkForParens(paren, parenStack):
    if paren == "{":
        parenStack.append("{")
    elif paren == "[":
        parenStack.append("[")
    elif paren == "(":
        parenStack.append("(")
    elif paren == "}":
        if len(parenStack) == 0 or parenStack.pop() != "{":
            print("Unequal {")
            return False
    elif paren == "]":
        if len(parenStack) == 0 or parenStack.pop() != "[":
            print("Unequal [")
            return False
    elif paren == ")":
        if len(parenStack) == 0 or parenStack.pop() != "(":
            print("Unequal (")
            return False


checkForBalance(")(")