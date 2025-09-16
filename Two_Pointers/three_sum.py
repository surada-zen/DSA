"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        size = len(nums)
        for i in range(size):
            if i > 0 and (nums[i - 1] == nums[i]):
                continue

            l = i+1
            r = size-1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        return res

