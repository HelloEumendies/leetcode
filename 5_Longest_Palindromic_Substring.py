#Runtime: 6976 ms
class Solution(object):
    def longestPalindrome(self, s):
    	if len(s) <= 1:
    		return s
    	count = 0
    	for i in range(1,len(s)):
    		if s[i] == s[i-1]:
    			count += 1
    	if count == len(s) - 1:
    		return s
    	dp = [[False for i in range(len(s))] for j in range(len(s))]
    	for i in range(len(s)):
    		for j in range(i,len(s)):
    			dp[j][i] = True
    	maxLen = 1
    	left,right = 0,0
    	for k in range(1,len(s)):
    		i = 0
    		while k + i < len(s):
    			j = i + k
    			if s[i] != s[j]:
    				dp[i][j] = False
    			else:
    				dp[i][j] = dp[i+1][j-1]
    				if dp[i][j]:
    					if k + 1 > maxLen:
    						maxLen = k +1
    						left = i
    						right = j
    			i += 1
    	return s[left:right+1]
s = "ffffffffffffffffffffffffffffffff"
so = Solution()
print(so.longestPalindrome(s))


