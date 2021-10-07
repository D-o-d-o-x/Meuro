# Meuro

Prices in euros from different times can not be compared without taking inflation into account.  
This also negatively impacts peoples abilities to gauge their own financial prosperity because what they conceive as a raise might not even cover they loss in purchase-power due to inflation.  
To fix this issue, I present:  
### The Millenial Euro
#### aka Meuro (symbol µ)
Meuro's worth is equivalent to that of the euro on January 1st 2001 00:00 GMT.  
(Yes, thats 2001 and not 2000 because the first millenium started in the year 1 and so the third one started in 2001. I do realize that this is stupid, but that's not my fault and all the people that celebrated the beginning of the new century at silvester 2000 should technically have waited another year.)  
## This repo
What you find in this repo is a small python-libary that connects to the ecb to get historic inflation-data and computes the conversion-factor between € and µ for any given date (after Jan 1st 2001).  
##### The provided functions are:
#### exchangeRate(date=None)
Gives you the exchange rate between euros and meuros for the given date.
#### euroToMeuro(eur, date=None, wholeCents=True)
Converts the given amount of euros to meuros for the given date. (wholeCents means it rounds to two decimal places)
#### meuroToEuro(meur, date=None, wholeCents=True)
Converts the given amount of meuros to euros for the given date. (wholeCents means it rounds to two decimal places)
#### liveValue(eur, interval=10)
Print the current amount of meuros for the given amunt of euros every interval-seconds. Comes in handy when you want to watch your live saving slowly fade away thanks to inflation.
#### When the date is set to None the current date is used
## Caveats
The ecb only gives an estimate for the inflation of the last month and no data for the current month.  
This libary just uses this estimate and assumes a yearly-inflation-rate of the current month (and all others months without data) of 2% (which is the stated goal-inflation-rate of the ecb).
## Future Plans
It would be cool to have a stable-coin on the ethereum-network, that tracks to the value of a meuro. I'm way to lazy to write that though...
