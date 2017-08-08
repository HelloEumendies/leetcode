#Runtime: 42 ms
class Solution(object):
    def searchInsert(self, nums, target):
    	if len(nums) == 0 or target < nums[0]:
    		return 0
    	if target > nums[-1]:
    		return len(nums)
    	i,j = 0,len(nums) - 1
    	while i <= j:
    		m = (i + j) // 2
    		if j - i == 1 and target > nums[i]:
    			return j
    		if nums[m] == target:
    			return m
    		elif target < nums[m]:
    			j = m 
    		else:
    			i = m 
a = [1,3] 
 
s = Solution()
print(s.searchInsert(a,1))
 