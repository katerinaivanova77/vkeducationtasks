arr = list(map(int, input().split()))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def spisok(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def seredina(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
head = spisok(arr)
middle = seredina(head)
print(middle.val)