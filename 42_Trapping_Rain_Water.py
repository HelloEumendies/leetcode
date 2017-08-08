#One 314/315 test cases passed.Status: Time Limit Exceeded
# class Solution(object):
#     def trap(self, height):
#     	amount = 0
#     	n = len(height)
#     	if n==0:
#     		return 0
#     	maxH = max(height)
#     	for h in range(maxH):
#     		temp = 0
#     		for i in range(n):
#     			if height[i] >= h+1:
#     				break
#     		for j in range(n-1,-1,-1):
#     			if height[j] >= h+1:
#     				break
#     		for k in range(i,j+1):
#     			if height[k] >= h+1:
#     				temp += 1
#     		if j-i+1-temp > 0:
#     			amount += (j-i+1-temp)
#     	return amount

class Solution(object):
    def trap(self, height):
    	a,b = 0,len(height) - 1
    	leftMax,rightMax = 0,0
    	amount = 0
    	while a <= b:
    		leftMax = max(leftMax,height[a])
    		rightMax = max(rightMax,height[b])
    		if leftMax <= rightMax:
    			amount += (leftMax - height[a])
    			a += 1
    		else:
    			amount +=(rightMax - height[b])
    			b -= 1
    	return amount
h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(h))