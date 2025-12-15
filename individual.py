import math

base1 = float(input("Введите длину первого основания: "))
base2 = float(input("Введите длину второго основания: "))
height = float(input("Введите высоту трапеции: "))

leg_p = abs(base1 - base2) / 2

side = math.sqrt(height**2 + leg_p**2)

perimeter = base1 + base2 + 2 * side

print(f"Периметр трапеции равен: {perimeter:}")