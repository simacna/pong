# This chapter deals with objects


#Example of a CreditCard class

class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g. 'John Bowman')
        bank      the name of the bank (e.g. 'California Savings')
        acnt      the account identifier (e.g. '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return name of customer. """
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """ Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied."""

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        self._balance -= amount #UGH NO RETURN STATEMENT WAS NEEDED



# The Constructor

cc1 = CreditCard("John Doe", '1st Bank', '5391 1111 1111 1111', 1000)

cc1.charge(20)
myB = cc1.get_balance
print(myB)



#Testing the Class
#We demonstrate some basic usage of the CreditCard class, inserting three cards into a list named wallet. We use loops to make some charges and payments, 
#and use various
#accessor to print results into the console.
#These tests are enclosed within a conditional: if __name__ == '__main__':
#so that they can be embedded in the source code with the class definition.

#the test provides METHOD COVERAGE as each of the methods is called at least once, but it does not provide STATEMENT COVERAGE as there is never a 
#case in which a charge is
#rejected due to the credit limit. 
#
# if __name__ == '__main__':
#     wallet = []
#     # wallet.append(CreditCard('John Bowman', 'California Savings', '1111 1111 1111 1111', 2500))
#     # wallet.append(CreditCard('John Cowman', 'California Federal', '2222 2222 2222 2222', 3500))
#     # wallet.append(CreditCard('John Dowman', 'California Finance', '3333 3333 3333 3333', 4500))
#     #
#     # for val in range(1,17):
#     #     wallet[0].charge(val)
#     #     wallet[1].charge(2*val)
#     #     wallet[2].charge(3*val)
#     #
#     # for c in range(3):
#         print('Customer=', wallet[c].get_customer())
#         print('Bank=', wallet[c].get_bank())
#         print('Account=', wallet[c].get_account())
#         print('Limit=', wallet[c].get_limit())
#         print('Balance=', wallet[c].get_balance())
#         while wallet[c].get_balance() > 100:
#             wallet[c].make_payment(100)
#             print ('New balance=', wallet[c].get_balance())
#             print()