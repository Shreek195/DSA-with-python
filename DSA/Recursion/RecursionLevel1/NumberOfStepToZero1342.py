class Solution:
    def number_of_steps(self, num: int) -> int:
        return self.helper(num, 0)

    def helper(self, num, c):
        if num == 0:
            return c

        if num % 2 == 0:
            return self.helper(num // 2, c + 1)
        return self.helper(num - 1, c + 1)

if __name__ == "__main__":
    obj = Solution()
    print(obj.number_of_steps(14))
