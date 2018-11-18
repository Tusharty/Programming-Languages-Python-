class CreditCard:
    """A consumer credit card"""
    def __init__(self,customer,bank,acnt,limit):
        """crete a new Credit card instance.
        The initial balance is zero.

        customer        the name of the customer
        bank            the name of the bank
        acnt            the account identifier
        limit           credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """return name of the customer"""
        return self._customer

    def get_bank(self):
        """return name of the bank"""
        return self._bank

    def get_account(self):
        """return account identifier"""
        return self._account

    def get_limit(self):
        """return current credit limit"""
        return self._limit

    def get_balance(self):
        """return current balance"""
        return self._balance

    def charge(self, price):
        """charge given price to the card, assumig sufficient credit limit

        return true if charge was processed. false if charge was denied

        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """process customer payment that reduces balance"""

        self._balance -= amount

# cc = CreditCard("Tushar Tyagi", "Bank of America", "111111", 1000)

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Mathew Stan", "BNY", 121212, 2500))
    wallet.append(CreditCard("Mathew Stan", "BNY", 131313, 3500))
    wallet.append(CreditCard("Mathew Stan", "BNY", 141414, 5000))

    # print("wallet = ",wallet)
    # print("wallet = ",wallet[0])

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print ("Customet = ",wallet[c].get_customer())
        print ("Bank = ", wallet[c].get_bank())
        print ("Account = ", wallet[c].get_account())
        print ("limit = ", wallet[c].get_limit())
        print ("Balance = ", wallet[c].get_balance())

        while wallet[c].get_balance() > 100 :
            wallet[c].make_payment(100)
            print('New Balance = ',wallet[c].get_balance())
        










