from typing import List

class Solution:
    # Using HashMap
    # @staticmethod
    # def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    #     idx_map = {}
    #     for idx, ele in enumerate(nums):
    #         if ele in idx_map:
    #             if idx - idx_map[ele] <= k:
    #                 return True
    #         idx_map[ele] = idx
    #
    #     return False

    # Using HashSet + Sliding Window
    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        window = set()
        for idx, ele in enumerate(nums):
            if ele in window:
                return True
            window.add(ele)

            if len(window) > k:
                window.remove(nums[idx - k])
        return False

Solution = Solution()
print(Solution.contains_nearby_duplicate([1, 2, 3], 3))