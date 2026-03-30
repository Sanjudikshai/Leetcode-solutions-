class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def bt(s, path, rem):
            if rem == 0:
                res.append(path)
                return
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i-1]: continue
                if candidates[i] > rem: break
                bt(i+1, path+[candidates[i]], rem-candidates[i])
        bt(0, [], target)
        return res

        