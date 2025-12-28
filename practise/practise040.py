class solution:
    def angaram(self,s,t):
        if len(s)!=len(t):
            return False
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord("a")]+=1
            count[ord(t[i])-ord("a")]-=1
        for i in range(26):
            if count[i]!=0:
                return False
        return True

s=solution()
print(s.angaram("anagram","nagaran"))