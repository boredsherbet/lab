class Account:
    """
    A class representing a bank account.

    Attributes:
        __account_name (str): The name of the account holder.
        __account_balance (float): The current balance of the account.

    Methods:
        deposit(amount: float) -> bool: Add a positive amount to the account balance.
        get_name() -> str: Return the account holder's name.
        get_balance() -> float: Return the current balance of the account.
        withdraw(amount: float) -> bool: Subtract a positive amount from the account balance.
    """

    def __init__(self, name: str) -> None:
        """
        Constructs an Account object with the given name.

        Parameters:
            name (str): The name of the account holder.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Adds a positive amount to the account balance.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            bool: True if the deposit was successful, False otherwise.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def get_name(self) -> str:
        """
        Returns the account holder's name.

        Returns:
            str: The account holder's name.
        """
        return self.__account_name

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.__account_balance

    def withdraw(self, amount: float) -> bool:
        """
        Subtracts a positive amount from the account balance.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount >= self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True