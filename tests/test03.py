# Аналогичное решение без try/except
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("На ноль делить нельзя")
            # raise ValueError("При выполнении команды возникла ошибка")
        else:
            print(int(a) / int(b))
            break
    else:
        print("Поддерживаются только числа")
    