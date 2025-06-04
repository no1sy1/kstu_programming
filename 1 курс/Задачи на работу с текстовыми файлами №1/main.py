#1
filename = 'numbers.txt'
sum = 0
count = 0
with open(filename, 'r') as file:
    for line in file:
        parts = line.split()
        for part in parts:
            sum += float(part)
            count += 1
average = sum / count if count > 0 else 0
print(f"Среднее арифметическое: {average}")

#2
filename = 'numbers.txt'
numbers = []
with open(filename, 'r') as file:
    for line in file:
        parts = line.split()
        for part in parts:
            if part.isdigit():
                numbers.append(float(part))
if numbers:
    min_num = min(numbers)
    max_num = max(numbers)
    print(f"Наименьшее число: {min_num}\nНаибольшее число: {max_num}")
else:
    print("В файле нет чисел.")

#3
input_file = 'numbers.txt'
output_file = 'even_numbers.txt'
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        parts = line.split()
        for part in parts:
            if part.isdigit() and int(part) % 2 == 0:
                outfile.write(part + '\n')

#4
filename = 'text.txt'
line_count = 0
with open(filename, 'r') as file:
    for _ in file:
        line_count += 1
print(f"Количество строк: {line_count}")

#5
filename = 'My_text.txt'
word_count = 0
with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        word_count += len(words)
print(f"Количество слов: {word_count}")

#6
filename = 'text.txt'
old_word = input("Введите слово для замены: ")
new_word = input("Введите новое слово: ")
with open(filename, 'r') as file:
    content = file.read()
updated_content = content.replace(old_word, new_word)
with open(filename, 'w') as file:
    file.write(updated_content)
