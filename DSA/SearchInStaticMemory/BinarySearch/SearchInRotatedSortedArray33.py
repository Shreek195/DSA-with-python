from typing import List


class Solution:
    """
    Best way to solve this problem is divide the array based on the peak/pivot element
    Left side is ascending and right i.e, pivot+1 is also ascending

    Continue with the basic binary search on both left array and right array
    """

    @staticmethod
    def find_pivot(nums: List[int]) -> int:
        s, e = 0, len(nums) - 1

        while s < e:
            mid = s + (e - s) // 2

            if nums[mid + 1] > nums[mid] >= nums[s]:
                s = mid + 1
            else:
                e = mid

        return s

    # For Duplicate array elements
    # @staticmethod
    # def find_pivot(nums: List[int]) -> int:
    #     s, e = 0, len(nums) - 1
    #
    #     while s < e:
    #         if nums[s] == nums[e]:
    #             if nums[s] > nums[s + 1]:
    #                 return s
    #             s += 1
    #
    #             if nums[e] < nums[e - 1]:
    #                 return e - 1
    #             e -= 1
    #
    #             if s >= e:
    #                 return s
    #
    #         mid = s + (e - s) // 2
    #
    #         if nums[mid + 1] > nums[mid] >= nums[s]:
    #             s = mid + 1
    #         else:
    #             e = mid
    #
    #     return s

    @staticmethod
    def b_search(nums: List[int], target: int, s: int, e: int) -> int:
        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1

        return -1

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        pivot = Solution.find_pivot(nums)

        if (ans := Solution.b_search(nums, target, 0, pivot)) != -1:
            return ans
        return Solution.b_search(nums, target, pivot + 1, len(nums) - 1)


Solution = Solution()

print(Solution.search([1, 1], 1))
