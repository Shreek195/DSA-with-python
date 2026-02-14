from typing import List, Any


class Solution:
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> list[Any]:
        # Step 1: Place each number at its correct index
        # (Number x should be at index x - 1)
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1

            # If current number is not at its correct position,
            # swap it with the number at its correct index
            # This continues until the current index has the correct value
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # If already correct (or duplicate), move forward
                i += 1

        # Step 2: Collect numbers that are not in their correct positions
        # If index i does not contain value i+1,
        # then i+1 is missing from the array
        result = []
        for idx, ele in enumerate(nums):
            if ele - 1 != idx:
                result.append(idx + 1)

        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().find_disappeared_numbers(nums))
