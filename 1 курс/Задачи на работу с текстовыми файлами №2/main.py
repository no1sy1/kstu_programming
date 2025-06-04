import re
import pymorphy3

#1
STOP_WORDS = {"и", "в", "на", "с", "по"}

with open("text_1.txt", 'r', encoding='utf-8') as file:
    text = file.read().lower()

text = re.sub(r'[^а-яё\s]', '', text)
words = text.split()

morph = pymorphy3.MorphAnalyzer()
freq = {}
for word in words:
    if word in STOP_WORDS:
        continue
    parsed = morph.parse(word)[0]
    normal_form = parsed.normal_form
    if normal_form in freq:
        freq[normal_form] += 1
    else:
        freq[normal_form] = 1

sorted_words = sorted(freq.items(), key=lambda x: -x[1])
for word, count in sorted_words[:20]:
    print(f"{word}: {count}")


#2
morph = pymorphy3.MorphAnalyzer()

def process(text):
    words = re.sub(r'[^а-яё\s]', '', text.lower()).split()
    return {morph.parse(w)[0].normal_form for w in words if len(w) > 2}

with open("text_1.txt", 'r', encoding='utf-8') as f1, open("text_2.txt", 'r', encoding='utf-8') as f2:
    set1, set2 = process(f1.read()), process(f2.read())

common = set1 & set2
similarity = len(common) / len(set1 | set2) * 100 if (set1 | set2) else 0

print(f"Схожесть: {similarity:.1f}%\nСовпадающие слова: {', '.join(sorted(common))}")
