from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def generate(chosen: list, target: int):
            if target == 0:
                chk = sorted(chosen[:])
                if chk not in ans:
                    ans.append(chk)
            if target < 0:
                return

            for candidate in candidates:
                chosen.append(candidate)
                generate(chosen, target - candidate)
                chosen.pop()
        generate([], target)
        return ans


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]])
print(s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
print(s.combinationSum([2], 1) == [])
print(s.combinationSum([1], 1) == [[1]])
print(s.combinationSum([1], 2) == [[1, 1]])
