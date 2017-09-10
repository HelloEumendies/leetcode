#Approach 1
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
	#在a,b中寻找第K小的数，每次查找就需要对两个序列中的一个去除k/2个数    	
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

#Approach 2  
class Solution(object):
	def findMedianSortedArrays(self, a, b):
		if len(a) > len(b):
			a,b = b,a
		m,n = len(a),len(b)
		iMin,iMax ,halfLen = 0,m, (m+n+1) // 2
		while iMin <= iMax:
			i = (iMin+iMax) // 2
			j = halfLen - i
			if i < iMax and b[j-1] > a[i]:
				iMin = iMin + 1
			elif i > iMin and a[i-1] > b[j]:
				iMax = iMax - 1
			else:
				leftMax = 0
				if i == 0:
					leftMax = b[j-1]
				elif j ==0 :
					leftMax = a[i-1]
				else:
					leftMax = max(a[i-1],b[j-1]) 

				if (m+n)%2 == 1:
					return  leftMax * 1.0
				rightMin = 0
				if i == m:
					rightMin = b[j]
				elif j == n:
					rightMin = a[i]
				else:
					rightMin = min(a[i],b[j])
				return (leftMax + rightMin) /2.0
		return 0.0
