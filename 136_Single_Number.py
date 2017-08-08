# 52 ms XOR satisfies exchange law
class Solution(object):
    def singleNumber(self, nums):
    	result = 0
    	for i in range(len(nums)):
    		result ^= nums[i]
    	return result
s = Solution()
a = [1,3,1,4,3,5,4]
print(s.singleNumber(a))