#76 ms
class Solution(object):
    def isValid(self, s):
    	stack = []
    	i  = 0
    	bracket_dict = {']':'[','}':'{',')':'('}
    	while  i < len(s):
    		if s[i] in ['[','(','{']:	 
    			stack.append(s[i]) 
    			i += 1
    		else:
    			try:
    				if stack[-1] != bracket_dict[s[i]]:
    					return False
    				stack = stack[:len(stack)-1] 
    				i += 1
    			except :
    				return False
    	return len(stack) == 0
s = "["
so = Solution()
print(so.isValid(s))
