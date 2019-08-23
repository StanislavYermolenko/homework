
#1. a=”10”, b=”15”, a і b – це строки, обчислити b/a
a = "10"
b = "15"
a = int(a)
b = int(b)
print(b/a)

#2. створити словник в якому вказати основні дані про себе,
#словник має містить ключі значенням якого є інший словник, а також масив
p = {"name" : ["Stanislav", "Yermolenko"], "address": {"city": "Kyiv","country": "Ukraine"},
     "experience" : {"sales manager": "2001-2004", "manager": "2004-2006",
                          "entrepreneur": "2006 - up to now"},
"duties": ["phone calls", "direct sales", "conclusion of contracts", "customer negotiations", 18]
}
print(p.keys())# перевірка всіх ключів
print(p["experience"]['entrepreneur'])


#3. створити масив з 10 елементів і перетворити його в tuple, вивісти зріз перших трьої елементів
a = [1, 2, 3, 4, 5, [1.022], "hu55", "klk", 15, 16]
a = tuple(a)
print(a[:3])

#4. a, b – сторони прямокутника, знайти площу прямокутника.
# Якщо a=b, використати формулу площи квадрата
a = 5
b = 7
if a == b:
    s = a*b
else:
    s = a**2
    print(s)

#5. Є три числа, знайти найменше.

a = 1
b = 2
c = 3

if a < b and a < c:
    print(a)
elif b < c and b < a:
    print(b)
elif c < a and c < b:
    print(c)

#6.    Є три числа A, B, C – якщо вони впорядковані по зростанню то до кожного з
# них добавити 3 і вести їх нові значення, якщо ні то вивести їх протилежне число
# ( помножити на -1 ).
A = 3
B = 6
C = 9
n = [A, B, C]

if  A < B < C:
    n = [3 + i for i in n]
    print(n)
else:
    n = [-1 * i for i in n]
    print(n)

#7. Дано три числа. Знайти суму двох найбільших з них.
a = 8
b = 5
c = 3

if a < b:
    x = a
else:
    x = b
if c < x:
    x = c
s = a + b + c - x

print(s)

#8. Створити невпорядкований список з 10 елементів:
# знайти найбільший, найменший елементи, а також сумму елементів.
a = [212, 545, 1234, 5693, 7969, 4545454, 78787, -1554, 6879457, 564]
min_element = min(a)
max_element = max(a)
print(min_element)
print(max_element)
s = sum(a)
print(s)
