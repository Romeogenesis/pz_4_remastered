import csv

def create_sales_file():
    data = [
        ['Товар', 'Количество', 'Цена_за_единицу'],
        ['Яблоки', '10', '50'],
        ['Бананы', '5', '80'],
        ['Апельсины', '8', '60'],
        ['Груши', '12', '45']
    ]

    with open('sales.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def process_sales():
    total_revenue = 0
    rows_processed = 0

    try:
        with open('sales.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    product = row['Товар']
                
                    quantity = int(row['Количество'])
                    price = float(row['Цена_за_единицу'])
                    
                    cost = quantity * price
                    total_revenue += cost
                    rows_processed += 1
                    
                    print(f"{product} | {quantity} | {price} | {cost}")

                except ValueError as ve:
                    print(f"Ошибка в данных товара '{row.get('Товар', 'Неизвестно')}': некорректное число ({ve})")
                except KeyError as ke:
                    print(f"Ошибка структуры файла: отсутствует колонка {ke}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {'sales.csv'} не найден!")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return
    
    print("-" * 55)
    print(f"{'Общая выручка:'} {total_revenue}")

if __name__ == "__main__":
    create_sales_file()

    process_sales()