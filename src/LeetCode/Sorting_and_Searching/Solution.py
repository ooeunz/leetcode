# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

# This is dummy function
def isBadVersion(version):
    return 0


class Solution:
    def firstBadVersion(self, n):
        start, mid, end = 0, 0, n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid) is False:
                start = mid + 1
            else:
                end = mid - 1
        return start
