#65 ms
class Solution(object):
    def strStr(self, haystack, needle):
    	len1,len2 = len(needle),len(haystack)
    	if len1 == 0 :
    		return 0
    	if len1 and len2 and len2 >= len1:
    		for i in range(len2-len1+1):
    			if haystack[i:i+len1] == needle:
    				return i
    	return -1
needle = "a"
haystack = "aaa"
s = Solution()
print(s.strStr(haystack,needle))