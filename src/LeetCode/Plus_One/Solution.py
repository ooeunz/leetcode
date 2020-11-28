from typing import List


class Solution:
    def round_up(self, digits: list, idx: int):
        if idx < len(digits):
            if digits[idx] == 9:
                digits[idx] = 0
                self.round_up(digits, idx + 1)
            else:
                digits[idx] += 1
        else:
            digits.append(1)

    def plusOne(self, digits: List[int]) -> List[int]:
        reverse = list(reversed(digits))
        if reverse[0] == 9:
            self.round_up(reverse, 0)
        else:
            reverse[0] += 1
        return list(reversed(reverse))


s = Solution()
print(s.plusOne([9]) == [1, 0])
print(s.plusOne([9, 9]) == [1, 0, 0])
