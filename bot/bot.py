from web3 import Web3
import json
import os
from dotenv import load_dotenv
from .bot_config import *

class Bot:
    def __init__(self, contract_addr: str):
        self.contract_addr = Web3.toChecksumAddress(contract_addr)
        self.web3 = Web3(Web3.HTTPProvider(DATASEED_ADDRESS))
        self.contract = self.web3.eth.contract(address=self.contract_addr, abi=json.loads(ABI_STR))
        # My account's address
        self.account = Web3.toChecksumAddress("0xD09c87E4701fa8955D21CC40EaE1D5A6CB1323e3")
        self.settings = Settings()

    def run(self):
        start_balance = self._get_account_balance()
        if start_balance <= 0.001:
            print("Balance is too small.")
            return

    def _get_account_balance(self):
        ether = self.web3.fromWei(self.web3.get_balance(self.account), "ether")
        return ether

    def print_contract_total_supply(self):
        wei = self.contract.functions.totalSupply().call()
        print(Web3.fromWei(wei, 'ether'))

    def set_buy_limit(self, limit: float):
        self.settings

    def set_sell_limit(self, limit: float):
        pass

    def _check_liquidity_added(self):
        pass

    def _buy(self, amount: float):
        pass

    def _sell(self, amount: float):
        pass

        