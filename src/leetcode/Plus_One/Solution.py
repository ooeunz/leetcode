from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
            else:
                digits[i] += 1
                break
        return digits


s = Solution()
print(s.plusOne([9]) == [1, 0])
print(s.plusOne([9, 9]) == [1, 0, 0])
