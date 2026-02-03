from typing import List

class Solution:
    @staticmethod
    def is_alien_sorted(words: List[str], order: str) -> bool:
        order_map = {}

        for idx, value in enumerate(order):
            order_map[value] = idx

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    curr_element = order_map[words[i][j]]
                    next_element = order_map[words[i+1][j]]

                    if curr_element > next_element:
                        return False

                    break

        return True



Solution = Solution()
print(Solution.is_alien_sorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))