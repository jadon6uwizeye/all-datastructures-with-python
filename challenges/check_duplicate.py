class Solution(object):
    def containsDuplicate(self, nums):
        count = 0
        for i in range(len(nums)):
            for num2 in nums[i+1:len(nums):1]:
                if num2==nums[i]:
                    return True
                
        return False