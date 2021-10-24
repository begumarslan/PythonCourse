import random

class Portfolio():
    def __init__(self):
        self.hist = "\n"    #list of transaction history
        self.cash = 0.0
        self.account = dict({'stock': {}, 'mutual funds':{}, 'bonds': {}})


    def addCash(self, cash):
        self.cash += cash
        self.hist+="{:.2f} cash had been added, current cash is {:.2f}\n".format(cash,self.cash)


    def removeCash(self,cash):
        if self.cash<cash:  #check if the cash is enough to remove
            print("You do not have enough amount to remove the cash, you have {} cash\n").format(self.cash)
            self.hist += "Cannot remove cash since balance is {:.2f}\n".format(self.cash)
        else:
            self.cash-=cash
            self.hist+="{:.2f} cash had been removed, current cash is {:.2f}\n".format(cash, self.cash)


    def buyStock(self, number_of_shares, Stock):    #Number of shares should be an integer
        if self.cash < int(number_of_shares)*Stock.price:   #check if cash is enough to buy a stock
            print("You do not have enough amount to buy stock, you have {:.2f} cash\n".format(self.cash))
            self.hist+= "Cannot buy cash since balance is {:.2f}\n".format(self.cash)
        else:
            self.cash -= int(number_of_shares)*Stock.price
            self.hist += "Bought {} shares of {}. Current cash is {:.2f}\n".format(int(number_of_shares), Stock.ticker, self.cash)
            if Stock.ticker in self.account['stock']:
                self.account['stock'][Stock.ticker] += int(number_of_shares)
            else:
                self.account['stock'][Stock.ticker] = int(number_of_shares)


    def sellStock (self, ticker, number_of_shares):  #Number of shares should be an integer
        if ticker in self.account['stock']: #check if the ticker is present in our stocks
            if self.account['stock'][ticker] < int(number_of_shares): #check if there is enough amount to sell
                print('You do not have enough amount to sell stock\n')
                self.hist+= "Cannot sell stock since you don't have enough\n"

            elif self.account['stock'][ticker] == int(number_of_shares):
                self.cash+=int(number_of_shares)*random.uniform(0.5*self.account['stock'][ticker], 1.5*self.account['stock'][ticker])
                del self.account['stock'][ticker]   #if share becomes zero, deletes
                self.hist += "Sold {} shares of {}. Current cash is {:.2f}\n".format(int(number_of_shares), ticker, self.cash)

            else:
                self.account['stock'][ticker] -= int(number_of_shares)
                self.cash+=int(number_of_shares)*random.uniform(0.5*self.account['stock'][ticker], 1.5*self.account['stock'][ticker]) #stocks can be sold for a price that is uniformly drawn from [0.5-1.5]
                self.hist += "Sold {} shares of {}. Current cash is {:.2f}\n".format(int(number_of_shares), ticker, self.cash)
        else:
            print("You do not have enough amount to sell stock\n")
            self.hist += "Cannot sell stock since there isn't enough\n"


    def buyMutualFund(self, number_of_shares, mf):
        if self.cash < 1*number_of_shares:
            print("You do not have enough amount to buy mutual fund, you have {:.2f} cash\n".format(self.cash))
            self.hist+= "Cannot buy mutual fund since balance is {:.2f}\n".format(self.cash)
        else:
            self.cash -= 1*number_of_shares
            self.hist += "Bought {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_of_shares, mf.symbol, self.cash)
            if mf.symbol in self.account['mutual funds']:
                self.account['mutual funds'][mf.symbol] += number_of_shares
            else:
                self.account['mutual funds'][mf.symbol] = number_of_shares

    def sellMutualFund(self,symbol, number_of_shares):
        if symbol in self.account['mutual funds']: #check if the ticker is present in our mutual funds
            if self.account['mutual funds'][symbol] < number_of_shares: #check if there is enough amount to sell
                print('You do not have enough amount to sell mutual funds\n')
                self.hist+= "Cannot sell mutual funds since you there isn't enough\n"

            elif self.account['mutual funds'][symbol] == number_of_shares:
                self.cash += random.uniform(0.9*1, 1.5*1)*number_of_shares
                del self.account['mutual funds'][symbol]    #if share becomes zero, deletes
                self.hist += "Sold {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_of_shares, symbol, self.cash)

            else:
                self.account['mutual funds'][symbol] -= number_of_shares
                self.cash += random.uniform(0.9*1, 1.5*1)*number_of_shares #mutual funds can be sold for a price that is uniformly drawn from [0.9-1.2]
                self.hist += "Sold {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_of_shares, symbol, self.cash)
        else:
            print("You do not have enough amount to sell mutual funds\n")
            self.hist += "Cannot sell mutual funds since there isn't any\n"

    def history(self): print(self.hist)

    def __str__(self):

        cash_result = "{:.2f}".format(self.cash)
        stocks_result = ""
        mf_result = ""
        bond_result = ""
        for stock, share in self.account['stock'].items():
            stocks_result+= "\n{} {}".format(share,stock)
        for mf, share in self.account['mutual funds'].items():
            mf_result+= "\n{} {}".format(share,mf)
        for bond, share in self.account['bonds'].items():
            bond_result+= "\n{} {}".format(share,bond)
        return "cash:"+ cash_result + "\nstock:" + stocks_result + "\nmutual funds:" + mf_result + "\nbonds:" + bond_result

    def buyBond(self, number_of_bond, Bond):
        if self.cash < number_of_bond* Bond.price:
            print("You do not have enough amount to buy bond, you have {:.2f} cash\n".format(self.cash))
            self.hist+= "Cannot buy bond since balance is {:.2f}\n".format(self.cash)
        else:
            self.cash -= number_of_bond* Bond.price
            self.cash += number_of_bond*Bond.coupon
            self.hist += "Bought {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_of_bond, Bond.ticker, self.cash)
            if Bond.ticker in self.account['bonds']:
                self.account['bonds'][Bond.ticker] += number_of_bond
            else:
                self.account['bonds'][Bond.ticker] = number_of_bond

    def sellBond(self, number_bond_sold, Bond):
        if Bond.ticker in self.account['bonds']: #check if the ticker is present in our mutual funds
            if self.account['bonds'][Bond.ticker] < number_bond_sold: #check if there is enough amount to sell
                print('You do not have enough amount to sell bonds\n')
                self.hist+= "Cannot sell bonds since you there isn't enough\n"

            elif self.account['bonds'] == number_bond_sold:
                self.cash += random.uniform(0.9*Bond.price, 1.5*Bond.price)*number_bond_sold
                del self.account['bonds'][Bond.ticker]    #if share becomes zero, deletes
                self.hist += "Sold {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_bond_sold, Bond.ticker, self.cash)

            else:
                self.account['bonds'][Bond.ticker] -= number_bond_sold
                self.cash += random.uniform(0.9*Bond.price, 1.5*Bond.price)*number_bond_sold #mutual funds can be sold for a price that is uniformly drawn from [0.9-1.2]
                self.hist += "Sold {:.2f} shares of {}. Current cash is {:.2f}\n".format(number_bond_sold, Bond.ticker, self.cash)
        else:
            print("You do not have enough amount to sell mutual funds\n")
            self.hist += "Cannot sell mutual funds since there isn't any\n"





class Stock(): #Create stock class
    def __init__(self, price, ticker):
        self.price = price
        self.ticker=ticker

class MutualFund(): #Create mutualfund class
    def __init__(self, symbol):
        self.symbol = symbol

class Bond(Stock):
    def __init__(self, price, ticker, coupon):
        Stock.__init__(self, price, ticker)
        self.coupon = coupon


if __name__ == '__main__':
    portfolio = Portfolio()
    portfolio.addCash(300.50)
    s = Stock(20, "HFH")
    portfolio.buyStock(5, s)
    mf1 = MutualFund("BRT")
    mf2 = MutualFund("GHT")
    portfolio.buyMutualFund(10.3, mf1)
    portfolio.buyMutualFund(2, mf2)
    portfolio.sellMutualFund("BRT", 3)
    portfolio.sellStock("HFH", 1)
    b = Bond(40, "TNP", 5)
    portfolio.buyBond(2, b)
    portfolio.sellBond(1, b)
    portfolio.history()
    print(portfolio)
