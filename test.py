from tapi_yandex_metrika import YandexMetrikaLogsapi

ACCESS_TOKEN = {'OAuth AgAAAAAagjSRAAaIX07JmInDcEEHh0Ns5hYlQtM'}
COUNTER_ID = {'65607892'}

api = YandexMetrikaLogsapi(
    access_token=ACCESS_TOKEN,
    default_url_params={'counterId': COUNTER_ID},
    # Если True, скачает первую часть отчета, когда он будет сформирован.
    # По умолчанию False.
    wait_report=True,
    # Если True, будет скачивать все части отчета.
    # По умолчанию False.
    receive_all_data=True
)
params={
    "fields": "ym:s:date,ym:s:clientID,ym:s:dateTime,ym:s:startURL,ym:s:endURL",
    "source": "visits",
    "date1": "",
    "date2": ""
}
result = api.create().post(params=params)
request_id = result().data["log_request"]["request_id"]
# Когда включен параметр receive_all_data=True, параметр partNumber можно не указывать.
result = api.download(requestId=request_id).get()
data = result().data
print(data[:1000])