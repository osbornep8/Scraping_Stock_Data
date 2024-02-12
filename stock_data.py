import requests
from datetime import datetime
import time


ticker = input('Enter stock symbol: ')
from_date = input('Enter start data in "DD/MM/YYYY" format: ')
to_date = input('Enter end data in "DD/MM/YYYY" format: ')

from_datetime = datetime.strptime(from_date, '%d/%m/%Y')
to_datetime = datetime.strptime(to_date, '%d/%m/%Y')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))





headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'
content = requests.get(url, headers=headers).content
# print(content)

with open(f'{ticker}_stock_data.csv', 'wb') as file:
    file.write(content)