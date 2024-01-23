#/env/scripts python3

"""
verifica o ping com uma lista de endereços IP

Script tenta gerar uma comunicação com os IPs definidos

>>>ping-a.py
        DEVICE      |       IP      |       ms       |      [12:49]
 printer_logistica  | 192.168.17.28 |       1       |

"""

__version__ = "0.1.0"
__author__ = "Myke Bueno"
__licence__ = "Free"

from ping3 import ping as ping33
from time import sleep
from datetime import datetime




# print(datetime.now())