#Runtime: 78 ms
class Solution(object):
    def isValidBST(self, root):
    	if root == None or (root.left==None and root.right==None):
    		return True
    	INT_MIN ,INT_MAX = -2147483649,2147483648
    	return self.valid(root.left,INT_MIN,root.val) & self.valid(root.right,root.val,INT_MAX)
   
    def valid(self,root,min,max):
    	if root == None:
    		return True
    	if root.val > min and root.val<max:
    		return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)
    	else:
    		return False