# Ввод строки
text = input("Введите строку: ")

# Создаём наборы гласных и согласных букв
vowels = "аеёиоуыэюяaeiou"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

# Счётчики символов
vowel_count = 0
consonant_count = 0
digit_count = 0

# Перебираем символы строки
for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char.isdigit():
        digit_count += 1

# Выводим результаты
print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)
print("Количество цифр:", digit_count)