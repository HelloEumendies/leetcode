#Runtime :35 ms
class Solution(object):
    def letterCombinations(self, digits):
    	dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    	res = []
    	if len(digits) == 0:
    		return res
    	elif len(digits) == 1:
    		return [str(x) for x in dic[digits[0]]]
    	else:
    		last = self.letterCombinations(digits[1:])
    		for x in dic[digits[0]]:
    			for y in last:
    				res.append(str(x) + y)
    		return res    
s = Solution()
a = "347"
print(s.letterCombinations(a))