class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def part(i,p):  
            if i==len(s):
                res.append(p)
                return
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    part(j+1,p+[s[i:j+1]])
        
        part(0,[])
        return res