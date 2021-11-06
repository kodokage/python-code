import urllib.request
import time

exact = 20.00

while exact > 0 :
  time.sleep(5)
  page = urllib.request.urlopen("https://sunlightlabs.github.io/congress/legislators?api_key='(myapikey)")
  text = page.read().decode("utf8")
  price = text[231:239]
  where = text.find("=-") 
  start = where + 2
  end =  start + 6
  exact = float(text[start:end])
  print(exact)
  print('Target on the move')
