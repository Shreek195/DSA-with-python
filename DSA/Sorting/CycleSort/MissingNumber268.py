from typing import List


class Solution:
    @staticmethod
    def missing_number(nums: List[int]) -> int:
        i = 0

        # Cyclic sort: place each number x at index x
        # (valid values are in range [0, n])
        while i < len(nums):
            correct_idx = nums[i]  # Target index for current value

            # Swap only if:
            # 1) value is within array bounds (ignore n)
            # 2) value is not already at correct index
            if len(nums) > nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1  # Move forward if already placed or value == n

        # After placement, first index where index != value is missing
        for idx, ele in enumerate(nums):
            if idx != ele:
                return idx

        # If all indices match, missing number is n
        return len(nums)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missing_number(nums))
