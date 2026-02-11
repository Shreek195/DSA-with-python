from typing import List


class Solution:
    @staticmethod
    def count_rotation(nums: List[int]) -> int:
        """
        Find the pivot element and return pivot + 1
        if pivot + 1 > length of nums return 0
        as the array is not rotated at all
        """
        s, e = 0, len(nums) - 1

        while s < e:
            mid = s + (e - s) // 2

            if nums[mid + 1] > nums[mid] >= nums[s]:
                s = mid + 1
            else:
                e = mid

        return (s + 1) % len(nums)


Solution = Solution()

print(Solution.count_rotation([10, 11, 3, 4, 5, 6]))
