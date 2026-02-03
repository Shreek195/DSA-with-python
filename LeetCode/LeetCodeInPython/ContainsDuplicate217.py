from typing import List

class Solution:
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        if len(nums) == 1:  return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

Solution = Solution()
print(Solution.contains_duplicate([10, -11, -12, 9, 9, -11, 100]))