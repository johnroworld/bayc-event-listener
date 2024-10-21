from web3 import Web3
from django.conf import settings

def connect_to_blockchain():
    web3 = Web3(Web3.HTTPProvider(settings.ETH_NETWORK_URL))
    if not web3.is_connected():
        raise ConnectionError("Unable to connect to Ethereum network")
    return web3

contract_address = Web3.to_checksum_address(settings.WEB3_CONTRACT_ADDRESS)
abi = settings.WEB3_ABI

def get_bayc_contract(web3):
    return web3.eth.contract(address=contract_address, abi=abi)