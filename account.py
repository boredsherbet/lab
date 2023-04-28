class Account:
    """
    A class representing a bank account.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create the initial state of an account object
        :param name: The name of the account holder.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit a positive amount into the account balance
        :param amount: The amount to deposit.
        :return bool: True if the deposit was successful, False otherwise.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def get_name(self) -> str:
        """
        Method to access the name of the account
        :return str: The account holder's name.
        """
        return self.__account_name

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.
        :return float: The current balance of the account.
        """
        return self.__account_balance

    def withdraw(self, amount: float) -> bool:
        """
        Subtracts a positive amount from the account balance.
        :param amount: The amount to withdraw.
        :return bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount >= self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True