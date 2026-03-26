class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


        """
        for i in s:
            if i in t:
                return True
            else:
                return False
                """
                #passed 2nd testcase
"""
        a=''
        b=''
        for i in s:
            a+=i
        for j in t:
            b+=j
        return a==b
        """
        #passed 1st testcase
        