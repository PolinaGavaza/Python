
def create_dict_from_lists():
    words = input("Введите список слов через запятую: ").split(",")
    words_set = set(words)
    print(f"Количество слов в списке: {len(words)}")
    num_words = int(input("Введите количество слов для второго списка: "))
    words2 = []
    for i in range(num_words):
        word = input(f"Введите слово {i+1} с {len(words[0])} символами: ")
        words2.append(word)
    dictionary = dict(zip(words_set, words2))
    print(dictionary)
