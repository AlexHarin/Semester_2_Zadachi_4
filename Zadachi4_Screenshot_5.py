import csv
import sys

csv_file_path = 'special.csv'

column_number = 1

def calculate_sum_in_column(csv_file, column_number):
    total_sum = 0
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                total_sum += float(row[column_number])
            except ValueError:
                continue
    return total_sum

print("Сумма числовых значений в столбце {0}: {1}".format(column_number, calculate_sum_in_column(csv_file_path, column_number)))
