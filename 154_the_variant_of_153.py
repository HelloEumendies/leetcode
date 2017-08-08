#Runtime:  55ms
class Solution(object):
    def findMin(self, nums):
    	if len(nums) == 0:
    		return None
    	left,right = 0,len(nums) - 1
    	while  left <= right:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            if right-left > 1 and nums[mid] == nums[left] and nums[mid] == nums[right]:
                left +=1 
                right -= 1
            elif nums[mid] <= nums[right]:
                if nums[mid] > nums[left]:
                    return nums[left]
                else:
                    right = mid 
            else:
                left = mid + 1
s = Solution()
a = [1,1]
print(s.findMin(a))