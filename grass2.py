import time
import random
import curses
from curses import wrapper

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

grass = ["# #   #  ",
        "  # #   ",
        "# # #   ",
        "  #     #"]

def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(curses.LINES // 2, curses.COLS // 2, "#_#_#_#_#", curses.color_pair(1)| curses.A_UNDERLINE)
        stdscr.refresh()
        for i in range(6):
            if i == 1:
                stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, grass[random.randint(0, 1)], curses.color_pair(1)) 
                stdscr.refresh()
            if i == 2:
                balls = random.randint(2, 3)
                stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, grass[balls], curses.color_pair(1)) 
                if balls == 2:
                    stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # #  ", curses.color_pair(1)) 
                else:
                    stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # # #", curses.color_pair(1))
                stdscr.refresh()                                
            if i == 3:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "#     #  ", curses.color_pair(1))
                if balls == 2:
                    stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # #  ", curses.color_pair(1))    
                else:
                    stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # # #", curses.color_pair(1))
                stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # # #", curses.color_pair(1))
                stdscr.refresh()
            if i == 4:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "# # # #  ", curses.color_pair(1))
                stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # # #", curses.color_pair(1))
                stdscr.refresh()
            if i == 5:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "# # # # #", curses.color_pair(1))
                stdscr.refresh()
                break
            time.sleep(random.randint(1, 3))
        flum = stdscr.getch()
        if flum == curses.KEY_BACKSPACE:
            continue
        else:
            break

wrapper(main)
