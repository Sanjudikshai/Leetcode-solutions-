class Solution:
    def reverse(self, x: int) -> int:
        x_val = abs(x)
        str_x = str(x_val)
        strn = str_x[::-1]
        num = int(strn)
        if x < 0:
            num = -num
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num 