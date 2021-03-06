from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def generate(chosen: list, target: int):
            if target == 0:
                ans.append(chosen[:])
                return
            if target < 0:
                return

            start = candidates.index(chosen[-1]) if chosen else 0
            for i in range(start, len(candidates)):
                chosen.append(candidates[i])
                generate(chosen, target - candidates[i])
                chosen.pop()
        generate([], target)
        return ans


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]])
print(s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
print(s.combinationSum([2], 1) == [])
print(s.combinationSum([1], 1) == [[1]])
print(s.combinationSum([1], 2) == [[1, 1]])
