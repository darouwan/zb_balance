import codecs


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

    return transaction_list


def get_balance(list):
    final_coin = 0
    final_money = 0
    for transction in list:
        if isinstance(transction, Transactions):
            if transction.category == "+":
                final_coin = final_coin + transction.coin_amount
                final_money = final_money - transction.money_amount
            elif transction.category == "-":
                final_coin = final_coin - transction.coin_amount
                final_money = final_money + transction.money_amount
    print("final coin = ", final_coin)
    print("final money = ", final_money)


get_balance(read_file())
