from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            fir = ans[-1]
            sec = intervals[i]
            if fir[1] >= sec[0]:
                ans[-1] = [fir[0], max(fir[1], sec[1])]
            else:
                ans.append(sec)
        return ans


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(s.merge([[1, 4], [4, 5]]) == [[1, 5]])
print(s.merge([[1, 4], [2, 3]]) == [[1, 4]])
