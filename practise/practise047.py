class solution:
    def histrogram(self,nums):
        low=0
        high=len(nums)-1
        lmax=nums[low]
        rmax=nums[high]

        while low<high:
            lmax=max(lmax,nums[low])
            rmax=max(rmax,nums[high])
            low+=1
            high-=1
            
