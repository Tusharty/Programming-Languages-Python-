class PredatoryCreditCard(CreditCard):

    """
    An extension to CreditCard that compounds intrest and fees
    """

    def __init__(self, customer, bank, acnt, limit, apr):
        """create a new predatory Credit Card instance

        The initial value is zero

        customer        the name of the customer
        bank            the name of the bank
        acnt            the account identifier
        limit           credit limit
        apr             annual percentage rate
        """

        super().__init__(customer, bank,acnt,limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
            Return true if charge was processed.
            Return false and assess $5 if charge is denied
        """

        success = super().charge(price)

        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Access monthly interest in outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor