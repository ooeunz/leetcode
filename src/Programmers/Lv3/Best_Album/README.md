# [베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579)

`genres[i]`는 장르의 이름이고, `plays[i]`는 해당 장르의 재생 수이고, `i`는 노래의 id 값을 나타낼 경우, 
아래의 기준에 맞추어 각 장르별로 최대 2개까지 정답 배열에 담아 return 하는 문제입니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

> 2020-01-17

### solve 1.
특별한 알고리즘 풀이법은 없고 HashMap 형태의 자료구조를 자유롭게 사용할 수 있는지를 체크하는 문제입니다.

`total = {"장르": 전채_재생시간}`

`popular = {"장르": [(앨범_id, 재생시간), ...]`

형태의 두 dictionary를 만든 다음, 각 장르별로 재생시간이 많은 순으로 최대 2개까지 `ans` 배열에 담아서 return해 줍니다. 

```python
from collections import defaultdict


def solution(genres: list, plays: list):
    total = defaultdict(int)
    popular = defaultdict(list)
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
```