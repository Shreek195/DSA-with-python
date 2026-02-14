from typing import List


class Solution:
    @staticmethod
    def find_duplicates(nums: List[int]) -> List[int]:
        # Step 1: Place each number at its correct index
        # Number x should be at index x - 1
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1

            # If current number is not at its correct position,
            # swap it with the element at its correct index
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # If already in correct position or duplicate,
                # move to next index
                i += 1

        # Step 2: Identify duplicates
        # After cyclic placement:
        # If index i does not contain i+1,
        # then the value at that index is a duplicate
        result = []
        for idx, ele in enumerate(nums):
            if idx + 1 != ele:
                result.append(ele)

        return result


nums = [1, 1, 2]
print(Solution().find_duplicates(nums))
