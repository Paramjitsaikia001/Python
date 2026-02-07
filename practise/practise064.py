class solution:
    def solved(self,st,sd):
        count=0
        i,j=len(st),len(sd)
        while i >0 or j >0:
            print(st,sd)
            if st[0]==sd[0]:
                count+=1
                sd.pop(0)
                st.pop(0)
                i-=1
                j-=1
            else:
                idx=st.pop(0)
                st.append(idx)

        return count
    
s=solution()
print(s.solved([1,1,0,0],[0,1,0,1]))
print(s.solved([1,1,1,0,0,1],[1,0,0,0,1,1]))
