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