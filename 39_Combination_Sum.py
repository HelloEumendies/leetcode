#105 ms
class Solution:
	def combinationSum(self, candidates, target):
		res,curAns = [],[]
		self.DFS(sorted(candidates),res,0,curAns,target)
		return res
	def DFS(self,candidates,res,start,curAns,target):
		if target == 0:
			res.append(list(curAns))
		while start < len(candidates) and candidates[start] <= target:
			curAns.append(candidates[start])
			self.DFS(candidates,res,start,curAns,target -candidates[start])
			curAns.pop()
			start += 1
s = Solution()
print(s.combinationSum([2,3,6,7],7))