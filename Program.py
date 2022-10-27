
from requests import get

waluta = input("Podaj walutę: ")
waluta = waluta.upper()

data = input("Podaj datę: ")

odpowiedz = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json")

if odpowiedz.ok:
    dane = odpowiedz.json()
    kurs_waluty = dane['rates'][0]['mid']

    print(f"1 {waluta} = {kurs_waluty} PLN w dniu {data}" )

else:
    print("Brak danych")
