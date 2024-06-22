import requests

# Ваш API ключ
API_KEY = ''

#INFORMATIVE ENDPOINTS
################################################################################################################
#функция запроса Retrieve country success rates per service (показатели успешности по странам для каждой услуги)
def post_ratesperservice():
    URL = 'https://api.smspool.net/request/success_rate'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'service': 395 #в данном случае делаем запрос на доступность гугла\жумала
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция запроса баланса
def post_balance():
    URL = 'https://api.smspool.net/request/balance'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(URL, headers=headers)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция запроса предлагаемых стран по сервисам
def post_suggestcountries():
    URL = 'https://api.smspool.net/request/suggested_countries'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'service': 395 #в данном случае делаем запрос на доступность гугла\жумала
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция просмотра предложенных пулов
def post_retrivesuggestedpool():
    URL = 'https://api.smspool.net/pool/retrieve_valid'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'service': 395, #в данном случае делаем запрос на гугл\жумаил
        'country': 4,
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция запроса countrylist (листстран)
def get_countrycode():
    URL = 'https://api.smspool.net/country/retrieve_all'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(URL, headers=headers)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция запроса servicelist (листсервисов)
def get_servicelist():
    URL = 'https://api.smspool.net/service/retrieve_all'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(URL, headers=headers)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#фкнция запроса пулов
def post_poollist(): 
    URL = 'https://api.smspool.net/pool/retrieve_all'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(URL, headers=headers)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")
################################################################################################################


#SMS
###############################################################################################################
#функция заказа смс
def post_getsms():
    URL = 'https://api.smspool.net/purchase/sms'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'country': 'RU', 
        'service': 395, #в данном случае делаем запрос на доступность гугла\жумала
        'pool': 3, #находим самый нужны пул при помощи функции  post_retrivesuggestedpool() 
        'max_price': 1, #определяем для себямакс прайс, лучше отталкивать от данных из пула, полученных в функции post_retrivesuggestedpool() 
        'pricing_option': 1, #0 если хотим закпать по минимальной цене, 1 если если хотим максимальный прок номера
        'quantity': 1, #колличество номеров 
        'areacode': '+972', #areacode
        'exclude': 0, #1  делает areacode исключением  
        'create_token': 0 #тут мы ставим 0 если нам не нужен общедоступный токен доступа к номерам, либо 1, если нужна его генерация 
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция проверки смс (тута мы берем ордерид из функции гетсмс)
def post_checksms(orderid):
    URL = 'https://api.smspool.net/sms/check'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'orderid': f'{orderid}'
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция завершения аренды конкретного номера (опять же мы берем ордерид из гетсмс)
def post_cancelorder(orderid):
    URL = 'https://api.smspool.net/sms/cancel'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    params = {
        'orderid': f'{orderid}'
    }
    response = requests.post(URL, headers=headers, data=params)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")

#функция завершения всех ордеров на аренду
def post_cancelorders(orderid):
    URL = 'https://api.smspool.net/sms/cancel_all'
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(URL, headers=headers)
    try:
        response_data = response.json()
        print("Ответ:", response_data)
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: Невозможно декодировать JSON ответ.")
        print("Ответ:", response.text)
    if response.status_code == 200:
        print("Запрос выполнен успешно.")
    elif response.status_code == 401:
        print("Ошибка: Неверный API ключ.")
    else:
        print(f"Ошибка: {response.status_code}")
