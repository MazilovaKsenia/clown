x = input("Введите цвет: ")
y = input("Введите цвет: ")
q = "Красный"
w = "Синий"
r = "Желтый"
if x == q and y == w:
    print("Фиолетовый")
elif x == q and y == r:
    print("Оранжевый")
elif x == w and y == r:
    print("Зеленый")
else:
    print("Ошибка")
