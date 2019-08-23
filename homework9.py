# Створити класс людина, в якого є атрибут ріст - зробити неможливим введення
# невалідного росту ( валідним є від 40см до 240см )
# Написати декоратор який робить паузу в одну секунду перед виконанням функції
import time
def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(1)
        return f(*args, **kwargs)

    return tmp

class People:

    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 40:
            self.__height = 40
        elif height > 240:
            self.__height = 240
        else:
            self.__height = height

    @pause
    def getPeopleHeight(self):
        return str(self.height)


heightTOOHIGH = People(270)
print(heightTOOHIGH.getPeopleHeight())

heightTOOLOW = People(33)
print(heightTOOLOW.getPeopleHeight())

# Написати декоратор який робить паузу в одну секунду перед виконанням функції
import time

def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(1)
        return f(*args, **kwargs)

    return tmp

x = 10
y = 15
@pause
def func(x, y):
    return x * y

print(func(x, y))
