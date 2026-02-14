from typing import List, Any


class Solution:
    @staticmethod
    def find_duplicate(nums: List[int]) -> int | list[Any]:
        i = 0
        # Cyclic sort: place each number at index (value - 1)
        while i < len(nums):
            correct_idx = nums[i] - 1  # Target index for current value

            # If value not at correct position, swap it
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # If duplicate found at wrong index, return it early
                if correct_idx != i:
                    return nums[i]
                i += 1  # Move forward if already correctly placed

        result = []
        # Second pass: collect mismatched indices
        for idx, ele in enumerate(nums):
            if ele - 1 != idx:  # If value not at correct index
                result.append(idx + 1)

        return result


nums = [3, 3, 3, 3, 3]
print(Solution().find_duplicate(nums))
