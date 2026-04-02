import json, csv
from datetime import datetime

LOG = 'converter_log.txt'

def log(msg):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [data] if isinstance(data, dict) else data

def load_csv(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    headers = lines[0].strip().split('\t')
    return [{headers[i]: v for i, v in enumerate(line.strip().split('\t'))} for line in lines[1:] if line.strip()]

def save_json(data, path):
    out = data[0] if len(data) == 1 else data
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=4)

def save_csv(data, path):
    if not data: return
    with open(path, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        w.writeheader()
        for row in data:
            w.writerow({k: ', '.join(v) if isinstance(v, list) else v for k, v in row.items()})

def save_txt(data, path):
    if not data: return
    with open(path, 'w', encoding='utf-8') as f:
        headers = list(data[0].keys())
        f.write('\t'.join(headers) + '\n')
        for row in data:
            vals = [', '.join(row.get(h, '')) if isinstance(row.get(h), list) else str(row.get(h, '')) for h in headers]
            f.write('\t'.join(vals) + '\n')

LOADERS = {'json': load_json, 'csv': load_csv, 'txt': load_txt}
SAVERS = {'json': save_json, 'csv': save_csv, 'txt': save_txt}

print("=" * 40)
print("КОНВЕРТЕР: JSON - CSV - TXT")
print("=" * 40)

fr = input("\nИз формата (json/csv/txt): ").lower()
to = input("В формат (json/csv/txt): ").lower()

if fr not in LOADERS or to not in SAVERS:
    print("✗ Неверный формат!")
else:
    src = input("Исходный файл: ").strip()
    dst = input("Выходной файл: ").strip()
    
    log(f"{fr.upper()} → {to.upper()} | {src} → {dst}")
    
    try:
        data = LOADERS[fr](src)
        SAVERS[to](data, dst)
        print(f"\n Готово! Записей: {len(data)}")
        log(f" Успешно ({len(data)} записей)")
    except Exception as e:
        print(f"\n Ошибка: {e}")
        log(f" Ошибка: {e}")