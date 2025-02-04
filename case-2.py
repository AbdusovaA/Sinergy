from math import factorial

def fact(f):
    while True:
        try:
            f = int(input('Введите целое неотрицательное число: '))
            if 1500 > f > 0:
                print(factorial(f))
                break
            elif f <= 0:
                print('Ошибка: число отрицательное.')
            else:
                print('Ошибка: число слишком большое')
        except ValueError:
            print("Ошибка: введите целое неотрицательное число.")

fact(5)