import pytest
from account import Account


class Test:
    def setup_method(self):
        self.account1 = Account('John Doe')
        self.account2 = Account('Jane Doe')

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'John Doe'
        assert self.account2.get_name() == 'Jane Doe'
        assert self.account1.get_balance() == 0
        assert self.account2.get_balance() == 0

    def test_deposit(self):
        # Normal behavior
        assert self.account1.deposit(100) is True
        assert self.account1.get_balance() == pytest.approx(100, abs == 0.001)
        assert self.account1.deposit(100.51) is True
        assert self.account1.get_balance() == pytest.approx(200.51, abs == 0.001)
        # Negative Amount
        assert self.account1.deposit(-10) is False
        assert self.account1.get_balance() == pytest.approx(200.51, abs == 0.001)
        assert self.account1.deposit(-25.7) is False
        assert self.account1.get_balance() == pytest.approx(200.51, abs == 0.001)
        # Zero Amount
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == pytest.approx(200.51, abs == 0.001)

    def test_withdraw(self):
        self.account1.deposit(100)  # deposit amount to be withdrawn
        # Normal behavior
        assert self.account1.withdraw(10.5) is True
        assert self.account1.get_balance() == pytest.approx(89.5, abs == 0.001)
        assert self.account1.withdraw(10) is True
        assert self.account1.get_balance() == pytest.approx(79.5, abs == 0.001)
        # Negative Amounts
        assert self.account1.withdraw(-10.5) is False
        assert self.account1.get_balance() == pytest.approx(79.5, abs == 0.001)
        assert self.account1.withdraw(-10) is False
        assert self.account1.get_balance() == pytest.approx(79.5, abs == 0.001)
        # Irregular Amounts
        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == pytest.approx(79.5, abs == 0.001)
        assert self.account1.withdraw(1000) is False
        assert self.account1.get_balance() == pytest.approx(79.5, abs == 0.001)
