arr = list(map(int, input().split()))
val = int(input())
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def spisok(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_spisok(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()
def remove_elements(head, val):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
head = spisok(arr)
head = remove_elements(head, val)
print("После удаления:")
print_spisok(head)