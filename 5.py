words = input("Введите список слов через запятую: ").split(",")
word_set = set(words)
print(f"Количество слов в списке: {len(words)}")

new_words = []
while len(new_words) < len(words):
    new_word = input(f"Введите слово длиной {len(words[0])} символов: ")
    if len(new_word) == len(words[0]):
        new_words.append(new_word)
    else:
        print(f"Слово должно быть длиной {len(words[0])} символов")

dictionary = dict(zip(words, new_words))
print(dictionary)
