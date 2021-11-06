from trasnsactions import *
import promotion 
import starbuzz

items = ["Donut", "Latte", "Filter", "Muffin"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for item in items:
        print(str(option) + ". " + item)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running =  False
    else:
        credit_card = input("Credit card number: ")
        new_price = promotion.discount(prices[choice - 1])
        starrbuzz_holder = input('Holding Starbuzz card (Y/N): ')
        if starrbuzz_holder == "Y":
            final_price = starbuzz.discount(new_price)
        else:
            final_price =  new_price
        save_transaction(final_price, credit_card,items[choice - 1])