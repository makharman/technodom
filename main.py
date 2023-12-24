'Найти в API сайта технодома URL для получения смартфонов от Apple. Попробовать получить данные и сохранить в apple.json ТОЛЬКО те смартфоны у которых память 256Гб ИЗ ПЕРВЫХ 20 смартфонов.'

import requests
from bs4 import BeautifulSoup
import json

count = 0
all_data = []

for i in range(1, 4):
    url = f'https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=apple&page={i}&sorting=score&price=0'
    response = requests.get(url)
    data = response.json()

    for product in data.get('payload', []):
        product_title = product.get('title', '')

        if "256" in product_title:
            print(f'{product_title}\n')
            count += 1

            all_data.append({'title': product_title})

        if count >= 20:
            break

with open('apple.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)
