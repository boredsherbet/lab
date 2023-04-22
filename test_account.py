import pytest
from account import Account


def test_account_init():
    account = Account('John Doe')
    assert account.get_name() == 'John Doe'
    assert account.get_balance() == 0


def test_account_deposit():
    account = Account('Jane Smith')
    assert account.deposit(100) == True
    assert account.get_balance() == 100


def test_account_withdraw():
    account = Account('Bob Johnson')
    account.deposit(500)
    assert account.withdraw(200) == True
    assert account.get_balance() == 300
    assert account.withdraw(400) == False
    assert account.get_balance() == 300
