from typing import List, Any

class Solution:
    @staticmethod
    def group_anagrams(strs: List[str]) -> list[str] | list[Any]:
        if len(strs) == 1:
            return [[strs[0]]]

        count_map = {}
        result = []

        # Iterate through the array
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1

            # convert to string or tuple and store as key in map
            key = tuple(freq)
            count_map.setdefault(key, []).append(word)

        # Return the list
        for key, value in count_map.items():
            result.append(value)

        return result

Solution = Solution()
print(Solution.group_anagrams(["bdddddddddd","bbbbbbbbbbc"]))
# print(Solution.group_anagrams(['a']))