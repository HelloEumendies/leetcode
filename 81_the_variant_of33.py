#Runtime: 69 ms
class Solution(object):
    def search(self, nums, target):
    	if len(nums) <= 0:
    		return False
    	left ,right = 0,len(nums) - 1
    	while left <= right:
    		mid = (left + right) // 2
    		if nums[mid] == target:
    			return True
    		elif nums[left] == nums[mid] and nums[mid] == nums[right]:
    			right -= 1
    			left += 1
    		elif nums[mid] <= nums[right]:
    			if nums[mid] <= target and target <= nums[right]:
    				left = mid + 1
    			else:
    				right = mid - 1
    		else:
    			if nums[left] <= target and target <= nums[mid]:
    				right = mid - 1
    			else:
    				left = mid + 1
    	return False 
s = Solution()
nums = [3,1,1]
print(s.search(nums,3))