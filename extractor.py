import requests
import json


def fetch_data():
    try:
        x = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=10&page=1')

        if 200 == x.status_code:
            raw_data = x.json()

            print(type(raw_data))

            with open('raw_test.json', 'w', encoding='utf-8') as f:
                json.dump(raw_data, f, ensure_ascii=False, indent=4)

            with open('raw_test.json', 'r', encoding='utf-8') as rf:
                load_data = json.load(rf)
                print(type(load_data))

        else:
            print(f'failed extracted, the error reminder is {x.status_code}')

    except Exception as e:
        print(f'error message: {e}')
