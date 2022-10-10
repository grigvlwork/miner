from minerobj import Field
from colorama import Fore, Back, Style

f = Field(9, 9, 10)
f.current_row = 5
f.current_col = 5
f.generate()
f.open_all()
for c in str(f):
    if c == "1":
        print(Fore.LIGHTBLUE_EX + c, end="")
    elif c == "2":
        print(Fore.LIGHTGREEN_EX + c, end="")
    elif c == "3":
        print(Fore.LIGHTRED_EX + c, end="")
    elif c == "4":
        print(Fore.BLUE + c, end="")
    elif c == "5":
        print(Fore.RED + c, end="")
    elif c == "6":
        print(Fore.LIGHTMAGENTA_EX + c, end="")
    elif c == "7":
        print(Fore.GREEN + c, end="")
    elif c == "8":
        print(Fore.MAGENTA + c, end="")
    elif c == "P":
        print(Fore.GREEN + Back.LIGHTRED_EX + c, end="")
    elif c == ".":
        print(Fore.WHITE + c, end="")
    elif c == "*":
        print(Fore.BLACK + Back.LIGHTRED_EX + c, end="")
    elif c == "X":
        print(Fore.YELLOW + Back.LIGHTRED_EX + c, end="")
    else:
        print(c, end="")
    print(Style.RESET_ALL, end="")



