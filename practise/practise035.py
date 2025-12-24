class solution:
    def sum(self,nums):
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        a=sorted([nums[i],nums[j],nums[k]])
                        if a not in result:

                            result.append(a)




        return result
    
# s1=solution()
# print(s1.sum([-1,0,1,2,-1,-4]))


class Osol:
    def three_sum(self,nums):
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum <0:
                    j+=1
                elif sum >0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return ans

s1=Osol()
print(s1.three_sum([-1,0,1,2,-1,-4]))

                


