#Solution one ,Time Limit Exceeded
# class Solution(object):
# 	def threeSum(self,nums):
# 		hash = {}
# 		result = []
# 		for i in range(len(nums)):
# 			hash[nums[i]] = i
# 		for i in range(len(nums)):
# 			for j in range(i+1,len(nums)):
# 				t = 0-nums[i]-nums[j]
# 				if t in hash and j != hash[t] and i!=hash[t]:
# 					result.append(sorted([nums[i],nums[j],t]))
# 		result = sorted(result)
# 		rr = []
# 		for i in range(len(result)):
# 			if result[i] not in rr:
# 				rr.append(result[i])
# 		return rr
#Solution two,the key point is avoid Duplicate removal  operating 
class Solution(object):
	def threeSum(self,nums):
		nums.sort()
		res = []
		n = len(nums)
		for i in range(0,n-2):
			if i and nums[i] == nums[i-1]:
				continue
			left ,right = i+1,n-1
			while left < right:
				s = nums[i] + nums[left] + nums[right]
				if s < 0:
					left += 1
				elif s > 0:
					right -= 1
				else:
					res.append([nums[i],nums[left],nums[right]])
					right -= 1
					left += 1
					while left < right and nums[left] == nums[left-1]:
						left += 1
					while left < right and nums[right] == nums[right + 1]:
						right -= 1
		return res
a=[-1,0,1,2,-1,4]
s=Solution()
print(s.threeSum(a))
