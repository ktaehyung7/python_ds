class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        t = 0
        for k in range(len(flowerbed)):
            if k==0:
                if flowerbed[k] == 0 and flowerbed[k+1] ==0: t +=1
            elif k==len(flowerbed)-1:
                if flowerbed[k-1] == 0 and flowerbed[k] == 0: t +=1
            else:
                if flowerbed[k-1] ==0 and flowerbed[k]==0 and flowerbed[k+1]==0: t +=1
            
        return t >= n
    
a = Solution()
aa = a.canPlaceFlowers([1,0,0,0,1], 2)