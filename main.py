import requests
import csv

def get_google_sheet_data(spreadsheet_id, sheet_id):
    # URL для получения данных в формате CSV из Google Sheets
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?gid={sheet_id}&format=csv"
    
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешность запроса
    
    return response.text

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

# Ваш идентификатор таблицы и ID листа
spreadsheet_id = '1RfAnpdQZ8ow1Cb4B8WjJbNO79QX0Ii0OkuG7XFJMh3Y'
sheet_id = '69322794'

# Получаем данные из таблицы
csv_data = get_google_sheet_data(spreadsheet_id, sheet_id)

# Преобразуем данные из CSV текста в список строк
import csv
from io import StringIO

csv_data_io = StringIO(csv_data)
reader = csv.reader(csv_data_io)
data = [row for row in reader]

# Сохраняем данные в CSV файл
output_filename = 'output.csv'
save_to_csv(data, output_filename)

print(f"Данные успешно сохранены в файл {output_filename}")
