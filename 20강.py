# 리트코드 239번

def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        queue = collections.deque()
        
        for i, v in enumerate(nums):
            while queue and nums[queue[-1]] <= v:
                queue.pop()
            
            queue.append(i)
            if i - queue[0] >= k:
                queue.popleft()
            
            if i >= k - 1:
                results.append(nums[queue[0]])
            
        return results


# 리트코드 76번

def minWindow(self, s: str, t: str) -> str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    for char, right in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]


# 리트코드 424번

def characterReplacement(self, s: str, k: int) -> int:
    counts = collections.Counter()
    left = right = 0

    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        max_char_n = counts.most_common(1)[0][1]

        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1

    return right - left