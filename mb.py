import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import json

def mb():
    start_date = date(2021, 12, 30)
    end_date = date.today()
    delta = timedelta(days=1)
    end_date -= delta

    with open('mb.json', 'r') as file:
        data = json.load(file)

    while start_date <= end_date:
        date_str = start_date.strftime("%Y-%m-%d")


        if date_str in data["USD"] and date_str in data["EUR"]:
            start_date += delta
            continue

        url = f"https://index.minfin.com.ua/ua/exchange/archive/mb/rate/{date_str}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select_one(".idx-currency")

        if table == None:
            prev_date = start_date - delta
            prev_date_str = prev_date.strftime("%Y-%m-%d")

            data['USD'][date_str] = {"buy": data['USD'][prev_date_str]['buy'], "sale": data['USD'][prev_date_str]['sale']}
            data['EUR'][date_str] = {"buy": data['EUR'][prev_date_str]['buy'], "sale": data['EUR'][prev_date_str]['sale']}
            start_date += delta
            continue

        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            currency = cells[0].text
            buy = cells[2].text
            sale = cells[5].text
            # print(date_str, currency, buy, sale)
            if currency != "USD" and currency != "EUR":
                continue
            data[currency][date_str] = {"buy": buy, "sale": sale}
        start_date += delta





    with open('mb.json', 'w') as file:
        json.dump(data, file)




