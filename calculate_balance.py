import codecs
import json

import requests

transaction_file = "transactions.txt"  # transactions file name
coin_type = "zb"  # coin type, like btc,eth, or hsr, etc.
currency_type = "qc"  # currency name, like qc or usdt


class Transactions:
    category = ""
    coin_amount = 0
    money_amount = 0

    def __init__(self, category, coin_amount, money_amount):
        self.category = category
        self.coin_amount = coin_amount
        self.money_amount = money_amount

    def __str__(self):
        return self.category + "\t" + str(self.coin_amount) + "\t" + str(self.money_amount)


def read_file(file_name="transactions.txt"):
    transaction_list = []
    for line in codecs.open(file_name, "r", "utf-8").readlines():
        line = line.strip()
        if line.find("已完成")>=0:
            if line.find("卖") >= 0:
                items = line.split("\t")
                transc = Transactions("-", float(items[1].split(" ")[3]), float(items[3]))
                transaction_list.append(transc)
                print(transc)
                continue
            elif line.find("买") >= 0:
                items = line.split("\t")
                transc = Transactions("+", float(items[1].split(" ")[3]), float(items[3]))
                transaction_list.append(transc)
                print(transc)
                continue
            else:
                continue
        else:
            continue

    return transaction_list


def get_balance(trans_list):
    final_coin = 0
    final_money = 0
    buy_in_cost = 0
    buy_in_coin = 0
    for transaction in trans_list:
        if isinstance(transaction, Transactions):
            if transaction.category == "+":
                final_coin = final_coin + transaction.coin_amount
                final_money = final_money - transaction.money_amount
                buy_in_cost += transaction.money_amount
                buy_in_coin += transaction.coin_amount
            elif transaction.category == "-":
                final_coin = final_coin - transaction.coin_amount
                final_money = final_money + transaction.money_amount
    print("final coin changed = ", final_coin)
    print("final money changed = ", final_money)
    if final_coin > 0:
        print("Avg buying cost = ", -final_money / final_coin)
    elif final_coin < 0:
        print("Avg selling cost = ", -final_money / final_coin)
    price = get_latest_market(coin_type, currency_type)
    actual_benefit = final_coin * price + final_money
    print("Actual Benefit = ", actual_benefit)
    print("Avg buy in cost = ", buy_in_cost / buy_in_coin)


def get_latest_market(coin="hsr", currency="qc"):
    r = requests.get("http://api.zb.com/data/v1/ticker?market=" + coin + "_" + currency)
    content = r.content
    # print(content)
    data = json.loads(content.decode())
    price = float(data['ticker']['last'])
    print("The latest price = %.2f %s" % (price, currency))
    return price


if __name__ == "__main__":
    get_balance(read_file(transaction_file))
