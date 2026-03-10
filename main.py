import math
from colorama import Fore, Style, init
import time


def moivre_binet(n:int) ->int:
    return 1 / math.sqrt(5) * ((1 + math.sqrt(5)) / 2)**n - 1 / math.sqrt(5) * ((1 - math.sqrt(5)) / 2)**n  # pyright: ignore[reportReturnType]


def main():
    
    i:int = 0

    init(autoreset=True) # colorama: Automatically resets color after each print
    try:
        for i in range(1500):
            fn = moivre_binet(i)

            print(f"\r{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{i:4}: {Fore.YELLOW}{Style.BRIGHT}{fn:.0f}", end="", flush=True)
            time.sleep(0.05)

    except OverflowError:
        print(f"\nJetzt sind Sie zu weit gegangen! {Fore.RED}{Style.BRIGHT}{i}")


if __name__ == '__main__':
    main()

