"""
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix = []
        prod = 1
        for num in nums:
            prod *= num
            prefix.append(prod)

        prod = 1
        suffix = []
        for num in reversed(nums):
            prod *= num
            suffix.append(prod)        
        suffix.reverse()
        
        res = [0] * size
        for i in range(size):
            if i == 0:
                res[i] = suffix[1]
            elif i == size-1:
                res[i] = prefix[size-2]
            else:
                res[i] = prefix[i-1] * suffix[i+1]

        return res


        
