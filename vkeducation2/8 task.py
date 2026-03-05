arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def spisok(arr):
    arr.sort()
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def merge(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return dummy.next
def print_spisok(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()
list1 = spisok(arr1)
list2 = spisok(arr2)
merged = merge(list1, list2)
print("Объединённый список:")
print_spisok(merged)