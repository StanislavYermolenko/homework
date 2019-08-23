#Написати функції що:

# 1. перевіряє чи число є простим
# 2. функцію що рахує суму елементів по діагоналі в матриці
# 3. функцію що перевіряє чи є строка панаграмою
# 4. за допомогою рекурсії порахувати суму елементів списку

# 1. перевірка на просте число
n = 5
def prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(prime(n))

# сума елементів по діагоналі в матриці
matrix = [[i+j for j in range(5)] for i in range(5)]

for row in matrix:
    print(" ".join(list(map(str, row))))

diagonalSum = sum([matrix[i][i] for i in range(len(matrix))])

print(diagonalSum)

# 3. функція що перевіряє чи є строка панаграмою
str = 'The five boxing wizards jump quickly'

def ispangram(str):
    return len(set(str.lower().replace(" ", ""))) == 26

a = ispangram(str)
print(a)

# 4. за допомогою рекурсії порахувати суму елементів списку
x = [1, 2, 3, 4, 5, 6, 7]
def sum(x):
    if len(x) == 0:
        return 0
    else:
        return(x[0] + sum(x[1:]))

z = sum(x)
print(z)

