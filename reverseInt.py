class Solution:
    def reverseInt(self, x):
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > INT_MAX//10 or (rev==INT_MAX and pop > 7): return 0
            if rev < INT_MIN//10 or (rev==INT_MIN and pop < -8): return 0
            rev = rev * 10 + pop
        
        return rev
    
a = Solution()
aa = a.reverseInt(123)
print(aa)