import time

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coin = ""
cur = ""
p = ""


class Container(BoxLayout):
    def get_curr(self):
        global coin
        global cur
        coin = self.coin_name.text
        cur = self.curr.text

    def view_cur(self):
        sell = cg.get_price(ids=coin, vs_currencies=cur)
        price = sell.pop(coin)
        global p
        p = price[cur]
        self.currency.text = time.ctime() + " Цена " + coin + " " + str(p) + " " + cur

    def enter_limit(self):
        if float(p) < float(self.min_c.text):
            self.view_lim.text = "курс упал ниже " + self.min_c.text
        elif float(p) > float(self.max_c.text):
            self.view_lim.text = "курс поднялся выше " + self.max_c.text
        else:
            self.view_lim.text = "курс в пределах: от " + self.min_c.text + " до " + self.max_c.text


class CoinApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    CoinApp().run()
