#search in rotated sorted array

class solution:
    def rotatedarr(self,num,k):
        low=0
        high=len(num)-1
        while low<=high:
            mid=low+(high-low)//2
            if num[mid]==k:
                return mid
            elif num[low]<=num[mid]:
                if num[low] <= k <=num[mid]:
                    high=mid-1
                else:

                    low=mid+1
            else:
                if num[mid]<=k<=num[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
s=solution()
print(s.rotatedarr([6,7,0,1,2,4,5],7))
