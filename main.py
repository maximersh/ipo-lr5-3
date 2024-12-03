# Открытие файла и чтение его содержимого
with open("text.txt", "r", encoding="utf-8") as файл:
    текст = файл.read()

# Разделение текста на слова
слова = текст.split()

# Подсчёт количества слов
количество_слов = len(слова)

# Вывод результата
print(f"Количество слов в файле: {количество_слов}")
