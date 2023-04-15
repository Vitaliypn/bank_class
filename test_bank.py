from bank__oop import *

def test_bank():
    wallet_1 = Wallet(10000)
    assert isinstance(wallet_1, Wallet)
    assert wallet_1.balance == 10000
    assert wallet_1.id == 23491
    assert wallet_1.currency == 'c. v.'
    assert str(wallet_1) == "Your wallet balance is equel to 10000 c. v."
    try:
        Wallet(-100)
    except ValueError as e:
        assert str(e) == "Your balance must be a positive number"

    assert wallet_1.insert_money(1000) == "Your account has been replenished by 1000 c. v."
    assert wallet_1.balance == 11000

    try:
        wallet_1.insert_money(-100)
    except ValueError as e:
        assert str(e) == "Your replenishment amount must be a positive number"

    wallet_2 = Wallet(5000)
    assert wallet_2.id == 23492
    assert wallet_1.insert_from_wallet(wallet_2, 4000) == "Your account has been replenished by 4000 c. v."
    assert wallet_1.balance == 15000
    assert wallet_2.balance == 1000
    try:
        wallet_1.insert_from_wallet(wallet_2, -100)
    except ValueError as e:
        assert str(e) == "Your replenishment amount must be a positive number"
    try:
        wallet_1.insert_from_wallet(wallet_2, 20000)
    except WalletOperationError as e:
        assert str(e) == "Replenishment amount must be not bigger than your balance"

    assert wallet_1.withdraw(10000) == "You have been withdrawed 10000 c. v."
    assert wallet_1.balance == 5000
    try:
        wallet_1.withdraw(-100)
    except ValueError as e:
        assert str(e) == "Your withdraw amount must be a positive number"
    try:
        wallet_1.withdraw(20000)
    except WalletOperationError as e:
        assert str(e) == "Withdraw amount must be not bigger than your balance"

    uan_wallet = UanWallet(200)
    assert str(uan_wallet) == "Your wallet balance is equel to 200 uan"
    assert isinstance(uan_wallet, Wallet)
    assert isinstance(uan_wallet, UanWallet)
    assert uan_wallet.balance == 200
    assert uan_wallet.currency == 'uan'

    usd_wallet = UsdWallet(100)
    assert str(usd_wallet) == "Your wallet balance is equel to 100 usd"
    assert isinstance(usd_wallet, Wallet)
    assert isinstance(usd_wallet, UsdWallet)
    assert usd_wallet.balance == 100
    assert usd_wallet.currency == 'usd'

    assert uan_wallet.insert_from_wallet(usd_wallet, 100) == "Your account has been replenished by 100 uan"
    assert uan_wallet.balance == 300
    assert usd_wallet.balance == 97.5

    assert uan_wallet.withdraw(50) == "You have been withdrawed 50 uan"
    assert uan_wallet.balance == 250

    assert usd_wallet.insert_from_wallet(uan_wallet, 5) == "Your account has been replenished by 5 usd"
    assert uan_wallet.balance == 50
    assert usd_wallet.balance == 102.5

    assert usd_wallet.withdraw(50) == "You have been withdrawed 50 usd"
    assert usd_wallet.balance == 52.5

    try:
        uan_wallet.insert_from_wallet(usd_wallet, -100)
    except ValueError as e:
        assert str(e) == "Your replenishment amount must be a positive number"

    try:
        uan_wallet.insert_from_wallet(usd_wallet, 10000)
    except WalletOperationError as e:
        assert str(e) == "Replenishment amount must be not bigger than your balance"

    try:
        usd_wallet.insert_from_wallet(uan_wallet, -100)
    except ValueError as e:
        assert str(e) == "Your replenishment amount must be a positive number"

    try:
        usd_wallet.insert_from_wallet(uan_wallet, 10000)
    except WalletOperationError as e:
        assert str(e) == "Replenishment amount must be not bigger than your balance"

    client_1 = Client('Vitalii', 'Paliichuk', 18)
    assert isinstance(client_1, Client)
    assert client_1.name == 'Vitalii'
    assert client_1.surname == 'Paliichuk'
    assert client_1.id == 3421
    assert client_1.number_wallets == 0
    assert str(client_1) == "Client name: Vitalii, surname: Paliichuk, id: 3421, wallets: []"
    assert client_1.wallets == "Client has no wallets"
    
    #try:
    #  client_2 = Client('Anastasiia', 'Martsinkovska', 17)
    #except AgeErroe as e:
    #  assert str(e) == "To became a client you have to be at least 18 years old"

    uan_wallet1_vp = UanWallet(1000)
    assert uan_wallet1_vp.id == 23495
    usd_wallet2_vp = UsdWallet(150)
    assert usd_wallet2_vp.id == 23496
    uan_wallet3_vp = UanWallet(3000)
    assert uan_wallet3_vp.id == 23497
    usd_wallet4_vp = UsdWallet(400)
    assert usd_wallet4_vp.id == 23498

    assert client_1.add_wallet(uan_wallet1_vp) == "Your wallet balance is equel to 1000 uan was successfully added"
    assert client_1.add_wallet(usd_wallet2_vp) == "Your wallet balance is equel to 150 usd was successfully added" 
    assert client_1.add_wallet(uan_wallet3_vp) == "Your wallet balance is equel to 3000 uan was successfully added" 
    assert client_1.add_wallet(usd_wallet4_vp) == "You can't add more wallet"

    assert client_1.remove_wallet(23495) == "Wallet was succesfully deleted"
    assert client_1.remove_wallet(99995) == "There is no wallet with id: 99995"

    assert client_1.total_sum_uan() == 9000
    assert client_1.total_sum_usd() == 225.0

    bank_1 = Bank('Mono')
    assert isinstance(bank_1, Bank)
    assert bank_1.name == 'Mono'
    assert bank_1.clients_amount == 0
    assert bank_1.capital == 0

    bank_1.add_client(client_1)
    assert bank_1.add_client('client_1') == "You can add no object except Client"
    assert bank_1.clients_amount == 1
    #assert bank_1.capital == 9000

    assert bank_1.remove_client(3421) == "Client was successfully deleted"
    assert bank_1.clients_amount == 0
    #assert bank_1.capital == 0

    assert bank_1.remove_client(9999) ==  "There is no client with such id"

if __name__ == '__main__':
    test_bank()
