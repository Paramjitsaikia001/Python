class solution:
    def removeoccurance(self,s,part):
        while s:
            idx=s.find(part)
            if  s.find(part)==-1:
                return s
            s=s.replace(s[idx:idx+len(part)],"")
    
s1=solution()
print(s1.removeoccurance("daabcbaabcbc","abc"))
