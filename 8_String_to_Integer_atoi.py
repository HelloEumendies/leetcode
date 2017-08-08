#69 ms
class Solution(object):
    def myAtoi(self, str):
    	if len(str) == 0:
    		return 0
    	INT_MAX ,INT_MIN = 2147483647,-2147483648 
    	sign ,res ,i = 1,0,0
    	while str[i] == ' ':
    		i += 1
    	if str[i] == '-' or str[i] == '+':
    		sign = 1 - 2*(str[i] == '-')
    		i += 1
    	while i < len(str) and str[i] >='0' and str[i] <= '9' :
    		if res > INT_MAX // 10 or (res == INT_MAX // 10 and str[i] > '7'):
    			return INT_MAX if sign == 1 else INT_MIN
    		res = 10 * res + int(str[i])
    		i += 1
    	return res * sign
s = Solution()
a = "1"
print(s.myAtoi(a))
