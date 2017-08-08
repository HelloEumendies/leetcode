#Solution one
# class Solution():
# 	def twoSum(self,nums,target):
# 		hash = {}
# 		for i in range(len(nums)):
# 			hash[nums[i]] = i
# 		for i in range(len(nums)):
# 			if target - nums[i] in hash and i != hash[target-nums[i]]:
# 				return [i,hash[target-nums[i]]]
# 		return [-1,-1]

#after optimization  run time just 69ms
# class Solution():
# 	def twoSum(self,nums,target):
# 		hash = {}
# 		for i in range(len(nums)):
# 			if target-nums[i] in hash:
# 				return[hash[target-nums[i]],i]
# 			hash[nums[i]] = i
# 		return[-1,-1]

#Solution two run time 1699ms
# class Solution():
# 	def twoSum(self,nums,target):
# 		for i in range(len(nums)):
# 			if target - nums[i] in nums and i!=nums.index(target-nums[i]): 
# 				if i < nums.index(target-nums[i]):
# 					return [i,nums.index(target-nums[i])]
# 				else:
# 					return [nums.index(target-nums[i]),i] 
# 		return [-1,-1]
s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))