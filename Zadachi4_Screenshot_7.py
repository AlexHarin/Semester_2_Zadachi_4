import pandas as pd

file_path = 'specail.csv'
data = pd.read_csv(file_path)


for column in data.columns:
    print("Статистика для столбца", column)
    print("Среднее значение:", data[column].mean())
    print("Медиана:", data[column].median())
    print("Минимальное значение:", data[column].min())
    print("Максимальное значение:", data[column].max())
    print("Сумма:", data[column].sum())
    print("Количество уникальных значений:", data[column].nunique())
    print("\n")
