# Runtime: 69 ms
#假设一个有m个元素的序列pn，其下一个较大序列为pn+1。
#1) 若pn最右端的2个元素构成一个增序子序列，那么直接反转这2个元素使该子序列成为减序，即可得到pn+1。
#2) 若pn最右端一共有连续的s个元素构成一个减序子序列，令i = m - s，则有pn(i) < pn(i+1)，
#其中pn(i)表示排列pn的第i个元素。例如pn=<1 2 5 4 3>，那么pn的右端最多有3个元素构成一个减序子集<5 4 3>，
#i=5-3=2，则有pn(i)=2 < 5=pn(i+1)。因此若将pn(i)和其右边的子集s {pn(i+1), pn(i+2), ..., pn(m)}
#中任意一个元素调换必能得到一个较大的序列（不一定是下一个）。要保证是下一个较大的序列，必须保持pn(i)左边的元素不动，
#并在子集s {pn(i+1), pn(i+2), ..., pn(m)}中找出所有比pn(i)大的元素中最小的一个pn(j)，即不存在pn(k) ∈ s
#且pn(i) < pn(k) < pn(j)，然后将二者调换位置。现在只要使新子集{pn(i+1), pn(i+2), ..., pn(i), ...,pn(m)}成为
#最小序列即得到pn+1。注意到新子集仍保持减序，那么此时直接将其反转即可得到pn+1 {pn(1), pn(2), ..., pn(j), pn(m),
# pn(m-1), ..., pn(i), ..., pn(i+2), pn(i+1)}。
class Solution(object):
    def nextPermutation(self, nums):
    	m ,N= 1,len(nums)
    	if N <= 1:
    		return 
    	for i in range(N-1,0,-1):
    		if nums[i-1] >= nums[i]:
    			m += 1
    		else:
    			break
    	if m == N:
    		nums.reverse()
    		return
    	for j in range(N-m,N):
    		if nums[j] > nums[N-m -1]:
    			j += 1
    		else:
    			break
    	nums[j-1],nums[N-m-1] = nums[N-m-1],nums[j-1]
    	nums[N-m:] = list(reversed(nums[N-m:]))
solver = Solution()
a = [3,2,1]
print(solver.nextPermutation(a))

