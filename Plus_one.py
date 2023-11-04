class Plus_one:
    def plusone(self, digits):
        numAsString = "";
        for i in digits:
            numAsString = numAsString+str(i);

        numAsInt = int(numAsString);
        numAsInt = numAsInt + 1;

        numAsString = str(numAsInt);
        lister = []
        for j in numAsString:
            lister.append(int(j));

        return lister;

obj = Plus_one();
digits = [1,2,3];
obj.plusone(digits);