from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coin = "dogecoin"  # input("What coin you interested?: ")
curr = "uah"  # input("what currency?: ")
max_limit = 10
min_limit = 5

sell = cg.get_price(ids=coin, vs_currencies=curr)
print(sell)

price = sell.pop(coin)
print(price)

s = price[curr]
print(s)
if s > max_limit:
    print("You win")
elif s < min_limit:
    print("You loose")