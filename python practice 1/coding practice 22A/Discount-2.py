def discount(price):
    price=int(price)
    if price<500:
        print("discount "+str(5)+"%")
    elif price<2500:
        print("discount "+str(10)+"%")
    elif price>2500:
        print("discount "+str(20)+"%")
price=input()
discount(price)

    