#Runtime: 219 ms
class Solution(object):
    def convert(self, s, numRows):
    	if numRows == 1 or len(s) < 2:
    		return s
    	res = ""
    	for i in range(numRows):
    		for j in range(i,len(s),2*(numRows-1)):
    			res += res.join(s[j])
    			if i > 0  and i<numRows - 1:
    				if j + 2*(numRows-i-1) < len(s):
    					res += res.join(s[j+2*(numRows-i-1)])
    	return res
