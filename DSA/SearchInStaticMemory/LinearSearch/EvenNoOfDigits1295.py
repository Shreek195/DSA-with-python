import math
from typing import List


class Solution:
    @staticmethod
    # def find_numbers(nums: List[int]) -> int:
    #     ans = 0
    #
    #     for i in nums:
    #         if len(str(i)) % 2 == 0 and len(str(i)) > 1:
    #             ans += 1
    #
    #     return ans

    # def find_numbers(nums: List[int]) -> int:
    #     ans = 0
    #
    #     for num in nums:
    #         if num < 0:
    #             num *= -1
    #         cnt = 0
    #         while num > 0:
    #             cnt += 1
    #             num //= 10
    #
    #         if cnt % 2 == 0:
    #             ans += 1
    #
    #     return ans

    def find_numbers(nums: List[int]) -> int:
        """
        The number of digits in a base-10 integer can be computed as ⌊log10(n)⌋ + 1.
        Similarly, ⌊log2(n)⌋ + 1 gives the number of bits required to represent n in binary.
        """

        ans = 0

        for num in nums:
            if (int(math.log10(num) + 1)) % 2 == 0:
                ans += 1

        return ans


Solution = Solution()

print(Solution.find_numbers([555, 901, 482, 1771]))
