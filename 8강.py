# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 리트코드 234번

def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and slow.val == rev.val:
        slow, rev = slow.next, rev.fast

    return not rev


# 리트코드 21번

def mergeTwoLists(self, l1: ListNode, l2: ListNode):
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1


# 리트코드 206번

def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


# 리트코드 2번

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


# 리트코드 24번

def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        head.next = self.swapPairs(p.next)
        p.next = head
        return p

    return head


# 리트코드 328번

def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head

    return head


# 리트코드 92번

def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    root = start = ListNode(None)
    root.next = head

    for _ in range(left - 1):
        start = start.next
    end = start.next

    for _ in range(right - left):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next