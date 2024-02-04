#/env/scripts python3

"""
verifica o ping com uma lista de endereços IP ("default_ping-a.txt")
HP-M600-DESENVOLVIMENTO,192.168.17.28

Script tenta gerar uma comunicação com os IPs definidos

>>>ping-a.py

------------------------------------------------------------------------------------------------
|      DEVICE [12:49]       ||         IP          ||        PING        ||        Fail        |
------------------------------------------------------------------------------------------------
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||       [0/5]        |
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||       [0/5]        |
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||       [0/5]        |
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||       [0/5]        |
------------------------------------------------------------------------------------------------
"""

__version__ = "0.1.1"
__author__ = "Myke Bueno"
__licence__ = "Public Domain"

from ping3 import ping as ping33
from time import sleep
from datetime import datetime
import os


if __name__ == "__main__":
    
    pass
