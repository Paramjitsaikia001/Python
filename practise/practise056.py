#find the duplicate number from a list

class solution:
    def find(self,nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
    
s=solution()
print(s.find([1,3,4,2,2]))
print(s.find([3,1,3,4,2]))
print(s.find([3,3,3,3,3]))