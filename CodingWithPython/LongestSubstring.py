class Solution(object):
    def longestPalindrome(self, s):
        outlist = []
        # convert s to array
        sArray = list(s)

        while(len(sArray) >= 1):
            tempArray = sArray.copy()
            while(len(tempArray) >= 1):
                if self.isPalindrome(tempArray):
                    outlist.append("".join(tempArray))
                    break
                else:
                    tempArray.pop()
            sArray.pop(0)

        # get the max size of the list:
        outlist.sort(key=len, reverse=True)
        return outlist[0]

    def isPalindrome(self, str):
        revStr = list(str)
        revStr = revStr[::-1]
        revStr = "".join(revStr)

        if "".join(str) == revStr:
            return True
        return False


def main():
  sol = Solution();
  sol.longestPalindrome("babad")

main()



