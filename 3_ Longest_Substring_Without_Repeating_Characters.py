#Runtime: 99 ms
class Solution(object):
	def lengthOfLongestSubstring(self,s):
		dic,ans,start = {},0,0
		for i,ch in enumerate(s):
			if ch in dic:
				ans = max(ans,i-start)
				start = max(start,dic[ch] + 1)
			dic[ch] = i	
		return max(ans,len(s) - start)
s = "abcccc"
so = Solution()
print(so.lengthOfLongestSubstring(s))