import requests
import csv
from io import StringIO

def get_google_sheet_data(spreadsheet_id, sheet_id):
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?gid={sheet_id}&format=csv"
    
    response = requests.get(url)
    response.raise_for_status()
    
    response.encoding = 'utf-8'
    
    csv_data = StringIO(response.text)
    reader = csv.reader(csv_data)
    data = [row for row in reader]
    
    return data

def save_data_to_file(data, file='output.csv'):
    with open(file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

