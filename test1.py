import requests
import json

counterId = 65607892
token = 'AgAEA7qjTg1sAAaHwZjUGtfCFUZKoeIpTgwBLbg'

def get_id_requests():
        url = f'https://api-metrika.yandex.ru/management/v1/counter/{counterId}/logrequests?metrics=ym:s:visits,ym:s:pageviews&dimensions=ym:s:referer,ym:s:startURLDomain&date1=2020-08-01&date2=yesterday&limit=10000&offset=1'
        logs = json.loads(requests.get(url, 
                                       headers={"Authorization": f'OAuth {token}'}).text)['requests']
        print("------------------------------------------\nСПИСОК ЗАПРОСОВ ЛОГОВ:\n------------------------------------------")
        print(logs)
        return

get_id_requests()