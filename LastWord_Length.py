class LastWord_length:
    def lengthOfLastWord(self, s):
        y = s.rstrip();
        count = 0;
        for i in reversed(y):
            if i != " ":
                count = count + 1
            else:
                return count;

        return count;



s = "             fly me   to   the moon  ";
obj = LastWord_length();
obj.lengthOfLastWord(s);