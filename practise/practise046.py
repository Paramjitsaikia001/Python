class solution:
    def slidingwindow(self,nums,k):
        l=0
        high=k-1
        ans=[]
        while high<len(nums):
            amax=nums[l]
            for i in range(l,high+1):
                amax=max(amax,nums[i])
            ans.append(amax)
            # print(an
            l+=1
            high+=1
s=solution()
print(s.slidingwindow([1,3,-1,-3,5,3,6,7],3))
print(s.slidingwindow([1],1))