import csv
from .models import LinesForTyping

def import_lines(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            LinesForTyping.objects.create(
                Character=row['Character'],
                Line=row['Line']
            )

if __name__ == '__main__':
    csv_file_path = 'static/typeLines.csv'
    import_lines(csv_file_path)