from typing import List
import heapq


class Solution:
    # Using Priority Heap
    # @staticmethod
    # def top_k_frequent(nums: List[int], k: int) -> List[int]:
    #     if len(nums) == 1:
    #         return [nums[0]]
    #
    #     # Impute the frequency map
    #     freq_map = {}
    #     for i in nums:
    #         freq_map[i] = freq_map.setdefault(i, 0) + 1
    #
    #     # Using priority heap
    #     heap = []
    #     for ele, freq in freq_map.items():
    #         heapq.heappush(heap, (freq, ele))
    #         while len(heap) > k:
    #             heapq.heappop(heap)
    #
    #     return [num for freq, num in heap]

    # Using

    # Using Bucket Sort
    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.setdefault(i, 0) + 1

        # Bucket
        bucket = [[] for i in range(len(nums) + 1)]

        for ele, freq in freq_map.items():
            bucket[freq].append(ele)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result[:k]

        return result


Solution = Solution()
print(Solution.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
