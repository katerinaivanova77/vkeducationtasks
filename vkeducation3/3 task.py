n = int(input())
animals = list(map(int, input().split()))
m = int(input())
food = list(map(int, input().split()))
def feed_animals(animals: list[int], food: list[int]) -> int:
    animals.sort()
    food.sort()
    c = 0
    for portion in food:
        if c == len(animals):
            break
        if portion >= animals[c]:
            c += 1
    return c
print(feed_animals(animals, food))

#Мы отсортировали потребности животных и их возможные порции, а значит самым нетребовательным даем меньшую порции, значит, реализуем самый эффективный в данном случае алгоритм, то есть "жадный"