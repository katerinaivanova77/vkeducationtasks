n = int(input())
def pascal_triangle(n):
    triangle = []
    for row in range(n):
        current_row = [1] * (row + 1)
        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        triangle.append(current_row)
    return triangle
triangle = pascal_triangle(n)
for row in triangle:
    print(*row)

#Новая строка формируется концами по 1, далее внутренние элементы составляются из сложения соседей, а те, что снизу по принципу верхнего левого и правого соседа. Если проходим n строк, то сложность O(n^2) (так как основа в соседях)