class Solution(object):
	def removeElement(self,nums,val):
		N = len(nums)
		j = 0
		for i in range(N):
			if nums[i] != val:
				nums[j] = nums[i]
				j += 1
		return j 
