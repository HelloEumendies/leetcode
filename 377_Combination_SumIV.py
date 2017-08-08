#Runtime: 56 ms
class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]
        return dp[target]	 
a = [1,2,3]
s = Solution()
print(s.combinationSum4(a,4))
