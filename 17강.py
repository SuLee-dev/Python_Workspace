# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 리트코드 148번

def mergeTwoLists(self, l1: ListNode, l2: ListNode):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2

def sortList(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    l1 = self.sortList(slow)
    l2 = self.sortList(half)

    return self.mergeTwoLists(l1, l2)

# easy

def sortList(self, head: ListNode) -> ListNode:
    lst: List = []

    p = head
    while p:
        lst.append(p.val)
        p = p.next

    lst.sort()

    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head


# 리트코드 56번

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key = lambda x : x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,

    return merged


# 리트코드 147번

def insertionSortList(self, head: ListNode) -> ListNode:
    cur = parent = ListNode(0)

    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        
        cur.next, head.next, head = head, cur.next, head.next
        if head and cur.val > head.val:
            cur = parent
    
    return parent.next


# 리트코드 179번

class Solution:

    @staticmethod
    def to_swap(n1: int, n2: int):
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))


# 리트코드 242번

def isAnagram(self, s: str, t: str) -> bool:

    return sorted(s) == sorted(t)


# 리트코드 75번

def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


# 리트코드 973번

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    heap = []
    for (x, y) in points:
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heap)
        result.append((x, y))
    
    return result