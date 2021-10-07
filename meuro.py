import requests
from datetime import datetime
from dateutil import relativedelta

# Ugly code thats outside of any function
url = 'https://sdw.ecb.europa.eu/quickviewexport.do?SERIES_KEY=122.ICP.M.U2.N.000000.4.ANR&type=csv'
resp = requests.get(url)
lines = resp.text.split('\n')[6:]
years = {} # Will later contain the monthly factor of inflation (~1.0016667) for every month
for line in lines:
    vals = line.split(',')
    year = int(vals[0][:4])
    month = datetime.strptime(vals[0][4:],'%b').month
    inflation = float(vals[1])
    if not year in years:
        years[year] = {}
    years[year][month] = 1 + (inflation/100)/12

for year in years:
    months = years[year]
    for month in range(1,13):
        if month not in months:
            years[year][month] = 1 + 0.02/12 # Lets say the ECB archives their target

# Gives you the exchange rate between euros and meuros for the given date.
# (Should always be a float < 1)
# date should be either a datetime-object or None (= current date)
def exchangeRate(date=None):
    if date==None:
        date = datetime.now()
    month, year = date.month, date.year
    if year < 2001:
        raise Exception('µeuro-values for €uro prices before the start of this millenium are undefined.')
    akk = 1
    for fullYear in range(2001, year):
        yearlyInf = 1
        for m in years[fullYear]:
            monthlyInf = years[fullYear][m]
            yearlyInf *= monthlyInf
        akk *= yearlyInf

    for fullMonth in range(1, month):
        monthlyInf = years[year][fullMonth]
        akk *= monthlyInf

    beginningOfMonth = date.replace(hour=0, minute=0, second=0, microsecond=0, day=1)
    endOfMonth = beginningOfMonth + relativedelta.relativedelta(months=1)
    fracOfMonth = (date - beginningOfMonth).total_seconds() / (endOfMonth - beginningOfMonth).total_seconds()
    inflationThisMonth = 1 + fracOfMonth * (years[year][month]-1)

    akk *= inflationThisMonth

    return 1/akk
# Converts the given amount of euros to meuros for the given date. (wholeCents means it rounds to two decimal places)
# date should be either a datetime-object or None (= current date)
def euroToMeuro(eur,date=None,wholeCents=True):
    return round(eur * factorForDate(date),[64,2][wholeCents])

# Converts the given amount of meuros to euros for the given date. (wholeCents means it rounds to two decimal places)
# date should be either a datetime-object or None (= current date)
def meuroToEuro(meur,date=None,wholeCents=True):
    return round(meur / factorForDate(date),[64,2][wholeCents])

# Print the current amount of meuros for the given amunt of euros every <interval>-seconds.
# Comes in handy when you want to watch your life savings slowly fade away thanks to inflation.
def liveValue(eur,interval=10):
    import time
    while True:
        print(str(eur*exchangeRate())+'µ')
        time.sleep(interval)
