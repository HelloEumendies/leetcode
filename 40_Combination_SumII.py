#Runtime:  89 ms  
class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        t = []
        for x  in result: 
            if x not in t:
                t.append(x)
        return t
    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1
a = [1,1,2,5,6,7,10]
s = Solution()
print(s.combinationSum2(a,8))
