s = input("Введите строку: ")
n = len(s) - 1

for i in range(n):
    if i == 2:
        continue
    if s[i] == 'с':
        print("Символ 'c' найден")
    print(s[i], end='')

print("Длина строки:", len(s))


