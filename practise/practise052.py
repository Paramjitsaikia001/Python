#powerset

class solution:
    def subsetsWithDup(self,nums):
        nums.sort()
        ans = []

        def backtrack(start, path):
            ans.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans

s=solution()
print(s.subsetsWithDup([1,2,2]))

'''
start=1
ans=[[],[1],[2,2]]

start=2
ans=[[],[1],[2,2],[1,2],[2]]
start
'''
