class solution:
    def four_sum(self,nums,target):
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k <l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum <target:
                        k+=1
                    elif sum >target:
                        l-=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
        return ans
        

s1=solution()
print(s1.four_sum([1,0,-1,0,-2,2],0))
