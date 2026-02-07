class solution:
    def solve(self,s):
        vowel=[]
        def isvowel(a):
            v="aeiouAEIOU"
            return a in v
        
        n=len(s)

        for i in range(n):
            if isvowel(s[i]):
                vowel.append(s[i])
        vowel.sort(key=lambda x:ord(x))
        s=list(s)
        j=0
        for i in range(n):
              if isvowel(s[i]):
                s[i]=vowel[j]
                j+=1
        return "".join(s)
    
ans=solution()
print(ans.solve("lEetcOde"))
