# Импортируем библиотеки
from math import *


def solve(a, b, c) -> tuple:
    # Считаем дискриминант
    D = b ** 2 - 4 * a * c

    # Проверяем знак дискриминанта
    if D > 0:
        # Два вещественных корня
        x1, x2 = (-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a)

        # Убираем лишние нули после точки (если есть)
        if x1 % 1 == 0:
            x1 = int(x1)
        if x2 % 1 == 0:
            x2 = int(x2)
        return x1, x2
    elif D == 0:
        # Один вещественный корень
        x1 = -b / (2 * a)

        # Убираем лишние нули после точки (если есть)
        if x1 % 1 == 0:
            x1 = int(x1)
        return (x1)
    else:
        # Два комплексных корня
        real_part, imag_part = -b / (2 * a), sqrt(abs(D)) / (2 * a)

        # Убираем лишние нули после точки (если есть)
        if real_part % 1 == 0:
            real_part = int(real_part)
        if imag_part % 1 == 0:
            imag_part = int(imag_part)
        return complex(real_part, -imag_part), complex(real_part, imag_part)
    

def main() -> None:
    # Обработка входных данных
    print('Уравнение имеет вид: ax^2+bx+c=0')
    a, b, c = list(map(float, input('Впишите a, b и c (Через пробел):').split()))

    # Проверка, является ли уравнение квадратным
    if a == 0:
        print('Уравнение не является квадратным, так как a = 0')
    else:
        # Получаем корни
        solutions = solve(a, b, c)

        # Выводим ответ
        print('Ответ:')
        if len(solutions) == 1:
            print(f'x1 = x2 = {solutions[0]}')
        else:
            print(f'x1 = {solutions[0]}\nx2 = {solutions[1]}')

main()
