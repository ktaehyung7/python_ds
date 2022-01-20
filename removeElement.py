class Solution:
    def removeElement(self, nums, val):
        i=0
        for j in range(len(nums)):
            if val != nums[j]:
                nums[i] = nums[j]
                i +=1
        for k in range(i, len(nums)):
            nums[k] = None    
        print(nums)
        return i
                
a = Solution()
aa = a.removeElement([0,1,2,2,3,0,4,2], 2)