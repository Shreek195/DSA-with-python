from typing import List

class Solution:
    @staticmethod
    def roman_to_integer(s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                     'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        result = 0
        i = 0
        while i < len(s):
            if (key := s[i] + s[i+1] if i+1 < len(s) else False) in roman_map:
                result += roman_map[key]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1

        return result

Solution = Solution()
print(Solution.roman_to_integer("ICV"))