#Runtime: 39 ms
class Solution(object):
    def findMin(self, nums):
    	if len(nums) == 0:
    		return None
    	left,right = 0,len(nums) - 1
    	while  left <= right:
    		if left == right:
    			return nums[left]
    		mid = (left + right) // 2
    		if nums[mid] < nums[right]:
    			if nums[mid] > nums[left]:
    				return nums[left]
    			else:
    				right = mid 
    		else:
    			left = mid + 1
s = Solution()
a = [5,6,7,8,9,10,1,2,3,4]
 
print(s.findMin(a))
 