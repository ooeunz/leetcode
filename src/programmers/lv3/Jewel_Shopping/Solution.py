import collections


def solution(gems):
    start = end = 0

    GEMS_LENGTH = len(gems)
    GEMS_NUMS = len(set(gems))

    bag = collections.defaultdict(int)
    ans = [1, GEMS_LENGTH]

    bag[gems[start]] += 1
    while start < GEMS_LENGTH and end < GEMS_LENGTH:
        if len(bag) == GEMS_NUMS:
            if bag[gems[start]] == 1:
                ans = min([ans, [start + 1, end + 1]], key=lambda x: x[1] - x[0])
                del bag[gems[start]]
            else:
                bag[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == GEMS_LENGTH:
                break
            bag[gems[end]] += 1
    return ans


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]) == [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5])
