import collections


def solution(genres: list, plays: list):
    total = collections.defaultdict(int)
    popular = collections.defaultdict(list)
    for music in range(len(genres)):
        genre, play = genres[music], plays[music]
        total[genre] += play
        popular[genre].append((music, play))
    orders = list(sorted(total, key=lambda items: total[items], reverse=True))

    ans = []
    for order in orders:
        popular[order].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        ans += list(map(lambda x: x[0], popular[order][:2]))
    return ans


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
