class Add_Binary:
    def addBinary(self, a, b):
        a = ascii(a);
        b = ascii(b);
        su = a+b;
        return bin(su);

obj = Add_Binary();
a = "1010";
b = "1011";
obj.addBinary(a,b);