class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
             
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[nums[i]]=i

a = Solution()
b = a.twoSum([2,7,11,15], 9)
