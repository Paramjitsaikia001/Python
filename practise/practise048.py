#peak index in mountain array

class solution:
    def peaki(self,nums):
        l=1
        h=len(nums)-2
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                l=mid
            else:
                h=mid
        return mid
    
s=solution()
print(s.peaki([0,3,8,9,5,2]))
print(s.peaki([0,10,5,2]))