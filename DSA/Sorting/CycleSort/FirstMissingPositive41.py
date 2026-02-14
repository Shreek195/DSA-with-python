from typing import List


class Solution:
    @staticmethod
    def first_missing_positive(nums: List[int]) -> int:
        i = 0

        # Cyclic sort: place each positive number x at index (x - 1)
        while i < len(nums):
            correct_idx = nums[i] - 1  # Target index for current value

            # Swap only if:
            # 1) value is in valid range [1, n]
            # 2) value is not already at correct position
            if len(nums) > correct_idx >= 0 and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1  # Move forward if invalid or already placed

        # After placement, first index where value != index+1 is answer
        for idx, ele in enumerate(nums):
            if idx + 1 != ele:
                return idx + 1

        # If all positions are correct, missing number is n + 1
        return len(nums) + 1


nums = [7, 8, 9, 11, 12]
print(Solution().first_missing_positive(nums))
