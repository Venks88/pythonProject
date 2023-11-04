class Palindrome_number:
    def palin(self, x: int) -> bool:
        stringOfX = str(x);
        if stringOfX[0] == "-":
            return False;

        revofX = "";
        for i in reversed(stringOfX):
            revofX = revofX+i;

        if x == int(revofX):
            return True;
        else:
            return False;


obj = Palindrome_number();
obj.palin(12121);
