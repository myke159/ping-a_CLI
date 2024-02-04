
"""
------------------------------------------------------------------------------------------------
|          DEVICE  [12:19]  ||         IP          ||        PING        ||        Fail        |
------------------------------------------------------------------------------------------------
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||         0          |
|  HP-M600-DESENVOLVIMENTO  ||   192.168.172.282   ||        off         ||         0          |
------------------------------------------------------------------------------------------------
"""


def line(caracter: str, width: int) -> print:
    return print(f"{caracter * width}")


def header(**keywords: dict) -> print:
    """
    
    """
    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))
    for kw in keywords:
        print(f"|{kw.upper():^{keywords[kw]}}|", end="")
    print() # way to remove this print()
    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))

def body(widths: int, packets: str) -> print:
    """
    
    """
    for packet in packets:
        for i, arg in enumerate(packet):
            print(f"|{arg.upper():^{widths[i]}}|", end="")
        print()
    line("-", sum(widths) + (len(widths) * 2))

    
header(device=27, ip=21, ping=21, fail=20)


body((27, 21, 21, 20), (("HP-M600-DESENVOLVIMENTO", "192.168.17.20", "200", "0"), ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0")))