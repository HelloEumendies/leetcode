# 39 ms
class Solution(object):
    def longestCommonPrefix(self, strs):
    	if len(strs) == 0 :
    		return ""
    	if len(strs) == 1:
    		return strs[0]
    	prefix = ""
    	strs.sort(key=lambda x :len(x))
    	for i in range(len(strs[0])):
    		prefix = strs[0][:i+1]
    		for j in range(1,len(strs)):
    			if strs[j][:i+1] == prefix:
    				continue
    			else:
    				if i == 0:
    					return ""
    				else:
    					return prefix[:len(prefix)-1]
    	return prefix
s = Solution()
strs = ["aaa","aaac","aaadc"]
print(s.longestCommonPrefix(strs))

    