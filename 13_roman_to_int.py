#139 ms
class Solution(object):
    def romanToInt(self, s):
    	val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    	key = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    	i,res = 0 ,0
    	while i < len(s):
    		if s[i] == 'C':
    			if i + 1 < len(s) and s[i+1] == 'M':
    				res += 900
    				i += 2
    			elif i + 1 < len(s) and s[i+1] == 'D':
    				res += 400
    				i += 2
    			else:
    				res += 100
    				i += 1
    		elif s[i] == 'X':
    			if i + 1 < len(s) and s[i+1] == 'C':
    				res += 90
    				i += 2
    			elif i + 1 < len(s) and s[i+1] == 'L':
    				res += 40
    				i += 2
    			else:
    				res += 10
    				i += 1
    		elif s[i] == 'I':
    			if i + 1 < len(s) and s[i+1] == 'X':
    				res += 9
    				i += 2
    			elif i + 1 < len(s) and s[i+1] == 'V':
    				res += 4
    				i += 2
    			else:
    				res += 1
    				i += 1
    		else:
    			res += val[key.index(s[i])]
    			i += 1
    	return res
s = Solution()
print(s.romanToInt('DCCCLXVIII')) 
