# Вариант с try/except
flag = True
while flag:
    print("Let's get start")
    try:
        a = input("Введите число: ")
        if a == 's':
            break
        
        b = input("Введите второе число: ")
        result = int(a) / int(b)
        
    except ValueError:
        print("Вводите числа")
    except ZeroDivisionError:
        print("You can not divide by 0")
    else:
        print("Result: ", result)
    finally:
        print("Finita la comedion")
