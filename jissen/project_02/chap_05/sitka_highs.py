import csv

filename = 'jissen/project_02/chap_05/data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # ファイルから最高気温を取得する
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
