class Longest_Common_Prefix:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        base = strs[0];
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i];

        return base;


obj = Longest_Common_Prefix();
strs = ["flower", "flow", "flight"];
obj.longestCommonPrefix(strs);