#Runtime: 59 ms
class Solution(object):
    def search(self, nums, target):
    	if len(nums) <= 0:
    		return -1
    	left,right = 0,len(nums) - 1
    	while left <= right:
    		mid = (left + right) // 2
    		if nums[mid] == target:
    			return mid
    		elif nums[mid] < nums[right]:
    			if nums[mid] <= target and nums[right] >= target:
    				left = mid + 1
    			else:
    				right = mid - 1
    		else:
    			if nums[left] <= target and target <= nums[mid]:
    				right = mid - 1
    			else:
    				left = mid  + 1
    	return -1
s = Solution()
nums = [1,3]
print(s.search(nums,3))