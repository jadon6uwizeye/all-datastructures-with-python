class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i=0
        j=0
        
        if len(nums1) == 0 or len(nums2) == 0 :
                nums = nums1 + nums2
        else:
            while True:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i +=1
                elif nums2[j] < nums1[i]:
                    nums.append(nums2[j])
                    j+=1

                else:
                    nums.append(nums1[i])
                    nums.append(nums2[j])
                    i+=1
                    j+=1

                if i==len(nums1):
                    nums+=nums2[j:]
                    break

                if j == len(nums2):
                    nums+=nums1[i:]
                    break


        nums_length = len(nums)
        if( nums_length % 2 != 0):
            index = (nums_length//2)
            print(nums)
            return nums[index]
        else:
            index1 = (nums_length//2)-1
            index2 = (nums_length//2)
            print(nums)
            try:
                return (nums[index1]+nums[index2])/2
            except IndexError:
                return 1

s = Solution()
print(s.findMedianSortedArrays([0,1,2,3],[4,5]))