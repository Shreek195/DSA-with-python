from typing import List


class Solution:
    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        """
        Returns 'start % len(letters)' <- 'rotating or wrapping' when the loop is violated, cause element == target is not the concern
        else, if the start goes out of the bound on the right-side it returns first element
        """
        s, e = 0, len(letters) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if target >= letters[mid]:
                s = mid + 1
            else:
                e = mid - 1

        return letters[s % len(letters)]


Solution = Solution()

print(Solution.next_greatest_letter(["c", "f", "j"], "j"))
