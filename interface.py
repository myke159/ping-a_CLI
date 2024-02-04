#/env/scripts python3

__version__ = "0.1.1"
__author__ = "Myke Bueno"
__licence__ = "Public Domain"

from datetime import datetime

def line(caracter: str, width: int) -> print:
    """Print a line with specific characters.
    
    This function is designed to print a line of specific characters.
    The 'caracter' parameter determines the character to be repeated,
    and the 'width' parameter determines the length of the line.

    Example:
    >>> line('-', 10)
    ----------
    """

    return print(f"{caracter * width}")

def header(**keywords: dict) -> print:
    """Creates and print the centered header with specified column names and sizes.
    
    This function uses the 'line' function to draw lines for the header and does not print an empty line 
    after the header.

    Example:
    >>> header(device=27, ip=21, ping=21, fail=20)
                                           04/02/2024 18:42:31
    -------------------------------------------------------------------------------------------------
    |          DEVICE           ||         IP          ||        PING         ||        FAIL        |
    -------------------------------------------------------------------------------------------------
    """

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{now:^{sum(keywords.values()) + (len(keywords.items()) * 2)}}")

    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))
    for kw in keywords:
        print(f"|{kw.upper():^{keywords[kw]}}|", end="")
    print() # way to remove this print()
    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))

def body(widths: int, packets: str) -> print:
    """Print a formatted body with specific widths and data packets.
    
    This function uses the 'line' function to draw a line after printing the body.

    Example:
    >>> body((27, 21, 21, 20), ((), ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0")))
    |     HP-3015-COMERCIAL     ||    192.168.16.48    ||         53          ||         0          |
    -------------------------------------------------------------------------------------------------
    """

    for packet in packets:
        for i, arg in enumerate(packet):
            print(f"|{arg.upper():^{widths[i]}}|", end="")
        print() # way to remove this print()
    line("-", sum(widths) + (len(widths) * 2))

def interface(packets: int, **keywords: dict) -> print:
    """Prints an interface with a header and body containing specified packets and column information.
    
    This function combines the 'header' and 'body' functions to create a user interface for displaying
    network information. The 'header' function is responsible for printing column headers,
    and the 'body' function is used to print the data rows.
    
    Example:
    >>> results = (("HP-M600-DESENVOLVIMENTO", "192.168.17.20", "200", "0"), ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0"))
    >>> interface((results), device=27, ip=21, ping=21, fail=20)
                                           04/02/2024 18:42:31
    -------------------------------------------------------------------------------------------------
    |          DEVICE           ||         IP          ||        PING         ||        FAIL        |
    -------------------------------------------------------------------------------------------------
    |  HP-M600-DESENVOLVIMENTO  ||    192.168.17.20    ||         200         ||         0          |
    |     HP-3015-COMERCIAL     ||    192.168.16.48    ||         53          ||         0          |
    -------------------------------------------------------------------------------------------------
    """

    header(**keywords)
    body(tuple(keywords.values()), packets)
    

if __name__ == "__main__":
    results = (("HP-M600-DESENVOLVIMENTO", "192.168.17.20", "200", "0"), ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0"))
    interface((results), device=27, ip=21, ping=21, fail=20)
    pass
