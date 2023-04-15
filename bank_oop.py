"""This module is responsible for bank system with differents client"""

#Wallet and its operation

class WalletOperationError(Exception):
    """Error is rised, when there is same problems with wallet operations"""
    pass

class AgeErroe(Exception):
    """Raised when it is unsuitable"""
    pass

class Wallet:
    """class wallet"""
    id = 23491
    currency = "c. v."
    def __init__(self, balance):
        if not(isinstance(balance, int)) or balance < 0:
            raise ValueError("Your balance must be a positive number")
        self.balance = balance
        self.id = self.id
        Wallet.id += 1

    def __str__(self):
        return f"Your wallet balance is equel to {self.balance} {self.currency}"

    def insert_money(self, replenishment_amount):
        """Function to insert money to wallet"""
        if not(isinstance(replenishment_amount, int)) or replenishment_amount < 0:
            raise ValueError("Your replenishment amount must be a positive number")
        self.balance += replenishment_amount
        return f"Your account has been replenished by {replenishment_amount} {self.currency}"

    def insert_from_wallet(self, other, amount):
        """Insert money from one wallet to another"""
        if not(isinstance(amount, int)) or amount < 0:
            raise ValueError("Your replenishment amount must be a positive number")
        if not isinstance(other, Wallet):
            return "You must insert only from another wallet"
        if amount > other.balance:
            raise WalletOperationError("Replenishment amount must be not bigger than your balance")
        self.balance += amount
        other.balance -= amount
        return f"Your account has been replenished by {amount} {self.currency}"

    def withdraw(self, withdraw_amount):
        """Function to withdraw money"""
        if not(isinstance(withdraw_amount, int)) or withdraw_amount < 0:
            raise ValueError("Your withdraw amount must be a positive number")
        if withdraw_amount > self.balance:
            raise WalletOperationError("Withdraw amount must be not bigger than your balance")
        self.balance -= withdraw_amount
        return f"You have been withdrawed {withdraw_amount} {self.currency}"

class UanWallet(Wallet):
    """UAN wallet"""
    currency = "uan"
    usd_to_uan = 40
    def __init__(self, balance):
        super().__init__(balance)

    def __repr__(self):
        return f"UANWallet_{self.id}"

    def insert_from_wallet(self, other, amount):
        if not(isinstance(amount, int)) or amount < 0:
            raise ValueError("Your replenishment amount must be a positive number")
        if not isinstance(other, Wallet):
            return "You must insert only from another wallet"
        if amount > other.balance:
            raise WalletOperationError("Replenishment amount must be not bigger than your balance")
        if isinstance(other, UanWallet):
            pass
        elif isinstance(other, UsdWallet):
            amount /= self.usd_to_uan
        self.balance += amount
        other.balance -= amount
        return f"Your account has been replenished by {amount} {self.currency}"

class UsdWallet(Wallet):
    """USD wallet"""
    currency = 'usd'
    usd_to_uan = 40
    def __init__(self, balance):
        super().__init__(balance)

    def __repr__(self):
        return f"USDWallet_{self.id}"

    def insert_from_wallet(self, other, amount):
        if not(isinstance(amount, int)) or amount < 0:
            raise ValueError("Your replenishment amount must be a positive number")
        if not isinstance(other, Wallet):
            return "You must insert only from another wallet"
        if amount > other.balance:
            raise WalletOperationError("Replenishment amount must be not bigger than your balance")
        if isinstance(other, UanWallet):
            amount *= self.usd_to_uan
        elif isinstance(other, UsdWallet):
            pass
        self.balance += amount
        other.balance -= amount
        return f"Your account has been replenished by {amount} {self.currency}"

class Client:
    """class client. It can have not bigger than 3 wallet in different currency"""
    capacity = 3
    client_id = 3421
    def __init__(self, first_name, last_name, age):
        Client.test_age(age)
        self.name = first_name
        self.surname = last_name
        #for class client id start with 3421 and encreased by one point
        self.id = self.client_id
        Client.client_id += 1
        self.__wallets = []
        self.number_wallets = 0

    @staticmethod
    def test_age(age):
        """Raising an Ageerror if client is under 18"""
        if not isinstance(age,int) and not 18 <= age <= 100:
            raise AgeErroe("To became a client you have to be at least 18 years old")

    @property
    def wallets(self):
        """Return wallets of client"""
        if not self.__wallets:
            return "Client has no wallets"
        return self.__wallets

    def __str__(self):
        return f"Client name: {self.name}, surname: {self.surname},\
 id: {self.id}, wallets: {self.__wallets}"

    def __repr__(self) -> str:
        return f"Client_{self.id}"

    def add_wallet(self, wallet):
        """Add wallet to client"""
        if not isinstance(wallet, (UanWallet, UsdWallet)):
            return "You can add only currency wallet"
        if self.number_wallets >= self.capacity:
            return "You can't add more wallet"
        self.__wallets.append(wallet)
        return f"{wallet} was successfully added"

    def remove_wallet(self, wallet_id):
        """Remove wallet by id"""
        for wallet in self.__wallets:
            if wallet.id == wallet_id:
                self.__wallets.remove(wallet)
                return "Wallet was succesfully deleted"
        return f"There is no wallet with id: {wallet_id}"

    def total_sum_uan(self):
        """Return balance of client in UAN"""
        amount = 0
        for wallet in self.__wallets:
            if isinstance(wallet, UanWallet):
                amount += wallet.balance
            elif isinstance(wallet, UsdWallet):
                amount += wallet.balance * wallet.usd_to_uan
        return amount

    def total_sum_usd(self):
        """Remove balance of client in USD"""
        amount = 0
        for wallet in self.__wallets:
            if isinstance(wallet, UanWallet):
                amount += wallet.balance / wallet.usd_to_uan
            elif isinstance(wallet, UsdWallet):
                amount += wallet.balance
        return amount

class Bank:
    """class bank"""
    def __init__(self, bank_name):
        self.name = bank_name
        self.clients = []
        self.__capital = 0

    @property
    def capital(self):
        """Returning the total of bank capital"""
        return self.__capital

    @capital.setter
    def capital(self):
        """Counting the total capital for bank"""
        capital = 0
        for client in self.clients:
            capital += client.total_sum_uan()
        self.__capital = capital

    def add_client(self, client):
        """Add new client to bank"""
        if not isinstance(client, Client):
            return "You can add no object except Client"
        self.clients.append(client)

    def remove_client(self, cliend_id):
        """Remove client of bank by id"""
        for client in self.clients:
            if client.id == cliend_id:
                self.clients.remove(client)
                return "Client was successfully deleted"
        return "There is no client with such id"
