def line(caracter: str, width: int) -> print:
    """Print a line with specific characters.
    
    Parameters:
    - character (str): The character to be used to form the line.
    - length (int): The length of the line. If not specified, 
    the length will be automatically calculated.

    Example:
    >>> line('-', 10)
    ----------
    """

    return print(f"{caracter * width}")

def header(**keywords: dict) -> print:
    """Creates and print the centered header with specified column names and sizes.
    
    Parameters:
    - **keywords: Keyword arguments representing column names and their 
    corresponding sizes. Ex: header(device=27, ip=21, ping=21, fail=20)

    Example:
    >>> header(device=27, ip=21, ping=21, fail=20)
    -------------------------------------------------------------------------------------------------
    |          DEVICE           ||         IP          ||        PING         ||        FAIL        |
    -------------------------------------------------------------------------------------------------
    """

    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))
    for kw in keywords:
        print(f"|{kw.upper():^{keywords[kw]}}|", end="")
    print() # way to remove this print()
    line("-", sum(keywords.values()) + (len(keywords.items()) * 2))

def body(widths: int, packets: str) -> print:
    """Print a formatted body with specific widths and data packets.
    
    Parameters:
    - widths (int): The width of the columns.
    - packets (str): The data packets to be displayed.

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
    
    Parameters:
    - packets (int): The number of data packets to be displayed.
    - **keywords: Keyword arguments representing column names and their corresponding sizes.
      Ex: results = ("HP-M600-DESENVOLVIMENTO", "192.168.17.20", "200", "0"), 
                    ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0")
          interface((results), device=27, ip=21, ping=21, fail=20)
    
    Example:
    >>> interface((results), device=27, ip=21, ping=21, fail=20)
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
    results = ("HP-M600-DESENVOLVIMENTO", "192.168.17.20", "200", "0"), ("HP-3015-COMERCIAL", "192.168.16.48", "53", "0")
    interface((results), device=27, ip=21, ping=21, fail=20)
    pass
