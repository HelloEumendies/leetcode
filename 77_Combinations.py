#289 ms
class Solution(object):
    def combine(self, n, k):
    	if n == k:
    		return [[i for i in range(1,n+1)]]
    	if   n >2 and k > n//2:
    		res ,source_set = [],[i for i in range(1,n+1)]
    		complementary_set = self.combine(n,n-k) 
    		for complement in complementary_set:
    			 res.append(list(set(source_set).difference(set(complement))))
    		return res
    	else:
    		return self.C_n_k([i for i in range(1,n+1)],k)
    def C_n_k(self,s,k):
   		if k == 1:
   			return [[i] for i in s]
   		else:
   			res = []
   			for i in range(len(s)):
   				for per in self.C_n_k(s[i+1:],k-1):
   					per.insert(0,s[i])
   					res.append(per)
   		return res
s= Solution()
print(s.combine(20,16))