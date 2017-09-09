class Solution():
	def twoSum(self,nums,target):
		hash = {}
		for i,val in enumerate(nums):
			if target - val in hash.keys():
				return [hash[target - val],i]
			hash[val] = i
		return [-1,-1]
