from typing import List


class Solution:
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # CF Product left to right
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # CF Product right to left
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


Solution = Solution()
print(Solution.product_except_self([1, 2, 3, 4]))
