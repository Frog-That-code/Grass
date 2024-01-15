import os
import time
import random
from colorama import Fore

class format:
    end = '\033[0m'
    underline = '\033[4m'

os.system('clear')

print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)

grass = ["# #   #  ",
        "  # #   ",
        "# # #   ",
        "  #     #"]

for i in range(6):
    if i == 1:
        print(Fore.GREEN + grass[random.randint(0, 1)])
        print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)
    if i == 2:
        balls = random.randint(2, 3)
        print(Fore.GREEN + grass[balls])
        if balls == 2:
            print(Fore.GREEN + "# # # #  ")
        else:
            print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)
    if i == 3:
        print(Fore.GREEN + "#     #  ")
        if balls == 2:
            print(Fore.GREEN + "# # # #  ")
        else:
            print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)
    if i == 4:
        print(Fore.GREEN + "# # # #  ")
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)
    if i == 5:
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + "# # # # #")
        print(Fore.GREEN + format.underline + '#_#_#_#_#' + format.end)
        break
    time.sleep(random.randint(5, 30))
    os.system('clear')