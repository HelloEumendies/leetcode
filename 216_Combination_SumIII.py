#Runtime: 42 ms
class Solution(object):
    def combinationSum3(self, k, n):
    	nums = [i for i in range(1,10)]
    	temp_res = self.combinationSum2(nums,n)
    	res = []
    	for ans in temp_res:
    		if len(ans) == k:
    			res.append(ans)
    	return res
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result
    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                intermediate.append(candidates[start])
                self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
                intermediate.pop()
                prev = candidates[start]
            start += 1
s = Solution()
print(s.combinationSum3(2,18))