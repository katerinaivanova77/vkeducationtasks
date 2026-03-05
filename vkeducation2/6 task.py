s = input()
def is_Palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
if is_Palindrome(s):
    print(f"{s} является палиндромом")
else:
    print(f"{s} не является палиндромом")