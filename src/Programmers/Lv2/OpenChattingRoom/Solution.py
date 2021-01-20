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


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
