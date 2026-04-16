class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        str_x = str(abs_x)
        reversed_str = str_x[::-1]
        reversed_num = int(reversed_str)
        if x < 0:
            reversed_num = -reversed_num
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num 