import re
from collections import Counter

REPORT_FILE = 'analysis_report.txt'

try:
    with open('example.txt', 'r', encoding='utf-8') as f:
          text = f.read()
    lines = len(text.splitlines())
    chars = len(text)
    words = re.findall(r'[а-яА-Яa-zA-Z]+', text.lower())
    word_count = len(words)
    freq = Counter(words)

    print("=" * 40)
    print("СТАТИСТИКА")
    print("=" * 40)
    print(f"Строк:        {lines}")
    print(f"Слов:         {word_count}")
    print(f"Символов:     {chars}")
    print(f"Уникальных:   {len(freq)}")
    print("\nТОП-5 слов:")

    for i, (word, count) in enumerate(freq.most_common(5), 1):
        print(f"{i}. {word} — {count}")
    
    # 4. Запись отчёта в файл
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("ОТЧЁТ ПО АНАЛИЗУ ФАЙЛА\n")
        f.write("=" * 40 + "\n")
        f.write(f"Строк: {lines}\n")
        f.write(f"Слов: {word_count}\n")
        f.write(f"Символов: {chars}\n\n")
        f.write("ТОП-5 СЛОВ:\n")
        for word, count in freq.most_common(5):
            f.write(f"{word}: {count}\n")


except FileNotFoundError:
    print(f"Ошибка: файл {'example.txt'} не найден!")
except PermissionError:
    print("Ошибка: нет доступа к файлу!")
except Exception as e:
    print(f"Ошибка: {e}")

