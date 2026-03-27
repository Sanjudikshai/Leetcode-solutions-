class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                t1 = s[i+1:len(s)-i]
                t2 = s[i:len(s)-1-i]
                return t1 == t1[::-1] or t2 == t2[::-1]
        return True


"""while l < r:
            if s[l] != s[r]:
                return self.check(s, l+1, r) or self.check(s, l, r-1)
            l += 1
            r -= 1
        return True"""
"""def check(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True"""
        
        