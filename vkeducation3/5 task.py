n = int(input())
data = list(map(int, input().split()))
target = int(input())
def two_sum(data: list[int], target: int) -> list[int]:
    sl = {}
    for i, v in enumerate(data):
        diff = target - v
        if diff in sl:
            return [sl[diff], i]
        sl[v] = i
    return []
print(two_sum(data, target))

#Ради каждого элемента мы не запускаем цикл заново, так как по сути спрашиваем у программы, видела ли она такое число или нет и она достает с помощью словаря ответ на этот вопрос без дополнительного прохода по массиву