class Solution:
    def longestCommonPrefixH(self, strs):
        prefix = strs[0]
        for i in range(1, len(strs)):
            while prefix not in strs[i]:
                prefix = prefix[:-1]
                if len(prefix) <=0: return ":None!"
                    
        print(prefix)
        
    def longestCommonPrefixV(self, strs):
        for i in range(len(strs[0])):
            for s in strs:
                if strs[0][i] != s[i] or i == len(s):
                    return strs[0][:i]
        
    def CommonPrefix(self, left, right):
        minA = min(len(left), len(right))
        for i in range(minA):
            if(left[i] != right[i]):
                return left[:i]
        return left[:minA]

    def longestCommonPrefixDC(self, strs, l, r):
        if l==r: 
            return strs[l]
        else :
            mid = (l+r)//2
            lcpLeft = self.longestCommonPrefixDC(strs, l, mid)
            lcpRight = self.longestCommonPrefixDC(strs, mid+1, r)
            return self.CommonPrefix(lcpLeft, lcpRight)                   
        

a = Solution()
aa = a.longestCommonPrefixV(["flower", "flow", "floight"])            
ab = a.longestCommonPrefixDC(["aab", "aac", "aaa", "aad"], 0, 3)
