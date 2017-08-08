#319 ms
class Solution(object):
    def isPalindrome(self, x):
    	if x < 0:
    		return False
    	x = str(x)
    	for i in range(len(x)//2):
    		if x[i] != x[len(x)-1-i]:
    			return False
    	return True
x = -22222
s = Solution()
print(s.isPalindrome(x))

