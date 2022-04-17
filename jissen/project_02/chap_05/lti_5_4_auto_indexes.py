import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(filename):
    """ファイルから最高気温と最低気温を取得する"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # 各項目のインデックスを取得する
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')

        # ファイルから日付、最高気温、最低気温を取得する
        dates, highs, lows = [], [], []
        place_name = ''
        for row in reader:
            # 観測所の名前が設定されていない場合、名前を取得す
            if not place_name:
                place_name = row[name_index]
                print(place_name)
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows

# シトカの天気のデータを取得する
filename = 'jissen/project_02/chap_05/data/sitka_weather_2018_simple.csv'
dates, highs, lows = get_weather_data(filename)

# シトカの天気データをグラフに描画する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# デス・バレーの天気を取得する
filename = 'jissen/project_02/chap_05/data/death_valley_2018_simple.csv'
dates, highs, lows = get_weather_data(filename)

# デス・バレーの天気データをグラフに描画する
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# グラフにフォーマットを指定する
title = "Daily high and low temperatures - 2018"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.savefig('jissen/project_02/chap_05/lti_5_4_sitka_death_valley.png')
plt.show()
