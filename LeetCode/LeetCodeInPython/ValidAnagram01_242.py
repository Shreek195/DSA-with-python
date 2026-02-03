from typing import List

class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Alphabet count
        freq = [0] * 26

        for i in range(len(s)):
            # For s String
            freq[ord(s[i]) - ord('a')] += 1
            # For t String
            freq[ord(t[i]) - ord('a')] -= 1

        # Check for non-zeros
        return all(i == 0 for i in freq)


Solution = Solution()
print(Solution.is_anagram("anagram", "nagaram"))