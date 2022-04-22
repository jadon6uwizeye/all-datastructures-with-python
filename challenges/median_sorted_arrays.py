class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        for  num1 in nums1:
            if nums2[0] < num1:
                nums = nums + nums2
                
            nums = nums + [num1]
                    
        if (nums1[len(nums1)-1] < nums2[0]):
            nums = nums + nums2
                
        nums_length = len(nums)
        if( nums_length % 2 != 0):
            index = (nums_length//2)
            print(index)
            return nums[index]
        else:
            index1 = (nums_length//2)-1
            index2 = (nums_length//2)
            return (nums[index1]+nums[index2])/2

s = Solution()
print(s.findMedianSortedArrays([0,1,2,3],[4,5]))