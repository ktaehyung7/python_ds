class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        i = 0
        
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
                
        print(nums)
        return i+1
    
    
a = Solution()
aa = a.removeDuplicates([0,1,1,1,2,3,3,4])