#Runtime: 89 ms
import copy
class Solution(object):
    def subsetsWithDup(self, nums):
    	R = self.subsets(sorted(nums))
    	RR = []
    	for r in R:
    		if r not in RR:
    			RR.append(r) 
    	return RR
    def subsets(self,nums):
    	res = []
    	if len(nums) == 0:
    		return res
    	if len(nums) == 1:
    		return [[],nums]
    	else: 
    		last = nums[-1]
    		res = self.subsets(nums[:len(nums)-1])
    		R = copy.deepcopy(res)
    		for x in res:
    			x.append(last)
    			R.append(x)
    		return R
s = Solution()
nums = [4,4,4,1,4]
print(s.subsetsWithDup(nums))