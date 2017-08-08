#Runtime: 382 ms
from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
    	if len(heightMap) == 0 :
    		return 0
    	m = len(heightMap)
    	n = len(heightMap[0]) if len(heightMap[0]) > 0 else 0
    	visited = [[False for i in range(n)] for j in range(m)]
    	priorty_queue = []
    	ans,mx = 0,-1
    	for i in range(m):
    		for j in range(n):
    			if i == 0 or i == m-1 or j == 0 or j == n-1:
    				heappush(priorty_queue,(heightMap[i][j],i,j))
    				visited[i][j] = True
    	direction = [[0,-1],[0,1],[-1,0],[1,0]] 
    	while  len(priorty_queue) :
    		curr = heappop(priorty_queue)
    		mx = max(mx,curr[0])
    		for k in range(len(direction)):
    			nx = curr[1] + direction[k][0]
    			ny = curr[2] + direction[k][1]
    			if nx < 0 or nx >= m or ny<0 or ny >= n or visited[nx][ny]:
    				continue
    			visited[nx][ny] = True
    			if heightMap[nx][ny] < mx:
    				ans += (mx - heightMap[nx][ny])
    			heappush(priorty_queue,(heightMap[nx][ny],nx,ny))
    	return ans
h = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

s = Solution()
print(s.trapRainWater(h))
