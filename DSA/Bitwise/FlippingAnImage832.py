from typing import List


class Solution:
    @staticmethod
    def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range((len(row) + 1) // 2):
                row[i], row[len(row) - i - 1] = row[len(row) - i - 1] ^ 1, row[i] ^ 1

        return image


Solution = Solution()
print(Solution.flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
