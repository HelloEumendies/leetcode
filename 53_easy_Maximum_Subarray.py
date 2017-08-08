#Runtime: 55 ms
class Solution(object):
	def maxSubArray(self,nums):
		maxSum,curSum = -2147483648,0
		for i in range(len(nums)):
			curSum += nums[i]
			if curSum > maxSum:
				maxSum = curSum
			if curSum < 0:
				curSum = 0
		return maxSum	
nums = [-2,-3]
s = Solution()
print(s.maxSubArray(nums))			