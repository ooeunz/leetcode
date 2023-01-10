# [오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3#_=_)

> 2021-01-20

### solve 1.
python에 dictionary 자료구조를 이용하여 문제를 풀이합니다.

오픈 채팅방에 들어온 유저들의 이름이 바뀔 수 있는 경우는 Change와 Enter일 경우입니다. (Leave는 아님)

따라서 `record`안에 있는 문자열을 공백을 기준으로 split하여 Enter와 Change일 경우 `key_id` dictionary의 값을 갱신해줍니다.
그 후 다시 한번 for문을 돌며 최신으로 적용된 유저의 이름을 기준으로 문자열을 입력하여 준후 return 합니다.

```python
def solution(record: list):
    key_id = {}
    for r in record:
        splitV = r.split(' ')
        if len(splitV) == 3:
            key_id[splitV[1]] = splitV[2]
    ans = []
    for r in record:
        splitV = r.split(' ')
        if splitV[0] == "Enter":
            ans.append(f"{key_id[splitV[1]]}님이 들어왔습니다.")
        elif splitV[0] == "Leave":
            ans.append(f"{key_id[splitV[1]]}님이 나갔습니다.")
    return ans
```