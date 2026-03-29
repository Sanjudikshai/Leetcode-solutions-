class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        n = len(part)
        for c in s:
            res.append(c)
            if ''.join(res[-n:]) == part:
                del res[-n:]
        return ''.join(res)
        