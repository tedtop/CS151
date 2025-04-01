# Ted Toporkov
# 2024-11-18
# bankaccount.py - A class that models a bank account with basic operations such as deposit, withdrawal, transfer, and balance inquiry.

import stdio

class BankAccount:
    def __init__(self, acct_num, acct_holder, balance=0):
        """Initialize a new bank account with account number, holder name, and optional starting balance"""
        self._acct_num = acct_num
        self._acct_holder = acct_holder
        self._balance = balance

    def get_account_holder_name(self):
        """Return the account holder's name"""
        return self._acct_holder

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            stdio.writeln("Invalid deposit amount.")
            return False
        self._balance += amount
        stdio.writeln(f"{self._acct_holder} deposited ${amount}. New balance: ${self._balance}")
        return True

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0 or amount > self._balance:
            stdio.writeln("Insufficient funds or invalid withdrawal amount.")
            return False
        self._balance -= amount
        stdio.writeln(f"{self._acct_holder} withdrew ${amount}. New balance: ${self._balance}")
        return True

    def get_balance(self):
        """Return the current balance"""
        return self._balance

    def transfer(self, recipient, amount):
        """Transfer money to another account"""
        if amount <= 0 or amount > self._balance:
            stdio.writeln("Insufficient funds or invalid transfer amount.")
            return False
        if self.withdraw(amount):
            if recipient.deposit(amount):
                stdio.writeln(f"{self._acct_holder} transferred ${amount} to {recipient.get_account_holder_name()}.")
                return True
            else:
                # If deposit fails, refund the withdrawal
                self._balance += amount
        return False

    def __str__(self):
        """Return string representation of the account"""
        return f"Account Number: {self._acct_num}, Account Holder: {self._acct_holder}, Balance: ${self._balance}"

def main():
    """Test client for BankAccount class"""
    # Creating accounts
    stdio.writeln("**Creating an account for Alice: (12345, Alice, 1000)")
    alice_account = BankAccount(12345, "Alice", 1000)
    stdio.writeln(alice_account)

    stdio.writeln("\n**Creating an account for Bob: (67890, Bob, 500)")
    bob_account = BankAccount(67890, "Bob", 500)
    stdio.writeln(bob_account)

    # Testing invalid deposit
    stdio.writeln("\n**Testing invalid deposit amount from Alice's account: -$200")
    alice_account.deposit(-200)
    stdio.writeln(alice_account)

    # Testing invalid withdrawals
    stdio.writeln("\n**Testing invalid withdrawal amount from Alice's account: -$200, $2000")
    alice_account.withdraw(-200)
    alice_account.withdraw(2000)
    stdio.writeln(alice_account)

    # Testing valid deposit and withdrawal
    stdio.writeln("\n**Testing valid deposit and valid withdrawal from Alice's account: $200, $300")
    alice_account.deposit(200)
    alice_account.withdraw(300)
    stdio.writeln(alice_account)

    # Testing invalid transfers
    stdio.writeln("\n**Testing invalid transfer from Alice to Bob: $2000, -$40")
    alice_account.transfer(bob_account, 2000)
    alice_account.transfer(bob_account, -40)
    stdio.writeln(alice_account)
    stdio.writeln(bob_account)

    # Testing valid transfer
    stdio.writeln("\n**Testing valid transfer from Alice to Bob: $500")
    alice_account.transfer(bob_account, 500)
    stdio.writeln(alice_account)
    stdio.writeln(bob_account)

if __name__ == "__main__":
    main()
