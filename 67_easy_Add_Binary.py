#82 ms
class Solution(object):
    def addBinary(self, a, b):
    	if len(a) < len(b):
    		a ,b = b,a
    	res ,R= [],""
    	i , j = len(a)-1,len(b) - 1
    	carry = 0
    	while j >=0:
    		carry,t1 = divmod(int(a[i])+int(b[j])+carry,2)
    		res.insert(0,t1);i -= 1;j -= 1
    	for index in range(i-j-1,-1,-1):
    		carry,t2 = divmod(int(a[index]) + carry,2)		
    		res.insert(0,t2);i -= 1
    	if carry > 0:
    		res.insert(0,1)
    	for x in res:
    		R += str(x)
    	return R
s = Solution()
a ,b = "11","1"
print(s.addBinary(a,b))


