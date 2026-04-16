class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        if not num:
            return 0
        res = sign * int(num)
        return max(-2**31, min(2**31 - 1, res))