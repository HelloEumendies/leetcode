#122 ms
class Solution(object):
    def intToRoman(self, num):
    	val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    	key = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    	res = ""
    	for i in range(len(val)):
    		if num >= val[i]:
    			count,num = divmod(num,val[i])
    			for j in range(count):
    				res += key[i]
    	return res		 
s = Solution()
print(s.intToRoman(868))