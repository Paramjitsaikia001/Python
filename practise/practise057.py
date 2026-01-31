class solution:
    def nextgreatest3(self,n):
        d=list(str(n))
        p=len(d)-2
        while p>=0 and d[p]>=d[p+1]:
            p-=1
        
        if p==-1:
            return -1
        
        j=len(d)-1

        while d[j]<=d[p]:
            j-=1
        d[j],d[p]=d[p],d[j]

        d[p+1:]=reversed(d[p+1:])

        res=int("".join(d))

        return res if res<=2**31-1 else -1
        

        
s=solution()
print(s.nextgreatest3(21))
