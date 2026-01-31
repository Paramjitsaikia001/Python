# Continuous Subarray Sum

class solution:
    def sub(self,nums,k):
        h={}
        pre_sum=0
        for i in range(len(nums)):
            pre_sum+=nums[i]
            ans=(pre_sum-k)%k
            if ans in h:
                return True
            h[pre_sum]=1
        return False

s=solution()
print(s.sub([23,2,4,6,7],12))