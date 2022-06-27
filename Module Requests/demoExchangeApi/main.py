import requests
import json

base = input("Bozulan döviz türü: ")
to = input("Alınan döviz türü: ")
num = int(input(f"Ne kadar {base} bozdurmak istiyorsunuz: "))

mainUrl = "https://api.apilayer.com/exchangerates_data/latest"
endpoint = "&base=" + base
url = mainUrl + endpoint
access_key = "aM8BpP0qpstjJXlCfFA2kGcRcIpUKmeG"
header = {
    "apikey" : access_key
}
response = requests.request("GET", url=url, headers=header)

if response.status_code == 200:
    dictExchangeRates = json.loads(response.text)["rates"]
    num2 = dictExchangeRates[to]
    result = num * num2
    print(f"1 {base} = {num2} {to}\n{num} {base} = {result} {to}")
else:
    print("Fail to access")

