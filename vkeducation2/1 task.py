arr = list(map(int, input().split()))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(arr[0])
current = head
for val in arr[1:]:
    current.next = ListNode(val)
    current = current.next
prev = None
current = head
while current:
    next_temp = current.next
    current.next = prev
    prev = current
    current = next_temp
head = prev
current = head
while current:
    print(current.val, end=" ")
    current = current.next