# Runtime: 86 ms
# class Solution(object):
# 	def removeDuplicates(self,nums):
# 		N ,tail = len(nums),0
# 		if N <= 1:
# 			return N
# 		for i in range(1,N):
# 			if nums[i] != nums[i-1]:
# 				tail += 1
# 				nums[tail] = nums[i]
# 		return tail + 1
class Solution(object):
	def removeDuplicates(self,nums):
		N  ,res= len(nums),len(nums)
		if N <= 1:
			return N
		i = 0
		while i < N:
			j = i + 1
			while j < N and nums[j] == nums[i]:
				j += 1
			if j != i +1:
				res = res - (j-i-1)
				i = j
			else:
				i += 1
		return res 
nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicates(nums))
