class Solution(object):
    def plusOne(self, digits):
    	if digits[0] == 0:
    		return [digits[0] + 1]
    	elif digits[-1]  <9:
    		digits[-1] += 1
    		return digits
    	else:
    		carry = 1
    		for i in range(len(digits)-1,-1,-1):
    			carry,digits[i] = divmod((digits[i] + carry) , 10)
    		if carry ==1:
    			digits.insert(0,1)
    		return digits
s = Solution()
digits = [0]
print(s.plusOne(digits))