import requests
import json

counterId = 65607892
token = 'AgAEA7qjTg1sAAaHwZjUGtfCFUZKoeIpTgwBLbg'

def get_id_requests():
        url = f'https://api-metrika.yandex.net/stat/v1/data.csv?id={counterId}&metrics=ym:s:avgPageViews&dimensions=ym:s:operatingSystem&limit=5'
        logs = requests.get(url,headers={"Authorization": f'OAuth {token}'}).text
        print("------------------------------------------\nСПИСОК ЗАПРОСОВ ЛОГОВ:\n------------------------------------------")
        print(logs)
        return

get_id_requests()