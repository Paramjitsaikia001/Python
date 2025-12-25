class solution:
    def per(self,nums):
        pivot=-1
        for i in range(len(nums)-2,0,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot==-1:
            nums.reverse()
            return 
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        low=pivot+1
        high=len(nums)-1
        while low<=high:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1

        return nums
    

s1=solution()
print(s1.per([1,2,3,6,5,4]))

