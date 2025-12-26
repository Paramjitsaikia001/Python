class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                result.append(s[i].lower())
                print(result)
        return result==result[::-1]

s1=Solution()
print(s1.isPalindrome("0P"))