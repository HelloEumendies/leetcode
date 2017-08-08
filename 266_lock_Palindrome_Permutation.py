class Solution(object):
	def palindromePermutation(self,s):
		char_count = {}
		unique_str = list(set(s))
		for ch in unique_str:
			char_count[ch] = s.count(ch)
		odd_count ,even_count = 0,0
		for val in char_count.values():
				if val % 2 :
					odd_count += 1
		if len(s) % 2:
			return True if odd_count == 1 else False
		else:
			return True if odd_count == 0 else False
solver = Solution()
s = "carerac"
print(solver.palindromePermutation(s))