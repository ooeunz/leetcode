# [Validate Binary Search Tree]()https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

> 2020-11-29

주어진 Binary Search Tree가 유효한지를 확인하는 알고리즘입니다.

### solve 1.
> 처음으로 `수학적 귀납법`에 관해 문제를 통해 이해하게 된 케이스입니다.

Binary Search Tree는 하나의 root node가 존재할 경우 왼쪽에 있는 모든 노드는 해당 node보다 값이 작아야하고, 
오른쪽에 있는 모든 노드는 root node보다 값이 커야합니다.

때문에 바로 이전의 노드의 값과 비교하여 왼쪽이라면 이전 노드의 값보다 작은지를 비교하고, 오른쪽으로 가게되면 이전 노드의 값보다 큰지를 비교하면 됩니다.
하지만 만약 아래와 같은 케이스라면 어떨까요? 
```
    3
   / \
  1   5
     / \
    2   6
```

2은 5보다 작지만, 5 이전의 node인 3보다도 값이 작게 됩니다. 이는 오른쪽에 있는 node는 모두 기준이되는 node보다 값이 커야한다는 rule을 벗어납니다.
이러한 경우는 이전의 노드의 값만으로는 Binary Search Tree가 올바르게 구성되어 있는지를 확인할 수 없습니다.

그렇다면 이때까지 방문했던 모든 노드의 값을 배열에 저장해두고 비교 해보아야 할까요?
그것 역시 방법이 될 수 있지만, 그렇게 되면 시간복잡도와 공간복잡도가 엄청나게 높아지게 되기 때문에 좋은 해법이 될 수 없습니다.

이때 들어가는 개념이 바로 **수학적 귀납법**입니다. 수학적 귀납법이란 *자연수 n에 관한 명제 P(n)이 모든 자연수에 대해서 성립함을 증명하기 위한 수학의 증명법 중 한 방법* 입니다.

수학적 귀납법은 아래의 두가지 방법으로 증명할 수 있습니다.
1. P(1)이 성립함을 보인다.
2. P(k)가 성립한다고 가정하고 P(k+1)이 성립함을 보인다.

다시 문제로 돌아와서 어떻게 이 문제에 수학적 귀납법을 사용할지 확인해보겠습니다.
이번에 세워보는 가정은 **마지막으로 검사한 값에 `True`라면 이전의 값 모 `True`이다.** (말이 좀 이상한가..?)입니다.

```
    3
   / \
  1   7
     / \
    5   8
   /\  /\
  4
```
이번엔 좀 더 트리를 확장시켜 보도록 하겠습니다.
- `7`은 `3`보다 오른쪽에 있으므로 `3`보다 값이 커야합니다. (`7`이 검증됩니다.)
- `5`는 `7`보다 왼쪽에 있으므로 `7`보다 값이 작아야하고 `3` 보다는 값이 커야합니다. (`5`가 검증됩니다.)
- `4`는 `5`보다 왼쪽에 있으므로 `5`보다 값이 작아야합니다.

우리는 `4`를 비교할 때 *`4`는 `3`보다 크고 `7`보다 작고 `5`보다도 작은지* 와 같은 방식으로 검사하지 않고 `5`보다 크고 `7`보다 작은지만을 검사했습니다.
`5`보다 작을 경우, 이전에 검사했던 `7`보다는 당연히 작을 것 이라는 가정하에 진행된 것입니다.

이와 같은 방법론은 예시와 같이 case가 적은 경우엔 차이가 미미하지만, test case가 많으면 많을수록 time complexity에서 큰 차이를 보입니다.
 
```python
class Solution:
    def check_valid(self, node: TreeNode, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if lower < node.val < upper:
            return self.check_valid(node.left, lower, node.val) and self.check_valid(node.right, node.val, upper)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_valid(root)
```