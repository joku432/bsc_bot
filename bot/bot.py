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
        load_dotenv()
        self.secret_key = os.getenv("SECRET_KEY")
        #if self.secret_key is None:
        #    raise Exception()
        

    def run(self) -> None:
        pass
            
    def print_contract_total_supply(self) -> None:
        wei = self.contract.functions.totalSupply().call()
        print(Web3.fromWei(wei, 'ether'))

    def set_buy_limit(self, limit: float) -> None:
        pass

    def set_sell_limit(self, limit: float) -> None:
        pass

    def _check_liquidity_added(self) -> bool:
        pass

    def _buy(self, amount: float):
        pass

    def _sell(self, amount: float):
        pass

        