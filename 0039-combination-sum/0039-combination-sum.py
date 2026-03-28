class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, current, total):
            
            # base case 1
            if total == target: return  result.append(current)  
            # base case 2
            
            if total > target or i >= len(candidates):
                return

            # -------- RECURSION STARTS HERE --------
            # choose the number
            dfs(i, current + [candidates[i]], total + candidates[i])
            # skip the number
            dfs(i + 1, current, total)
            # -------- RECURSION ENDS HERE ----------

        dfs(0, [], 0)
        return result



# Variable	Meaning
# i	        current index in candidates
# current     numbers chosen so far
# total	    sum of chosen numbers 


        