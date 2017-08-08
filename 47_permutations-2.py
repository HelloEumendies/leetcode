# Runtime: 126 ms
class Solution(object):
	def permuteUnique(self,nums):
		unique_nums = list(set(nums))
		result = []
		if len(nums) <= 1:
			return [nums]
		for x in unique_nums:
			temp_list = nums[:]
			temp_list.remove(x)
			temp_perms = self.permuteUnique(temp_list)
			for perm in temp_perms:
				perm[0:0] = [x]
				result.append(perm)
		return result	