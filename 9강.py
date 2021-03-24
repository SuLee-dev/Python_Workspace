# 리트코드 20번

def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


# 리트코드 316번

# 스택
def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        seen.add(char)
        stack.append(char)

    return ''.join(stack)

# 재귀
def removeDuplicateLetters(self, s: str) -> str:

    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))

    return ''



# 리트코드 739번

def dailyTemperatures(self, T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        if stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


# 리트코드 225번

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()