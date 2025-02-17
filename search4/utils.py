from requests import get, RequestException
from colorama import Style
from colorama import Fore as Color


def result(address, site):
    try:
        agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) "
        agent += "Gecko/20100101 Firefox/62.0"
        headers = {"User-Agent": agent}
        r = get(address, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            print(
                Style.BRIGHT
                + Color.YELLOW
                + "> {}: Account found on {}\n".format(site, address)
                + Style.RESET_ALL
            )
        else:
            print(
                Style.BRIGHT
                + Color.GREEN
                + "[!] {} : Account not found on {}\n".format(site, address)
                + Style.RESET_ALL
            )
    except RequestException:
        print(
            Style.BRIGHT
            + Color.GREEN
            + "[!] {} : Account not found on {}\n".format(site, address)
            + Style.RESET_ALL
        )


def banner():
    print(
        Style.BRIGHT
        + Color.MAGENTA
        + """


          _/_/_/                                          _/        _/  _/
       _/          _/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/    _/  _/
        _/_/    _/_/_/_/  _/    _/  _/_/      _/        _/    _/  _/_/_/_/
           _/  _/        _/    _/  _/        _/        _/    _/      _/
    _/_/_/      _/_/_/    _/_/_/  _/          _/_/_/  _/    _/      _/


        > version 1.0
        > Script to find user account on various platforms.
""" + Style.RESET_ALL)
