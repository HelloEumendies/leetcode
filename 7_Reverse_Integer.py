#Runtime: 82 ms
class Solution(object):
    def reverse(self, x):
    	maxInt = 2 ** 31 - 1
    	strX,res = str(x),""
    	flag = True
    	if strX[0] == '-':
    		strX = strX[1:]
    		flag = False
    	for i in range(len(strX)-1,-1,-1):
    		res += strX[i]
    	if int(res) > maxInt:
    		return 0
    	return int(res) if flag else 0-int(res)
s=Solution()
a= 1000000003
print(s.reverse(a))