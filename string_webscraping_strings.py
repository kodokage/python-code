#import urllib.request
import time

#page = urllib.request.urlopen("https://sunlightlabs.github.io/congress/legislators?api_key='(myapikey)")

#text = page.read().decode("utf8")

dummy_text = "$53.61 Shipping & Import Fees Deposit to Nigeria Details"

price = 40.00

while price > 30.00 :
    time.sleep(5)
    #dummy_text = "$53.61 Shipping & Import Fees Deposit to Nigeria Details"
    where = dummy_text.find("$")
    start = where + 1
    end = where + 7
    price = float(dummy_text[start:end])
    print(price)
print("Buy now")
