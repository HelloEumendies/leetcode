# import math
# class Solution(object):
#     def getPermutation(self, n, k):
#     	if n==1 :
#     		return str(n)
#     	nums = [i for i in range(1,n+1)]
#     	groupIndex = math.ceil(k/math.factorial(n-1))
#     	first = nums[int(groupIndex - 1)]
#     	ans = [first]
#     	nums.remove(first)
#     	k -= math.factorial(n-1) * (groupIndex - 1)
#     	theRest = self.getKthPerm(nums,k)
#     	ans.extend(theRest)
#     	strAns = "".join([str(x) for x in ans])
#     	return strAns 
#     def getKthPerm(self,nums,k):
#     	n = len(nums)
#     	if n == 1:
#     		return nums
#     	res = []
#     	groupIndex = math.ceil(k/math.factorial(n-1))
#     	first = nums[int(groupIndex - 1)]  
#     	res.append(first)
#     	nums.remove(first)
#     	k -= math.factorial(n-1) * (groupIndex - 1)
#     	rest = self.getKthPerm(nums,k)
#     	res.extend(rest)
#     	return res
#Runtime: 46 ms
import math
class Solution(object):
    def getPermutation(self, n, k):
        nums = [x for x in range(1,n+1)]
        perm = ''
        k -= 1
        while n > 0:
        	index,k = divmod(k,math.factorial(n-1))
        	n -= 1
        	perm += str(nums[index])
        	nums.remove(nums[index])
        return perm
s = Solution()
print(s.getPermutation(2,1))