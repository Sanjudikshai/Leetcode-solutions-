class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_count = Counter(s1)
        for i in range(len(s2) - k + 1):
             if Counter(s2[i:i+k]) == s1_count:
                return True
        return False  
        
        """
        n=len(s1)
        a=[0]*26
        b=[0]*26
        for i in range(n):
            if i < len(s2):
                a[ord(s1[i])-97] += 1
                b[ord(s2[i])-97] += 1 
            else:
                return 0
        if a == b:
            return True
        for i in range(n, len(s2)):
            b[ord(s2[i])-97] += 1
            b[ord(s2[i-n])-97] -= 1
            if a == b:
                return True
        else:
            return False
            """