class solution:
    def solved(self,nums):
        ans=[0]*len(nums)
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    continue
                if nums[i]>nums[j]:
                    count+=1
            ans[i]=count
        
        return ans
s=solution()
print(s.solved([4,1,2,2,3]))
print(s.solved([7,7,7,7]))
print(s.solved([6,5,4,8]))
print(s.solved([6,5]))
print(s.solved([]))