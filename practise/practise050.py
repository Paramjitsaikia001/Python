class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a=nums1
        b=nums2

        alen=len(a)
        blen=len(b)


        if alen>blen:
            a,b=b,a
            alen, blen = blen, alen
        
        total=alen+blen
        half=total//2

        lft=0
        rgt=len(a)-1

        while True:
            mid=lft+(rgt-lft)//2
            bridx=half-mid-2

            aleft=a[mid] if mid >=0 else float("-infinity")
            aright=a[mid+1] if (mid+1)<alen else float("infinity")
            bleft=b[bridx] if bridx>=0 else float("-infinity")
            bright = b[bridx+1] if (bridx+1)<blen else float("infinity")

            if aleft <=bright and bleft <=aright:
                if total%2!=0:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2
            elif aleft > bright:
                rgt=mid-1
            else:
                lft=mid+1

s=Solution()
print(s.findMedianSortedArrays([1,2,3,4,5,6,7,8],[1,2,3,4,5]))
        