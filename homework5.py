# 1. за допомогою map перетворити числа в списку на їх дзеркальні 123 -> 321
a = [1, 2, 3]

a = ''.join(str(i) for i in a)
print(a)

b = list(map(lambda x: a[::-1], a))

b = ''.join(str(i) for i in b)
print(b)

# 2. за допомогою filter залишити в списку слова довжина яких більше 5 букв
a = ['qwerty', 'tyuiodj', 'hjjb', 'hjh', 'kjkjlkjl']

b = list(filter(lambda x: len(x) > 5, a))
print(b)

