#041.
ticker = "btc_krw"
TICKER = ticker.upper()
print(TICKER)

#042.
ticker = "BTC_KRW"
ticker2 = ticker.lower()
print(ticker2)

#043.
ticker = "hello"
ticker = ticker.capitalize()
print(ticker)

#044.
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

#045.
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#047.
a = "hello world"
print(a.split(" "))

#048.

ticker = "btc_krw"

print(ticker.split("_"))


#049.

date = "2020-05-01"

date = date.split("-")
year = date[0]
month = date[1]
day = date[2]
print(year,month,day)

#050.

data = "039490  "
data = data.rstrip()
print(data)


