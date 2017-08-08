#Runtime: 69 ms
class Solution(object):
    def firstMissingPositive(self, nums):
    	i = 0
    	while i < len(nums):
    		if nums[i]>0 and nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1]:
    			self.swap(nums,i,nums[i]-1) 		
    		else:
    			i += 1
    	for i in range(len(nums)):
    			if i+1 != nums[i]:
    				return i+1
    	return len(nums) + 1    
    def swap(self,A,x,y):
    	t = A[x]
    	A[x] = A[y]
    	A[y] = t				
s = Solution()
a = [3,4,-1,1]
print(s.firstMissingPositive(a))
