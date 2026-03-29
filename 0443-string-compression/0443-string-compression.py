class Solution:
    def compress(self, chars: List[str]) -> int:
        i = s = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[s] = chars[i]; s += 1
            if j - i > 1:
                for c in str(j-i):
                    chars[s] = c; s += 1
            i = j
        return s
        