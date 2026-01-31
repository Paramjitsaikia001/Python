class Solution:
    def findErrorNums(self, nums):
        seen=set()
        for x in nums:
            if x in seen:
                duplicate=x
            seen.add(x)
        return seen
            

s=Solution()
print(s.findErrorNums([1,2,2,4]))
print(s.findErrorNums([2,2]))
print(s.findErrorNums([1,1]))
print(s.findErrorNums([3,2,2]))

        