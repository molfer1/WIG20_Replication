import openpyxl
import lxml
import pandas as pd
import requests
import xlsxwriter
from bs4 import BeautifulSoup

input = pd.read_excel("input_data.xlsx", sheet_name="data")

stock_prices = []
stocks = []
dates = []
share_count = []

start_valuation = 1000.00
index_valuation = []
benchmark_valuation = []


def get_stock_data():
    r = requests.get('https://www.biznesradar.pl/notowania-historyczne/WIG20')
    dataframe = pd.read_html(r.text)
    for el_2 in dataframe[0].iloc[:40].iterrows():
        index_valuation.append(el_2[1]['Zamknięcie'])
    index_valuation.reverse()

    get_dates = True
    for el in input.iterrows():
        stock_list = []
        stock = el[1]
        req = requests.get(f'https://www.biznesradar.pl/notowania-historyczne/{stock["spolka"]}')
        stocks.append(stock['spolka'])
        share_count.append(int(stock['Pakiet'].replace(" ", "")))
        df_list = pd.read_html(req.text)
        if get_dates:
            for el_3 in df_list[0].iloc[:40].iterrows():
                dates.append(el_3[1]['Data'])
        for el_2 in df_list[0].iloc[:40].iterrows():
            stock_list.append(el_2[1]['Zamknięcie'])
        stock_list.reverse()
        stock_prices.append(stock_list)
        get_dates = False
    dates.reverse()


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (current - previous) / previous
    except ZeroDivisionError:
        return 0


def count_benchmark_data():
    for i in range(0, len(dates)):
        # print(f'XDDDDDDDDDDDDDDDDDDDDDDDDDDDD{i}')
        market_caps = []
        index_share = []
        for j in range(0, len(stocks)):
            market_caps.append(float(share_count[j]) * float(stock_prices[j][i]))
        market_caps_sum = 0
        for el in market_caps:
            market_caps_sum += el
        for n in range(0, len(stocks)):
            index_share.append(round(market_caps[n] / market_caps_sum, 5))
        count_benchmark_valuation(index_share, i)


def count_benchmark_valuation(index_share, i):
    # print(index_share)
    if len(benchmark_valuation) == 0:
        benchmark_valuation.append(start_valuation)
        return
    else:
        difference = 0
        # print("i: " + str(i))
        # print(benchmark_valuation)
        # print(index_share)
        for n in range(0, len(stock_prices)):
            difference += get_change(stock_prices[n][i], stock_prices[n][i - 1]) * index_share[n]

            # print(f'spolka: {stocks[n]}, iteracja: {dates[i]}, difference: {difference}, current_price: {stock_prices[n][i]}, previous_price: {stock_prices[n][i - 1]}, index_share: {index_share[n]}, get_change: {get_change(stock_prices[n][i], stock_prices[n][i - 1])}')
        diff = 1 + difference
        # if diff > 0.09:
        #     print(f'difference: {diff}, iteracja: {dates[i]}')
        val = diff * benchmark_valuation[i - 1]

        benchmark_valuation.append(round(val, 2))


def get_output():
    df = pd.DataFrame(columns=['data', 'WIG20', 'benchmark'])
    df['data'] = dates
    df['WIG20'] = index_valuation
    df['benchmark'] = benchmark_valuation
    df.to_excel("wynik.xlsx", sheet_name="zadanie 2")

get_stock_data()
count_benchmark_data()
get_output()
# print(f"stock_prices: {stock_prices}")
# print(stocks)
# print(f"dates: {dates}")
# print(share_count)
# print(index_share)
# print(f"index_valuation: {index_valuation}")
# print(f"benchmark_valuation: {benchmark_valuation}")
