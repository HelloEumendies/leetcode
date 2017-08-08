# solution one
# class Solution(object):
# 	def threeSumClosest(self,nums,target):
# 		nums.sort()
# 		N = len(nums)
# 		ans = None
# 		for i in range(N):
# 			l,r = i+1,N-1
# 			while l < r:
# 				s = nums[i] + nums[l] + nums[r]
# 				if ans is None or abs(s - target) < abs(ans - target):
# 					ans = s
# 				if s <= target:
# 					l += 1
# 				else:
# 					r -= 1
# 		return ans
#solution two ,a little faster than soultion one
class Solution(object):
	def threeSumClosest(self,nums,target):
		nums.sort()
		N = len(nums)
		ans = nums[0] + nums[1] +nums[2]
		for i in range(N):
			l,r = i+1,N-1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if  abs(s - target) < abs(ans - target):
					ans = s
				if s <= target:
					l += 1
				else:
					r -= 1
		return ans
nums = [-1,2,1,-4]
target = 1
obj = Solution()
print(obj.threeSumClosest(nums,target))

