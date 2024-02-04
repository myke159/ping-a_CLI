#/env/scripts python3

"""
This function reads network information from a CSV file, pings the IP addresses,
updates the file with the ping results, displays an interface, and repeats the process
in a loop with a 10-second delay. Additional keyword arguments can be passed to customize
the appearance of the interface.

>>> ping-a.py
                                        04/02/2024 18:42:31
-------------------------------------------------------------------------------------------------
|          DEVICE           ||         IP          ||        PING         ||        FAIL        |
-------------------------------------------------------------------------------------------------
|  HP-M600-DESENVOLVIMENTO  ||    192.168.17.20    ||         OFF         ||         0          |
|     HP-3015-COMERCIAL     ||    192.168.16.48    ||         53          ||         0          |
-------------------------------------------------------------------------------------------------
"""

__version__ = "0.1.1"
__author__ = "Myke Bueno"
__licence__ = "Public Domain"

import os

from ping3 import ping
from time import sleep
from datetime import datetime

import interface


def with_reader(filepath: str, /) -> list:
    """Reads a CSV file and returns its content as a list of lists.

    This function assumes the CSV file has four columns separated by commas.

    Example:
    >>> filepath = 'default_ping-a.txt'
    >>> lista = with_reader(filepath)
    [['HP-M600-DESENVOLVIMENTO', '192.168.17.20', 'off', '20'], ['MY_PHONE', '192.168.18.21', '421', '0']]
    """

    with open(filepath, "r", encoding="UTF-8") as file_:
        file_ = file_.readlines()
        lista = []
        for line in file_:
            line = line.replace("\n", "").split(",")
            lista.append([line[0], line[1], line[2], line[3]])
        return lista
    

def with_writer(filepath: str, listas: list, /):
    """Writes a list of lists to a CSV/txt file.

    The function writes each list in the 'listas' parameter as a row in the CSV/txt file.
    The CSV/txt file is created or overwritten during the process.

    Example:
    >>> filepath = 'default_ping-a.txt'
    >>> lista_to_write = [['HP-M600-DESENVOLVIMENTO', '192.168.17.20', 'off', '20'], ['MY_PHONE', '192.168.18.21', '421', '0']]
    >>> with_writer(filepath, lista_to_write)
    """

    with open(filepath, "w", encoding="UTF-8") as file_:
        for packet in listas:
            packet = ",".join(packet)
            file_.write(packet + "\n")

def ping_now(listas: list) -> list:
    """Pings a list of IP addresses and updates the packet information with the ping results.
    
    The function uses the ping3 library. Ensure it is installed using: pip install ping3

    Example:
    >>> packet_list = [['Server1', '192.168.1.1', '0', '0'], ['Server2', '192.168.1.2', '0', '0']]
    >>> updated_list = ping_now(packet_list)
    [['Server1', '192.168.1.1', '10', '0'], ['Server2', '192.168.1.21', '389', '0']]
    """

    lista_atualized = []
    for packet in listas:
        pingg = ping(packet[1], timeout=0.5, size=112)
        result_ping = "off" if pingg==None else round(pingg*1000)

        if type(result_ping) is int:
            packet[2] = str(result_ping)
            packet[3] = "0"
        else:   
            packet[2] = result_ping
            packet[3] = str(int(packet[3]) + 1)

        lista_atualized.append([packet[0], packet[1], packet[2], packet[3]])

    return lista_atualized

def clear_terminal():
    """Clears the terminal screen.
    
    This function detects the operating system and executes the appropriate command
    to clear the terminal. On Windows, it uses 'cls', and on Unix-based systems (Linux, macOS), it uses 'clear'.

    Example:
    >>> clear_terminal()
    """

    os.system("cls" if os.name == "nt" else "clear")

def main(filepath: str, /, **keywords: dict):
    """Continuously monitors and updates network information.
    
    This function reads network information from a CSV file, pings the IP addresses,
    updates the file with the ping results, displays an interface, and repeats the process
    in a loop with a 10-second delay. Additional keyword arguments can be passed to customize
    the appearance of the interface.

    Example:
    >>> main("default_ping-a.txt", device=27, ip=21, ping=21, fail=20)
                                               04/02/2024 18:42:31
    -------------------------------------------------------------------------------------------------
    |          DEVICE           ||         IP          ||        PING         ||        FAIL        |
    -------------------------------------------------------------------------------------------------
    |  HP-M600-DESENVOLVIMENTO  ||    192.168.17.20    ||         OFF         ||         21         |
    |         MY_PHONE          ||    192.168.18.21    ||         139         ||         0          |
    -------------------------------------------------------------------------------------------------
    """

    while True:
        wt_rd = with_reader(filepath)
        pg_nw = ping_now(wt_rd)
        wt_wr = with_writer(filepath, pg_nw)
        interface.interface(pg_nw, **keywords)
        sleep(10)
        clear_terminal()

main("default_ping-a.txt", device=27, ip=21, ping=21, falhas=20)

if __name__ == "__main__":
    # main("default_ping-a.txt", device=27, ip=21, ping=21, fail=20)
    pass
