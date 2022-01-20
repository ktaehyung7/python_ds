class Solution:
    def strStr(self, haystack, needle):
        j=0
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                j +=1
            else:
                j = 0
                
            if j == len(needle):
                return i-len(needle)+1
        return -1
            
a = Solution()
aa = a.strStr('hello', 'll')
ab = a.strStr('aaaaa', 'bba')
ac = a.strStr('', '')
ad = a.strStr('station', 'tio')