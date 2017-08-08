#Runtime: 65 ms
# class Solution(object):
#     def subsets(self, nums):
#     	res = [[]]
#     	start,end = [0] * len(nums),[1] * len(nums)
#     	while start != end:
#     	 	start = self.plusOne(start)
#     	 	all_one_pos = [i for i,x in enumerate(start) if x == 1]  
#     	 	res.append([nums[index] for index in all_one_pos])
#     	return res
#     def plusOne(self,pos):
#     	carry = 1
#     	for i in range(len(pos)-1,-1,-1):
#     		carry,pos[i] = divmod(pos[i]+carry,2)
#     	return pos

# Runtime: 82 ms
import copy
class Solution(object):
    def subsets(self, nums):
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
nums = [1,2,3]
print(s.subsets(nums))