class solution():
    def reverseofword(self,s):
        ans=""
        s=s[::-1]
        i=0
        while i<len(s):
            if s[i]==" ":
                i+=1
                continue
            str=""
            while i<len(s) and s[i]!=" ":
                str+=s[i]
                i+=1
            ans+=str[::-1]+" "

        return ans
    
s=solution()
print(s.reverseofword("  the sky is blue  "))


