class Solution(object):
    def kth(self,a,b,k):
    	m, n= len(a),len(b)
    	if m > n:
    		a,b = b,a
    		m,n = n,m
    	if m == 0:
    		return b[k-1]
    	if k == 1:
    		return min(a[0],b[0])
    	pa = min(k//2,m)
    	pb = k - pa
    	if a[pa-1] < b[pb-1]:
    		return self.kth(a[pa:],b,k-pa)
    	elif a[pa-1] > b[pb-1]:
    		return self.kth(a,b[pb:],k-pb)
    	else:
    		return a[pa-1]
    def findMedianSortedArrays(self, a, b):
    	n = len(a) + len(b)
    	if n % 2 == 1:
    		return self.kth(a,b,n//2 + 1)
    	return (self.kth(a,b,n//2) + self.kth(a,b,n//2 + 1) )/ 2.