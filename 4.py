#Вводим 3 произвольных слова
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
word3 = input("Введите третье слово: ")

#Выводим слова в разных регистрах
print("Слова в нижнем регистре: {}, {}, {}".format(word1.lower(), word2.lower(), word3.lower()))
print("Слова в верхнем регистре: {}, {}, {}".format(word1.upper(), word2.upper(), word3.upper()))
print("Слова с первой заглавной буквой: {}, {}, {}".format(word1.capitalize(), word2.capitalize(), word3.capitalize()))

#Вводим количество каждого слова
count1 = int(input("Введите количество {}: ".format(word1)))
count2 = int(input("Введите количество {}: ".format(word2)))
count3 = int(input("Введите количество {}: ".format(word3)))

#Выводим данные в читаемом виде
print("Вы ввели:")
print("{}: {}".format(word1.capitalize(), count1))
print("{}: {}".format(word2.capitalize(), count2))
print("{}: {}".format(word3.capitalize(), count3))
