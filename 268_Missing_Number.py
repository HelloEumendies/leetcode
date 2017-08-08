#Runtime: 122 ms
class Solution(object):
    def missingNumber(self, nums):
    	i = 0
    	while i < len(nums):
    		if  nums[i]  < len(nums) and nums[i] != nums[nums[i]]:
    			self.swap(nums,i,nums[i]) 		
    		else:
    			i += 1
    	for i in range(len(nums)):
    			if i != nums[i]:
    				return i
    	return len(nums)     
    def swap(self,A,x,y):
    	t = A[x]
    	A[x] = A[y]
    	A[y] = t