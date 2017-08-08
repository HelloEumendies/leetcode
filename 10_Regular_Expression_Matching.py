class Solution(object):
    def isMatch(self, s, p):
        if p == '.*':
            return True
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return True if p[0]== '.'and len(s) == 1 else (len(s)==1 and s[0]==p[0])
        if p[1] != '*':
            return False if len(s) == 0 or (p[0] != '.' and  p[0]!=s[0]) else  self.isMatch(s[1:],p[1:])
        else:
            index,length = -1,len(s)
            while  index <length and (index < 0 or p[0]=='.' or s[index] == p[0]):
                if self.isMatch(s[index +1:],p[2:]):
                    return True
                index += 1
        return False
solver = Solution()
s ,p = 'aa','a*'
print(solver.isMatch(s,p))
