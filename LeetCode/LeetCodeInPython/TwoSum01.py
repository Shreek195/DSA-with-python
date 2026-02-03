from typing import List

class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, ele in enumerate(nums):
            if (target - ele) in seen:
                return [seen[target - ele], idx]
            seen[ele] = idx

        return []

Solution = Solution()
print(Solution.two_sum([10, 20, 1, 8, 9], 17))