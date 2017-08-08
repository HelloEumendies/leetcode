#Runtime: 369 ms
class Solution(object):
    def exist(self,board,word):
    	visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
    	for i in range(len(board)):
    		for j in range(len(board[i])):
    			if self.DFS(board,visited,i,j,word,0) :
    				return True
    	return False
    def DFS(self,board,visited,x,y,word,length):
    	if length == len(word):
    		return True
    	if x<0 or y<0 or x>=len(board) or y>=len(board[0])or visited[x][y] or board[x][y]!=word[length]:
    		return False	
    	visited[x][y] = True
    	if self.DFS(board,visited,x+1,y,word,length+1):return True
    	if self.DFS(board,visited,x-1,y,word,length+1):return True
    	if self.DFS(board,visited,x,y+1,word,length+1):return True
    	if self.DFS(board,visited,x,y-1,word,length+1):return True
    	visited[x][y] = False
    	return False
board = ["ab"]
S = Solution()
print(S.exist(board,"b"))