class solution:
    def solved(self,nums):
        n=len(nums)
        ans=[]

        for i in range(1,n+1):
            if i not in nums:
                ans.append(i)
        return ans
    
    '''
    n = len(nums)
        ans = []

        # Mark seen numbers
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Collect missing numbers
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

    '''

s=solution()
print(s.solved([4,3,2,7,8,2,3,1]))
