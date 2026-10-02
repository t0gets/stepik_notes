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


a = int(input())
print(a + a * 11 + a * 111)

git config --global user.name "t0gets" 
git config --global user.email "pst0gets@gmail.com"

