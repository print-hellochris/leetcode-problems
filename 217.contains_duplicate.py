"""1480.Running Sum of 1d Array.py
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

# class Solution(object):
# def containsDuplicate(self, nums):
#     return len(nums) != len(set(nums))
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        solution_dict = {}
        for numbers in nums:
            solution_dict.update({numbers: nums.count(numbers)})

        for keys, values in solution_dict.items():
            if solution_dict.get(keys) > 1:
                return True

            if nums.count(numbers) > 1:
                return True
            else:
                return False


solution = Solution()
print(solution.containsDuplicate(nums=[2, 14, 18, 22, 22]))

print(set([1, 2, 3, 1]))
