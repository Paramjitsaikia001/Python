class solution:
    def solved(self,prices):
        stack=[]
        ans=prices[:] #it copy the original array
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                    p=prices[stack[-1]]-prices[i]
                    ans[stack.pop()]=p
            stack.append(i)
        return ans
s=solution()
print(s.solved([8,4,6,2,3]))
print(s.solved([1,2,3,4,5]))
print(s.solved([10,1,1,6]))
