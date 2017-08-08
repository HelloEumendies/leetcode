#Runtime: 46 ms
class Solution(object):
    def firstBadVersion(self, n):
    	if n==1:
    		return n
    	left ,right = 0,n
    	while left <= right:
    		if left == right:
    			return left
    		mid = (left + right) //2
    		if isBadVersion(mid):
    			right = mid
    		else:
    			left = mid + 1