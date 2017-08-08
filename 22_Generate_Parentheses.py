#Runtime: 48 ms
import copy
class Solution(object):
    def generateParenthesis(self, n):
    	if n == 1:
    		return ["()"]
    	else:
    		res = self.generateParenthesis(n-1)
    		R = copy.deepcopy(res)
    		res = []
    		for exp in R:
    			for i in range(0,len(exp) + 1):
    				temp = exp
    				temp = temp[:i] + "()" + temp[i:]
    				res.append(temp)
    		res = list(set(res))
    		return res
s = Solution()
print(s.generateParenthesis(3))

