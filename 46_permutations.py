#Runtime: 69 ms
class Solution(object):
	def permute(self,nums):
 		if len(nums) <= 1:
 			return [nums]
 		result = []
 		for x in nums:
 			temp_list = nums[:]
 			temp_list.remove(x)
 			temp_perms = self.permute(temp_list)
 			for perm in temp_perms:
 				perm[0:0] = [x]
 				result.append(perm)
 		return result

a = [1,2,3]
solver = Solution()
print(solver.permute(a))

