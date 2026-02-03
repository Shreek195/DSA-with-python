from typing import List


class Solution:
    # @staticmethod
    # def bs(nums: List[int], target: int, is_first: bool) -> int:
    #     start, end = 0, len(nums) - 1
    #
    #     while start <= end:
    #         mid = start + (end - start) // 2
    #
    #         if is_first:
    #             if target <= nums[mid]:
    #                 end = mid - 1
    #             else:
    #                 start = mid + 1
    #         else:
    #             if target >= nums[mid]:
    #                 start = mid + 1
    #             else:
    #                 end = mid - 1
    #
    #     return start if is_first else end
    #
    # @staticmethod
    # def search_range(nums: List[int], target: int) -> List[int]:
    #     start = Solution.bs(nums, target, True)
    #     end = Solution.bs(nums, target, False)
    #
    #     if start == len(nums) or end == -1 or nums[start] != target or nums[end] != target:
    #         return [-1, -1]
    #     return ([start, end]

    """
    For First index 'end' will come towards 'start',
    For Last index 'start' will move towards 'end'

    Remember when we leave 'mid' element and move forward may be left or right halve
    we don't have any pointer pointing to the previous 'mid', hence we store the 'mid' to 'ans'

    Also, if the element is present in the other half then 'mid' will catch it
    if not then we have the 'ans' stored the previous 'mid' as the target value
    that is considered as first/last element based on which side we choose.
    """

    @staticmethod
    def bs(nums: List[int], target: int, is_first: bool) -> int:
        start, end = 0, len(nums) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                ans = mid
                if is_first:
                    end = mid - 1
                else:
                    start = mid + 1

        return ans

    @staticmethod
    def search_range(nums: List[int], target: int) -> List[int]:
        start = Solution.bs(nums, target, True)
        end = Solution.bs(nums, target, False)

        return [start, end]


Solution = Solution()

print(Solution.search_range([5, 7, 7, 8, 8, 10], 7))
