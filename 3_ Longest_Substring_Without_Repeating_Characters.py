#Approach 1  Sliding Window
class Solution(object):
	def lengthOfLongestSubstring(self,s):
		hashSet = set()
		ans,i,j = 0,0,0
		while i<len(s) and j < len(s):
			if s[j] not in hashSet:
				hashSet.add(s[j])
				j += 1
				ans = max(ans,j-i)
			else:
				hashSet.remove(s[i])
				i += 1
		return ans

#Approach 2 Sliding Window Optimized
class Solution(object):
	def lengthOfLongestSubstring(self,s):
		hashDict ,ans ,i = {},0,0
		for j ,ch in enumerate(s):
			if ch in hashDict.keys():
				ans = max(ans,j-i)
				i = max(i,hashDict[ch] + 1)
			hashDict[ch] = j
		return max(ans,len(s)-i)
		
obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
