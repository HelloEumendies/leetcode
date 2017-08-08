#Runtime: 65 ms
class Solution(object):
    def findDuplicate(self, nums):
    	low, high= 1,len(nums) - 1
    	while low < high:
    		mid = low + (high - low) // 2
    		count = 0
    		for i in nums:
    			if i<=mid:
    				count += 1
    		if count <= mid:
    			low = mid + 1
    		else:
    			high = mid
    	return low		
s = Solution()
a = [1,1,2,3,4]
print(s.findDuplicate(a))