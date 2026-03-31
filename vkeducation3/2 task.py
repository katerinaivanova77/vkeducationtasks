N, x, y = map(int, input().split())
def copirka(N: int, x: int, y: int) -> int:
    if N == 1:
        return min(x, y)
    left = 0
    right = (N - 1) * max(x, y)
    while left < right:
        mid = (left + right) // 2
        copy = mid // x + mid // y
        if copy >= N - 1:
            right = mid
        else:
            left = mid + 1
    return left + min(x, y)
print(copirka(N, x, y))

#Даже если оставшиеся N-1 копий делать самым медленным способом, этого хватит, поэтому именно так мы определяем правую границу, а первую копию мы посчитаем отдельно - min(x,y)