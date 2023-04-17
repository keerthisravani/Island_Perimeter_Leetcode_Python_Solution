def islandPerimeter(grid):
    count=0
    cl=len(grid[0])
    rl=len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                    if i==0 :
                        count+=1
                    if j==0:
                        count+=1
                    if i==rl-1:
                        count+=1
                    if j==cl-1:
                        count+=1
                        #uoward
                    if i>0 and grid[i-1][j]==0:
                            count+=1
                        #downward
                    if i<(rl-1) and grid[i+1][j] ==0:
                        count+=1
                        #left
                    if j>0 and grid[i][j-1]==0:
                        count+=1
                    if j<(cl-1) and grid[i][j+1]==0:
                        count+=1
        
    return count
grid=[[0,1,0,1,0],[1,0,0,1,0],[1,1,1,0,0]]   
print(islandPerimeter(grid))               

                        







    