s = input().strip()
def palindrome(s):
    if len(s) == 0:
        return ""
    best_left = 0
    best_right = 0
    def cent(left, right):
        nonlocal best_left, best_right
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > best_right - best_left:
                best_left = left
                best_right = right
            left -= 1
            right += 1
    for i in range(len(s)):
        cent(i, i)
        cent(i, i + 1)
    return s[best_left:best_right + 1]
print(palindrome(s))

#Сложность O(n^2), так как в центров палиндромов у нас ghbvthyj 2n, в худшем случае нам надо искать по длине n.