#Runtime: 52 ms
class Solution(object):
	def maxArea(self,height):
		left,right  = 0,len(height) - 1
		res,tempRes = 0,0
		while left < right:
			if height[left] < height[right]:
				tempRes = (right - left) * height[left]
				if  tempRes > res:
					res = tempRes
				left += 1
			else:
				tempRes = (right - left) *height[right]
				if tempRes > res:
					res = tempRes
				right -= 1
		return res
