import math

def task_1():
    A = float(input("Введіть значення A: "))
    B = float(input("Введіть значення B: "))

    # Виведення початкових значень
    print(f"\nПочаткові значення:")
    print(f"A = {A}")
    print(f"B = {B}")

    # Перевірка та обмін значень
    if A > B:
        A, B = B, A

    # Виведення результату
    print(f"\nРезультат після перерозподілу:")
    print(f"A = {A}")
    print(f"B = {B}")

def task_2():
    try:
        a = float(input("a (сторона квадрата) = "))
        r = a / 2  # Радіус кола = a / 2
        if a <= 0:
            raise ValueError
    except ValueError:
        print("Невірні значення a")
    else:
        # Введення координат точок для перевірки
        x_y_list = []
        try:
            n = int(input("N (кількість точок) = "))
            for i in range(n):
                x_i = float(input(f"\nX{i + 1} = "))
                y_i = float(input(f"Y{i + 1} = "))
                x_y_list.append((x_i, y_i))
        except ValueError:
            print("Невірні значення n, x або y")
        else:
            in_count = 0

            for x, y in x_y_list:
                # Перевірка для правого нижнього сектора (поза колом)
                if a / 2 <= x <= a and -a / 2 <= y <= 0:
                    length = math.sqrt(x**2 + y**2)
                    if length >= r:
                        in_count += 1

                # Перевірка для лівого нижнього сектора (всередині кола)
                elif -a <= x > -a / 2 and -a / 2 <= y <= 0:
                    length = math.sqrt(x**2 + y**2)
                    if length <= r:
                        in_count += 1

            print("Кількість точок у помаранчевих зонах = {}".format(in_count))

def task_3():
    n = 1
    s = 0
    e = 1e-10
    g = 1e+5

    while True:
        try:
            num = n**3 * math.exp(2 * n + 1)
            denom = math.factorial(n)
            u = num / denom
        except ValueError:
            print("Помилка значень!")
            break
        except ZeroDivisionError:
            print("Ділення на нуль!")
            break
        else:
            s += u
            print(f"n = {n}, u_n = {u}, поточна сума = {s}")
            n += 1

            if abs(u) < e:
                print(f"Ряд збігається до суми {s}")
                break
            elif abs(u) > g:
                print("Ряд розбігається")
                break

def main_menu():
    """Головне меню вибору завдань."""
    while True:
        print("\nОберіть завдання:")
        print("1. Обмін значень A та B")
        print("2. Точки у помаранчевих зонах")
        print("3. Обчислення ряду")
        print("4. Вийти")

        choice = input("\nВаш вибір: ")

        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "3":
            task_3()
        elif choice == "4":
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Спробуйте знову.")

# Виклик головного меню
main_menu()
