import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import json


def nbu():
    start_date = date(2021, 12, 30)
    end_date = date.today()
    delta = timedelta(days=1)
    end_date -= delta


    with open('nbu.json', 'r') as file:
        data = json.load(file)

    while start_date <= end_date:
        date_str = start_date.strftime("%Y-%m-%d")


        if date_str in data["USD"] and date_str in data["EUR"]:
            start_date += delta
            continue

        url = f"https://index.minfin.com.ua/ua/exchange/archive/nbu/curr/{date_str}/"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select_one(".idx-currency")

        if table == None:
            prev_date = start_date - delta
            prev_date_str = prev_date.strftime("%Y-%m-%d")

            data['USD'][date_str] = {"price": data['USD'][prev_date_str]['price']}
            data['EUR'][date_str] = {"price": data['EUR'][prev_date_str]['price']}
            start_date += delta
            continue

        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            currency = cells[1].text
            price = cells[4].text

            if currency != "USD" and currency != "EUR":
                continue
            print(date_str, currency, price)
            data[currency][date_str] = {"price": price}
        start_date += delta




    with open('nbu.json', 'w') as file:
        json.dump(data, file)

