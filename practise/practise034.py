class Solution(object):
    def maximizeNumber(self, nums):
        """
        :type nums: int        
        :rtype: int
        """
        a=list(str(nums))
        for i in range(len(a)):
            if a[i]=="6":
                a[i]="9"
                break
            
        return int("".join(a))

s=Solution()
print(s.maximizeNumber(9996))