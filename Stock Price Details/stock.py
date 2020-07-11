from yahoo_fin import stock_info

brand=input("Enter the company whose stock you want to track - ")

#while True:
price=stock_info.get_live_price(brand)
print(price)
if price<1500:
    print('Good time to sell your stocks')
elif price<2700:
    print('Good time to invest')
elif price<5000:
    print('Profit!')