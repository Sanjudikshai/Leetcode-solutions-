class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def solve(i, path):
            if i == len(digits):
                res.append(path)
                return
            for ch in nums[digits[i]]:
                solve(i + 1, path + ch)
        solve(0, "")
        return res

        