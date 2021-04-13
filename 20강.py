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