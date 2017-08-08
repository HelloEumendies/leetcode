class Solution(object):
    def lengthOfLastWord(self, s):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = s.strip()
        res = 0
        for i in range(len(s)-1,-1,-1):
        	if s[i] in chars:
        		res += 1
        	else:
        		return res        	
        return res 
s = Solution()
t = "b a ss"
print(s.lengthOfLastWord(t))