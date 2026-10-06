import allure
import pytest

# The thing we are testing (a simple bank account)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


@allure.feature("Account")
@allure.story("Creation")
@allure.title("Verify new account starts with correct balance")
@allure.severity(allure.severity_level.NORMAL)
def test_account_creation():
    with allure.step("Create account with balance 1000"):
        account = BankAccount("Mamta", 1000)
    with allure.step("Check starting balance"):
        assert account.balance == 1000


@allure.feature("Transactions")
@allure.story("Deposit")
@allure.title("Verify deposit increases balance")
@allure.severity(allure.severity_level.CRITICAL)
def test_deposit():
    account = BankAccount("Mamta", 1000)
    with allure.step("Deposit 500"):
        account.deposit(500)
    with allure.step("Check new balance is 1500"):
        assert account.balance == 1600


@allure.feature("Transactions")
@allure.story("Withdraw")
@allure.title("Verify withdraw decreases balance")
@allure.severity(allure.severity_level.CRITICAL)
def test_withdraw():
    account = BankAccount("Mamta", 1000)
    with allure.step("Withdraw 300"):
        account.withdraw(300)
    with allure.step("Check new balance is 700"):
        assert account.balance == 700


@allure.feature("Transactions")
@allure.story("Withdraw")
@allure.title("Verify cannot withdraw more than balance")
@allure.severity(allure.severity_level.BLOCKER)
def test_withdraw_too_much():
    account = BankAccount("Mamta", 1000)
    with allure.step("Try to withdraw 5000 and expect an error"):
        with pytest.raises(ValueError):
            account.withdraw(5000)