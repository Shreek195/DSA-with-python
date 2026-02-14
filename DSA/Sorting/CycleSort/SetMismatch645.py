from typing import List


class Solution:
    @staticmethod
    def find_error_nums(nums: List[int]) -> List[int]:
        i = 0

        # Cyclic sort: place each number x at index (x - 1)
        while i < len(nums):
            correct_idx = nums[i] - 1  # Target index for current value

            # Swap if value is not at its correct position
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1  # Move forward if already correctly placed

        # After placement:
        # Index mismatch reveals duplicate and missing number
        for idx, ele in enumerate(nums):
            if idx + 1 != ele:
                # ele → duplicate
                # idx + 1 → missing number
                return [ele, idx + 1]

        # Fallback (should not happen for valid input)
        return [-1, -1]


nums = [1, 2, 2, 4]
print(Solution().find_error_nums(nums))
