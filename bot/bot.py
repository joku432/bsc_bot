from web3 import Web3
import json

class Bot:
    def __init__(self, contract: str):
        self.contract = contract
        self.web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    
    def run() -> None:
        pass

    def set_buy_limit(self, limit: float) -> None:
        pass

    def set_sell_limit(self, limit: float) -> None:
        pass

    def _check_liquidity_added(self) -> bool:
        pass

        