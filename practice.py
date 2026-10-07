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


# x = int(input())  # king по этим координатам
# y = int(input())
# x2 = int(input())  # может ли пререйти на эти координаты
# y2 = int(input())
# if (
#     (x2 == x + 1 or x2 == x - 1)
#     and (y2 == y + 1 or y2 == y - 1)
#     or (x2 == x and (y2 == y + 1 or y2 == y - 1))
#     or (y2 == y and (x2 == x + 1 or x2 == x - 1))
# ):
#     print("YES")
# else:
#     print("NO")


# angle = int(input("Введите угол в градусах: "))

# if angle % 90 == 0:
#     if angle == 0:
#         print('Нулевой')
#     elif angle == 90:
#         print('Прямой')
#     elif angle == 180:
#         print('Развёрнутый')
# else:
#     if 0 < angle < 90:
#         print('Острый')
#     elif 90 < angle < 180:
#         print('Тупой')
#     elif 180 < angle < 270:
#         print('Выпуклый')
#     else:
#         print('Ни острый, ни тупой, ни выпуклый')

# n, k = int(input()), int(input())
# if n > k:
#     print("NO")
# elif n < k:
#     print("YES")
# else:
#     print("Don't know")

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c or c < b < a:
#     print(b)
# elif b < c < a or a < c < b:
#     print(c)
# elif c < a < b or b < a < c:
#     print(a)

# month = int(input("Введите номер месяца: "))
# if month == 12 or month == 5 or month == 1 or month == 3 or month == 7 or month == 8 or month == 10:
#     print("31")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("30")
# elif month == 2:
#     print("28")


# ves = int(input("Введите вес: "))
# if ves < 60:
#     print("Легкий вес")
# elif ves < 64:
#     print("Первый полусредний вес")
# elif ves < 69:
#     print("Полусредний вес")


# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# sim = input("Введите знак: ")
# if sim == "+":
#     print(a + b)
# elif sim == "-":
#     print(a - b)
# elif sim == "*":
#     print(a * b)
# elif sim == "/":
#     if b == 0:
#         print("На ноль делить нельзя!")
#     elif b != 0:
#         print(a / b)
# else:
#     print("Неверная операция")


# a = input()
# b = input()
# if a == b == "красный":
#     print("красный")
# elif a == b == "синий":
#     print("синий")
# elif a == b == "желтый":
#     print("желтый")
# elif (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
#     print("фиолетовый")
# elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
#     print("оранжевый")
# elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
#     print("зеленый")
# else:
#     print("ошибка цвета")


# a = int(input("Введите число: "))
# if a == 0:
#     print("зеленый")
# elif 1 <= a <= 10:
#     if a % 2 == 0:
#         print("черный")
#     if a % 2 != 0:
#         print("красный")
# elif 11 <= a <= 18:
#     if a % 2 == 0:
#         print("красный")
#     if a % 2 != 0:
#         print("черный")
# elif 19 <= a <= 28:
#     if a % 2 == 0:
#         print("черный")
#     if a % 2 != 0:
#         print("красный")
# elif 29 <= a <= 36:
#     if a % 2 == 0:
#         print("красный")
#     if a % 2 != 0:
#         print("черный")
# else:
#     print("ошибка ввода")


# a = int(input())
# b = int(input())
# a2 = int(input())
# b2 = int(input())

# if a > a2:
#     left = a
# else:
#     left = a2

# if b < b2:
#     right = b
# else:
#     right = b2

# if left > right:
#     print("пустое множество")
# elif left == right:
#     print(left)
# else:
#     print(left, right)


# year = int(input())
# if (year // 10**0) % 10 == 0 and (year // 10**1) % 10 == 0:
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 in [1, 3, 5, 7] and y1 in [1, 3, 5, 7]) or (x1 in [2, 4, 6, 8] and y1 in [2, 4, 6, 8]):
#     color1 = "светлый"
# else:
#     color1 = "темный"
# if (x2 in [1, 3, 5, 7] and y2 in [2, 4, 6, 8]) or (x2 in [2, 4, 6, 8] and y2 in [1, 3, 5, 7]):
#     color2 = "темный"
# else:
#     color2 = "светлый"

# if color1 == color2:
#     print("YES")
# else:
#     print("NO")


# year = int(input())
# pol = input()
# if 10 <= year <=15 and pol == "f":
#     print("YES")
# else:
#     print("NO")


# num = int(input())
# if num == 1:
#     print("I")
# elif num == 2:
#     print("II")
# elif num == 3:
#     print("III")
# elif num == 4:
#     print("IV")
# elif num == 5:
#     print("V")
# elif num == 6:
#     print("VI")
# elif num == 7:
#     print("VII")
# elif num == 8:
#     print("VIII")
# elif num == 9:
#     print("IX")
# elif num == 10:
#     print("X")
# else:
#     print("ошибка")

# num = int(input())
# romans = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
# if 1 <= num <= 10:
#     print(romans[num])
# else:
#     print("ошибка")


# a = int(input())
# if a % 2 != 0:
#     print("YES")
# elif a % 2 == 0:
#     if 2 <= a <= 5:
#         print("NO")
#     elif 6 <= a <= 20:
#         print("YES")
#     elif a > 20:
#         print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 + y1 == x2 + y2) or (x1 - y1 == x2 - y2):
#     print("YES")
# else:
#     print("NO")


# if abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if ((x2 == x1 + 2 or x2 == x1 - 2) and (y2 == y1 + 1 or y2 == y1 - 1)) or ((y2 == y1 + 2 or y2 == y1 - 2) and (x2 == x1 - 1 or x2 == x1 + 1)):
#     print("YES")
# else:
#     print("NO")


# a = float(input())
# b = float(input())
# print(a * b * 0.5)

# s = float(input())
# a1 = float(input())
# a2 = float(input())
# print(s / (a1 + a2))

# a = float(input())
# if a == 0:
#     print("Обратного числа не существует")
# else:
#     print(a ** -1)

# far = float(input())
# print((far - 32) * 5 / 9)

# year = int(input())
# if year <= 2:
#     print(year * 10.5)
# else:
#     print((year - 2) * 4 + 10.5 * 2)

# a = float(input())
# print(a % int(a))

# a = float(input())
# b = (a - int(a)) *10
# print(int(b))

# a = list(int(input()) for i in range(5))
# print("Наименьшее число =", min(a))
# print("Наибольшее число =", max(a))


# a = [float(input()) for i in range(5)]
# print(sum(map(abs, a)))

# total = sum(abs(float(input())) for _ in range(5))
# print(total)

# a_min, a_mid, a_max = map(int, sorted(input()))
# if a_max - a_min == a_mid:
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# nums = sorted([int(input()) for _ in range(3)], reverse=True)
# print(*nums, sep='\n')

# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# print(abs(p1 - q1) + abs(p2 - q2))