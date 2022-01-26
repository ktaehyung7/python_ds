class Solution:
    def roman2Int(self, s):
        values = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        
        i = 0
        
        while i < len(s)-1:
            if values[s[i]] >= values[s[i+1]]:
                result += values[s[i]]
            else:
                result -= values[s[i]]
            i +=1

        result += values[s[len(s)-1]]
        return result

a = Solution()
aa = a.roman2Int('LVIII')                