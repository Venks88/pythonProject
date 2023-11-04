class Roman_letter:
    def romanLetter(self, s: int) -> int:
        sumList = [];
        listRoman = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000,
                     "IV": 4,
                     "IX": 9,
                     "XL": 40,
                     "XC": 90,
                     "CD": 400,
                     "CM": 900}
        stringOfX = str(s);
        while len(stringOfX) > 0:
            inp1 = stringOfX[:1];
            inp2 = stringOfX[:2];

            if inp2 == "IV" or inp2 == "IX" or inp2 == "XL" or inp2 == "XC" or inp2 == "CD" or inp2 == "CM":
                out = listRoman.get(inp2);
                sumList.append(out);
                stringOfX = stringOfX[2:];
            else:
                out = listRoman.get(inp1);
                sumList.append(out);
                stringOfX = stringOfX[1:];

        return sum(sumList);

obj = Roman_letter();
obj.romanLetter("LVIII");