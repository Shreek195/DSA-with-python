from typing import List


class Solution:
    @staticmethod
    def search_element(nums: List[int], target: int) -> int:
        """
        Here to find the element in infinite array we define a window
        the window grows exponentially

        NOTE: Infinite array as no bounds for 'end'
        but for the sake of answer I keep the 'end' = length of array if it exceeds the bounds of input array
        """

        s, e = 0, 1

        # Check for whether the target lies within the bounds or not
        while target > nums[e]:
            temp = e + 1
            e += (e - s + 1) * 2
            s = temp

            # Just for the sake to keep the end in the bounds
            if e >= len(nums):
                e = len(nums) - 1
                break

        # Normal Binary Search
        while s <= e:
            mid = s + (e - s) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                s = mid + 1
            else:
                e = mid - 1

        return -1

Solution = Solution()

print(Solution.search_element([1, 2, 5, 8, 10, 20, 25, 26, 30, 35, 36], 26))
