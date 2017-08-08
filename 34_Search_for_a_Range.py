#Runtime: 42 ms
class Solution(object):
    def searchRange(self, nums, target):
    	pos = self.naiveSearch(nums,target)
    	if pos != -1:
    		left = self.leftBound(nums[:pos+1],target)
    		right = self.rightBound(nums[pos:],target)
    		return[left,pos+right]
    	else:
    		return [-1,-1]	
    def naiveSearch(self,nums,target):
    	if len(nums) == 0:
    		return -1
    	left,right = 0,len(nums) -1
    	while left <= right:
    		mid = (left + right) // 2
    		if nums[mid] == target:
    			return mid
    		elif target < nums[mid]:
    			right = mid - 1
    		else:
    			left = mid + 1
    	return -1
    def leftBound(self,nums,target):
    	if len(nums) == 1:
    		return 0
    	left,right = 0,len(nums) -1
    	while left <= right:
    		mid = (left +right) //2
    		if left == right :
    			return left
    		if nums[mid] == target:
    			right = mid
    		else: 
    			left = mid + 1
    def rightBound(self,nums,target):
    	if len(nums) == 1:
    		return 0
    	if nums[-1] == target:
    		return len(nums) - 1
    	left,right = 0,len(nums) -1 
    	while  left <= right:
    		mid = (left + right) //2
    		if right - left == 0:
    			return left 
    		if right - left == 1:
    			if nums[right] != target:
    				return left
    			else:
    				return right 
    		if nums[mid] == target:
    			left = mid
    		else:
    			right = mid - 1 
s = Solution()
a = [3,3,4,5,9]
print(s.rightBound(a,3))