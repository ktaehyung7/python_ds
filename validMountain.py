class Solution:
    def validMountainArray(self, x):
        isTop = 0
        for i in range(1, len(x)):
            if x[0] >= x[1]: return False
            else:
                if x[i-1] == x[i]: return False
                if isTop == 0:
                    if x[i-1] > x[i]: isTop = 1
                else :
                    if x[i-1] <= x[i]: return False
        return True
    
    def validMountainArray1(self, x):
        start, end, L = 0, -1, len(x)
        
        while start < L-1 and x[start] < x[start+1]:
            start +=1
            
        while end > -L and x[end] < x[end-1]:
            end -=1
            
        return start == end +L and 0 < start and end < -1
    
    def validMountainArray2(self, x):
        N = len(x)
        i=0
        
        while i+1 < N and x[i] < x[i+1]:
            i +=1
            
        if i == 0 or i == N-1:
            return False
        
        while i+1 < N and x[i] > x[i+1]:
            i += 1
            
        return i == N-1
    
a = Solution()
aa = a.validMountainArray([0,3,3,2,1])
ab = a.validMountainArray1([0,3,3,2,1])
ac = a.validMountainArray2([0,3,3,2,1])
