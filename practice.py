# name, familia, year = input("Ваше имя:"), input("Ваша фамилия:"), input("Полных лет:")
# print("ФИ:", name, familia, "\nПолных лет:", year)


# num = 754
# a = num % 10             # вычисляем последнюю цифру числа
# b = (num % 100) // 10    # вычисляем среднюю цифру числа
# c = num // 100           # вычисляем первую цифру числа

# print(a)
# print(b)
# print(c)


# num = int(input("Введите число: "))  # Запрашиваем у пользователя число
# i = int(input("Введите номер цифры числа с конца: "))  # Запрашиваем у пользователя номер цифры числа
# print((num // 10 ** (i - 1)) % 10)  # Запишем формулу для вычисления i-й цифры n-значного числа num в общем виде


# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)


# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Сумма цифр =', last_digit + first_digit)

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Искомое число =', last_digit * 10 + first_digit)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100

# print(digit1, digit2, digit3, sep=',')


# num = int(input())
# ch3 = num // 100
# ch2 = (num // 10) % 10
# ch1 = num % 10
# print("Сумма цифр =", ch1 + ch2 + ch3)
# print("Произведение цифр =", ch1 * ch2 * ch3)

# num = int(input())
# ch3 = (num // 10**2) % 10
# ch2 = (num // 10**1) % 10
# ch1 = (num // 10**0) % 10
# print(ch3, ch2, ch1, sep="")
# print(ch3, ch1, ch2, sep="")
# print(ch2, ch3, ch1, sep="")
# print(ch2, ch1, ch3, sep="")
# print(ch1, ch3, ch2, sep="")
# print(ch1, ch2, ch3, sep="")

# num = int(input())
# ch4 = (num // 10**3) % 10
# ch3 = (num // 10**2) % 10
# ch2 = (num // 10**1) % 10
# ch1 = (num // 10**0) % 10
# print("Цифра в позиции тысяч равна", ch4)
# print("Цифра в позиции сотен равна", ch3)
# print("Цифра в позиции десятков равна", ch2)
# print("Цифра в позиции единиц равна", ch1)


# print("Python", , "is the best")


# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)


# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)


# print("*" * 17)
# print("*" + " " * 15 + "*")
# print("*" + " " * 15 + "*")
# print("*" * 17)


# a = int(input())
# b = int(input())
# print("Квадрат суммы", a, "и", b, "равен", (a + b) ** 2)
# print("Сумма квадратов", a, "и", b, "равна", a ** 2 + b ** 2)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(a ** b + c ** d)


# a = int(input())
# print(a + a * 11 + a * 111)

# git config --global user.name "t0gets"
# git config --global user.email "pst0gets@gmail.com"


# password, password2 = input("Пароль: "), input("Повторите пароль: ")
# if password == password2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")


# num = int(input("Введите число: "))
# if num % 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")


# year = int(input("Сколько вам полных лет: "))
# if year >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# num1, num2 = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# if num1 > num2:
#     print(num2)
# else:
#     print(num1)


# num1, num2, num3 = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))
# raznitsa1 = num1 - num2
# raznitsa2 = num2 - num3
# if raznitsa1 == raznitsa2:
#     print("YES")
# else:
#     print("NO")


# num = int(input("Введите число четырехзначное: "))
# if ((num // 10**3) % 10) + (num % 10) == ((num // 10**2) % 10) - ((num // 10**1) % 10):
#     print("ДА")
# else:
#     print("НЕТ")


# che1, che2, che3 = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))
# if che1 > 0:
#     che1 = che1
# else:
#     che1 = 0
# if che2 > 0:
#     che2 = che2
# else:
#     che2 = 0
# if che3 > 0:
#     che3 = che3
# else:
#     che3 = 0
# print("Сумма положительных чисел =", che1 + che2 + che3)


# ОБА ПРАВИЛЬНО УРАААА

# year = int(input("Введите ваш возраст: "))
# if year <= 13:
#     print("детство")
# else:
#     if 14 <= year <= 24:
#         print("молодость")
#     else:
#         if 25 <= year <= 59:
#             print("зрелость")
#         else:
#             if year >= 60:
#                 print("старость")

# year = int(input())
# if year <=13:
#     print("детство")
# if year >= 14 and year <= 24:
#     print("молодость")
# if year >= 25 and year <= 59:
#     print("зрелость")
# if year >= 60:
#     print("старость")


# num1, num2, num3, num4 = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")), int(input("Введите четвертое число: "))
# if num1 <= num2 and num1 <= num3 and num1 <= num4:
#     print(num1)
# elif num2 <= num1 and num2 <= num3 and num2 <= num4:
#     print(num2)
# elif num3 <= num1 and num3 <= num2 and num3 <= num4:
#     print(num3)
# else:
#     print(num4)

# !!!!!!!!!!вот они min max
# che = int(input("Сколько чисел будем сравнивать? "))
# nums = [int(input(f"Введите число {i}: ")) for i in range(1, che + 1)]
# print("Наименьшее число:", min(nums))


# river1 = 'Нева'
# river2 = 'Инд'

# print(river1 == 'Буг' and river2 != 'Одер' or river1 == 'Нева')
# print(river1 != 'Эльба' and river1 != 'Сена' and river1 != 'Инд')


# x = int(input())
# if -1 < x < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
# if -3 >= x or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
# if -30 < x <= -2 or 7 < x <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
# if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())
# if a + c > b and a + b > c and b + c > a:
#     print("YES")
# else:
#     print("NO")


# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")


# x = int(input()) # ладья по этим координатам
# y = int(input())
# x2 = int(input()) # может ли пререйти на эти координаты
# y2 = int(input())
# if x == x2 and 1<= y2 <= 8 or y == y2 and 1<= x2 <= 8:
#     print("YES")
# else:
#     print("NO")


x = int(input())  # king по этим координатам
y = int(input())
x2 = int(input())  # может ли пререйти на эти координаты
y2 = int(input())
if (
    (x2 == x + 1 or x2 == x - 1)
    and (y2 == y + 1 or y2 == y - 1)
    or (x2 == x and (y2 == y + 1 or y2 == y - 1))
    or (y2 == y and (x2 == x + 1 or x2 == x - 1))
):
    print("YES")
else:
    print("NO")
