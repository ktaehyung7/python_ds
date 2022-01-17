class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        
        if s[::] == s[::-1]:
            print("::true")
        else:
            print("::false")
            
    def isPalindrome1(self, x):
        stack = []
        s = str(x)
        for letter in s:
            stack.append(letter)
        for letter in s:
            if stack.pop() != letter:
                print("::false")
                return False
        print("::true")
        return True
            
a = Solution()
aa = a.isPalindrome(122)
ab = a.isPalindrome1(121)