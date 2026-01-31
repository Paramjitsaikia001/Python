class solution:
    def solved(self,terget,n):
        m=len(terget)
        i=0
        j=1
        ans=[]
        while i <m and j <=n:
            if terget[i]==j:
                ans.append("push")
                i+=1
                j+=1
            else:
                ans.append("push")
                ans.append("pop")
                j+=1
        return ans

s=solution()
print(s.solved(terget = [1,3], n = 3))
print(s.solved(terget = [1,2,3], n = 3))
print(s.solved(terget = [1,2], n = 4))
            