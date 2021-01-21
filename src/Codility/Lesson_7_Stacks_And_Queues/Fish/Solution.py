def solution(size: list, direction: list):
    no_down_streamp = True
    UP, DOWN = 0, 1
    size_stack = []
    ans = 0
    for i in range(len((size))):
        if no_down_streamp and direction[i] == UP:
            ans += 1
        else:
            no_down_streamp = False

            if direction[i] == DOWN:
                size_stack.append(size[i])
            elif direction[i] == UP:
                while size_stack and size_stack[-1] < size[i]:
                    size_stack.pop()
                if not size_stack:
                    ans += 1
    return ans + len(size_stack)


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
