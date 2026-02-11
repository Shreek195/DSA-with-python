from typing import List


class Solution:
    @staticmethod
    def is_min(nums: List[int], k: int, target: int) -> bool:
        ele_sum = 0
        p = 1

        for i in range(len(nums)):
            if ele_sum + nums[i] > target:
                p += 1
                ele_sum = 0

                if p > k:
                    return False

            ele_sum += nums[i]

        return p <= k

    @staticmethod
    def split_array(nums: List[int], k: int) -> int:
        # start = maximum in array, end = sum of array
        s, e = max(nums), sum(nums)

        while s < e:
            mid = s + (e - s) // 2

            if Solution.is_min(nums, k, mid):
                e = mid
            else:
                s = mid + 1

        return s


Solution = Solution()

print(Solution.split_array([1, 2, 3, 4, 5], 1))
