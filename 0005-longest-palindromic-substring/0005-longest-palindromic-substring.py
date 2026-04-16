class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]
        return Max_Str


        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return s[l+1:r]
        # result = ""
        # for i in range(len(s)):
        #     p1 = expand(i, i)
        #     p2 = expand(i, i+1)
        #     longer = p1 if len(p1) > len(p2) else p2
        #     if len(longer) > len(result):
        #         result = longer
        # return result