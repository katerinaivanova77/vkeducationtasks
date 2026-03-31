n =int(input())
def square(n: int) -> int:
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(square(n))

#Здесь мы используем бинарный поиск, поэтому сложность алгоритма будет O(log(n)), так как каждый раз мы делим выборку "напополам". Граница поиска определяется крайними значениями#