class Solution:

    @staticmethod
    def find_peak(arr) -> int:
        """
        Finding the Peak element,
        as the 's' and 'e' lands on the peak we can return any

        According to logic 's' and 'e' will always tend to find peak
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

    @staticmethod
    def order_agnostic_search(arr, target, start, end):
        """
        Simple Order Agnostics Binary Search Implementation for based on 'start': 's' and 'end': 'e'
        """
        s, e = start, end

        is_asc = arr[s] < arr[e]

        while s <= e:
            mid = s + (e - s) // 2

            if target == arr[mid]:
                return mid
            if is_asc:
                if target < arr[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if target < arr[mid]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1

    @staticmethod
    def find_in_mountain_array(arr, target: int) -> int:
        """
        We Find the Peak
        Divide the array in 2 Halves

        Do the Order Agnostic search on both

        Edge Case:
        if the peak is on the left end, --> s = 0, e = n-1
        if the peak is on the right end --> s = 0, e = n-1

        else for the left side --> s = 0, e = peak
        and for the right --> s = peak + 1, e = n-1

        Now as we can see the 1st 3 cases are almost same if call it as left
        and finally right
        """
        peak = Solution.find_peak(arr)

        left_halve = Solution.order_agnostic_search(arr, target, 0, peak)
        if left_halve != -1:
            return left_halve

        return Solution.order_agnostic_search(arr, target, peak + 1, len(arr) - 1)


Solution = Solution()

print(Solution.find_in_mountain_array([0, 1, 4, 2, 1], 2))
