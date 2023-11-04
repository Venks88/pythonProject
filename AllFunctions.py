def get_opn(operator):
    if operator == "+":
        def sumn(a,b):
            return a+b;
        return sumn
    elif operator == "-":
        def sums(a,b):
            return a-b;
        return sums
    else:
        print("Invalid Operator")


add_func = get_opn("+");
result = sumn(20, 30);