from typing import List


class Solution:
    @staticmethod
    def peak_index_in_mountain_array(arr: List[int]) -> int:
        """
        At the end of the loop, start == end and both point to the peak element.

        Throughout the binary search, start and end always maintain a range that
        contains the maximum element. By comparing arr[mid] with arr[mid + 1],
        we discard the side that cannot contain the peak.

        When only one element remains in the range, that element must be the peak,
        because all other possibilities have already been eliminated.

        return start or end (any)
        """

        s, e = 0, len(arr) - 1

        while s < e:
            mid = s + (e - s) // 2

            if arr[mid] > arr[mid + 1]:
                e = mid
            # elif arr[mid] < arr[mid + 1]:
            # because we don't have duplicate elements we don't need to think of <=,
            # hence we can use else direct
            else:
                s = mid + 1

        return s


Solution = Solution()

print(Solution.peak_index_in_mountain_array([0, 10, 5, 2]))
