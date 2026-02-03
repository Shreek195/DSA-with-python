import math
from asyncio import current_task
from typing import List


class Solution:
    @staticmethod
    def maximum_wealth(accounts: List[List[int]]) -> int:
        """
        Compare the curr_sum to the max_sum (global) so that the max wealth will be updateed
        every single time after inner loop is executed.
        """
        
        max_sum = float('-inf')

        for i in accounts:
            curr_sum = 0
            for j in i:
                curr_sum += j

            max_sum = max(max_sum, curr_sum)

        return max_sum


Solution = Solution()
print(Solution.maximum_wealth([[1, 2, 3], [3, 2, 1]]))
