# 1 Runtime: 988 ms
# class Solution(object):
# 	def fourSum(self,nums,target):
# 		nums.sort()
# 		res = []
# 		for i in range(len(nums)-3):
# 			if i and nums[i] == nums[i-1]:
# 				continue
# 			for j in range(i+1,len(nums)-2):
# 				if j>i+1 and nums[j] == nums[j-1]:
# 					continue
# 				left,right = j+1,len(nums)-1
# 				while left < right:
# 					s = nums[i]+nums[j]+nums[left]+nums[right]
# 					if s > target:
# 						right -= 1
# 					elif s < target:
# 						left += 1
# 					else:
# 						res.append([nums[i],nums[j],nums[left],nums[right]])
# 						left += 1
# 						right -= 1
# 						while left<right and nums[left] == nums[left-1]:
# 							left += 1
# 						while  left< right and nums[right] == nums[right+1]:
# 							right -= 1
# 		return res
# 2 Runtime: 119 ms
# class Solution(object):
# 	def fourSum(self,nums,target):
# 		res = []
# 		if len(nums) < 4 :
# 			return res 
# 		nums.sort()
# 		maxNum = nums[-1]
# 		if 4*nums[0]>target or 4*maxNum<target:
# 			return res
# 		for i in range(len(nums)):
# 			t = nums[i]
# 			if i>0 and t==nums[i-1]:
# 				continue
# 			if t + 3*maxNum < target:
# 				continue
# 			if 4*t > target:
# 				break
# 			if 4*t == target:
# 				if i+3<len(nums) and nums[i+3]==t:
# 					res.append([t,t,t,t])
# 					break
# 			self.threeSumForFourSum(nums,target-t,i+1,len(nums)-1,res,t) 
# 		return res
# 	def threeSumForFourSum(self,nums,target,low,high,res,t1):
# 		if low+1>=high:
# 			return
# 		maxSum = nums[high]
# 		if 3*nums[low]>target or 3*maxSum<target:
# 			return
# 		for i in range(low,high):
# 			t = nums[i]
# 			if i>low and t == nums[i-1]:
# 				continue
# 			if t + 2*maxSum<target:
# 				continue
# 			if 3*t>target:
# 				break
# 			if 3*t == target:
# 				if i+1 < high and nums[i+2] == t:
# 					res.append([t1,t,t,t])
# 				break
# 			self.twoSumForFourSum(nums,target-t,i+1,high,res,t1,t)
# 	def twoSumForFourSum(self,nums,target,low,high,res,t1,t2):
# 		if low>=high:
# 			return
# 		if 2*nums[low]>target or 2*nums[high]<target:
# 			return
# 		i,j = low,high
# 		while i < j:
# 			s = nums[i] + nums[j]
# 			if s == target:
# 				res.append([t1,t2,nums[i],nums[j]])
# 				while i<j and nums[i] == nums[i-1]:
# 					i += 1
# 				j -= 1
# 				while i<j and nums[j] == nums[j+1]:
# 					j -= 1
# 			elif s < target:
# 				i += 1
# 			else:
# 				j -= 1
# 		return 
s=[1, 0, -1, 0, -2, 2]
target = 0
obj=Solution()
print(obj.fourSum(s,target))


