class Solution:
    def findMissingAndRepeatedValues(self, grid):
        s=[]
        ans=[]
        actualSum=0
        print(len(grid))
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in s:
                    ans.append(grid[i][j])
                actualSum+=grid[i][j]
                s.append(grid[i][j])
        expSum=len(grid)**2 * (len(grid)**2+1)//2
        print(expSum,actualSum,ans[0])
        b=expSum+ans[0]-actualSum
        ans.append(b)
        print(ans)



                
        


ans=Solution()
ans.findMissingAndRepeatedValues([[9,1,7],[8,7,2],[3,4,6]])
