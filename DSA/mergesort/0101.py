class solution:
    def solved(self,num):
        self.mergesort(num,0,len(num)-1)
        return num
    def merge(self,num,start,end,mid):
        temp=[]
        i,j=start,mid+1

        while i<=mid and j<=end:
            if num[i]<=num[j]:
                temp.append(num[i])
                i+=1
            else:
                temp.append(num[j])
                j+=1

        while i<=mid:
            temp.append(num[i])
            i+=1
        
        while j<=end:
            temp.append(num[j])
            j+=1

        for i in range(len(temp)):
            num[i+start]=temp[i]
        
    
    def mergesort(self,num,start,end):
        if start<end:
            mid=start+(end-start)//2

            self.mergesort(num,start,mid)
            self.mergesort(num,mid+1,end)
            self.merge(num,start,end,mid)

s=solution()
print(s.solved([12,31,35,8,32,17]))


        
