# Subarray sum equals k

class solution:
    def solved(self,nums,t):
        count=0
        
        
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==t:
                    count+=1
                    break
                if sum >t:
                    break
        return count
    
s=solution()
print(s.solved([1,1,1],2))
print(s.solved([1,2,3],3))
print(s.solved([9,4,20,3,10,5],33))

        