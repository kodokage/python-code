import urllib.request
import time



def getPrice() :
  page = urllib.request.urlopen("https://sunlightlabs.github.io/congress/legislators?api_key='(myapikey)")
  text = page.read().decode("utf8")
  where = text.find("=-") 
  start = where + 2
  end =  start + 6
  exact = float(text[start:end])
  print(exact)

option =  input('Do you require the price immediatey (Y/N) : ')

if option == 'Y' :
    getPrice()

else:
  exact = 20.0
  while exact > 0:
       time.sleep(5)
       getPrice()
