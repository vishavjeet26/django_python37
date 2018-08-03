import quandl
quandl.ApiConfig.api_key = '8vJnLQW_mrgAMT1DNVKN'
#Retrieve unfiltered time-series
mydata=quandl.get('EOD/HD')
print('Retrieve unfiltered time-series\n')
print(mydata)
# Filter by a single date
mydata=quandl.get('EOD/HD', start_date='2018-07-23', end_date='2018-07-23')
print('Filter by a single date\n')
print(mydata)
#Filter by a date range
mydata=quandl.get('EOD/HD', start_date='2018-07-19', end_date='2018-07-23')
print('Filter by a date range\n')
print(mydata)
#Retrieve two columns
mydata=quandl.get('EOD/HD', column_index='1')
print('Retrieve two columns\n')
print(mydata)
#Aditya Birla Capital Limited
mydata=quandl.get("NSE/ABCAPITAL", authtoken="8vJnLQW_mrgAMT1DNVKN")
print('Aditya Birla Capital Limited\n')
print(mydata)
#Bajaj Auto Limited
mydata=quandl.get("NSE/BAJAJ_AUTO", authtoken="8vJnLQW_mrgAMT1DNVKN")
print('Bajaj Auto Limited\n')
print(mydata)