class Solution:

    #time complexity:log(m*n)
    def searchMatrix(self, matrix, target):
        result=False
        for i in matrix:
            for j in i:
                if j ==target:
                    result=True
        return result


s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],0))
        