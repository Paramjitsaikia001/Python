class solution:
    def solved(self,tokens):
        def is_int(x):
            try:
                int(x)
                return True
            except:
                return False
        stack=[]
        for i in tokens:
            if is_int(i):
                stack.append(int(i))
            else:
                idx2=int(stack.pop())
                idx1=int(stack.pop())
                if i=="+":
                    stack.append(idx1+idx2)
                elif i=="*":
                    stack.append(idx1*idx2)
                elif i=="-":
                    stack.append(idx1-idx2)
                else:
                    stack.append(int(idx1/idx2))
        return stack.pop()
s=solution()
print(s.solved(["2","1","+","3","*"]
))
print(s.solved(["4","13","5","/","+"]))
print(s.solved(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))