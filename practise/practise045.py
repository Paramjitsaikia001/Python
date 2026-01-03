class solution:
    #brute force approach
    def traprainwater(self,height):
        water=0
        for i in range(1,len(height)-1):
            lmax=height[0]
            rmax=height[len(height)-1]
            for j in range(i):
                lmax=max(height[j],lmax)
                # print(lmax)
            for k in range(len(height)-1,i,-1):
                rmax=max(height[k],rmax)
                # print(rmax)
            water+=max(0,(min(lmax,rmax))-height[i])
            i+=1

        return water
    
    #optimal approach
    def trap(self, height):
        n=len(height)-1
        lmax=height[0]
        rmax=height[n]
        water=0
        low=1
        high=n-1
        while low<=high:
            print(water)
            lmax=max(lmax,height[low])
            rmax=max(rmax,height[high])
            if lmax<rmax:
                water+=lmax-height[low]
                low+=1
            else:
                water+=rmax-height[high]
                high-=1
        return water

        
s=solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))

