#https://leetcode.com/problems/two-sum/
#return indices of two two number which sum up to result

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}

        for index in range(len(nums)):
            compliment = target - nums[index]

            if compliment in dictionary:
                return [dictionary[compliment],index]
            
            dictionary[nums[index]] = index
