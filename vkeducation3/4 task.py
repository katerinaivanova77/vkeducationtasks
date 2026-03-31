a = input().strip()
b = input().strip()
def ex_buk(a: str, b: str) -> str:
    sl = {}
    for ch in b:
        sl[ch] = sl.get(ch, 0) + 1
    for ch in a:
        if ch in sl:
            sl[ch] -= 1
    for ch, count in sl.items():
        if count > 0:
            return ch
    return ""
print(ex_buk(a, b))

#Подсчет символов используем как раз для нахождения лишней буквы, так как если счетчик больше 0, значит буква нашлась и мы ее и возвращаем