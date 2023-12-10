def get_opn(operator, a,b):
    if operator == "+":
        def sumn():
            return a+b;
        return sumn
    elif operator == "-":
        def sums():
            return a-b;
        return sums
    else:
        print("Invalid Operator")


add_func = get_opn("+", 20, 30);