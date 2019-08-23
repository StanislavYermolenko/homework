#За допомогою циклу for & while розв'язати наступні задачі:
#1. Знайти максимальне число в списку
# for
a = [1, 56, 76, 8, 9]
max_number = 0

for i in a:
    if i > max_number:
           max_number = i
print(max_number)
# while
a = [75, 98, 65, 98, 78, 67, 76]
max_number = 0
i = 0
while i < len(a):

    if a[i] > max_number:
        max_number = a[i]
    i += 1
print(max_number)

#2. Знайти суму всіх чисел в списку що діляться на 3
# for
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 0
for i in a:
    if i % 3 == 0:
        s += i
print(s)

# другий спосіб
print(sum(i for i in range(1, 9) if i % 3 == 0))

#3. Знайти суму простих чисел у списку
# for
def is_simple(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, ]
s = 0

for i in a:
    if is_simple(i):
        s += i

print(s)
# while

def is_simple(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, ]
s = 0
i = 0
while i < len(a):

    if is_simple(i):
        s += i

    i += 1

print(s)

#Задача яку обговорювади в кінці зайняття: зробити зі списка новий список
# елементами якого будуть добуток всіх чисел масива
# крім поточного: [1,2,3,4] ---> [24, 12, 8, 6]
a = [1, 2, 3, 4]
b = 1
for i in a:
    b *= i
print([b//a[0], b//a[1], b//a[2], b//a[3]])

# за допомогою for знайти перші 100 чисел фібоначи
a = [0, 1]
for i in range(0, 98):
    a.append(a[-1]+a[-2])
for i in a:
        print(str(a), end=' ')