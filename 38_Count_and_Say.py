#Runtime: 39 ms
class Solution(object):
    def countAndSay(self, n):
    	if n == 1:
    		return str(1)
    	last_str = self.countAndSay(n - 1) + "*"
    	cur_str = ""
    	count = 1 
    	for i in range(len(last_str)-1):
    		if last_str[i] == last_str[i + 1]:
    			count += 1
    		else:
    			cur_str = cur_str + str(count) + last_str[i]
    			count = 1
    	return cur_str
s = Solution()
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(9))