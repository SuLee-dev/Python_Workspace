# 리트코드 215번

def findKthLargest(self, nums: List[int], k: int) -> int:

    return heapq.nlargest(k, nums)[-1]