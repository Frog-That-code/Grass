import time
import random
import curses
from curses import wrapper

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

lines = curses.LINES // 2
cols = curses.COLS // 2

grass = ["# #   #  ",
        "  # #   ",
        "# # #   ",
        "  #     #"]

def main(stdscr):
    points = 0
    while True:
        stdscr.clear()
        stdscr.addstr(lines, cols, "#_#_#_#_#", curses.color_pair(1)| curses.A_UNDERLINE | curses.A_BOLD)
        stdscr.addstr(lines - 5, cols + 4, str(points), curses.color_pair(2)| curses.A_BOLD) 
        stdscr.refresh()
        for i in range(6):
            if i == 1:
                stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, grass[random.randint(0, 1)], curses.color_pair(1) | curses.A_BOLD) 
                stdscr.refresh()
            if i == 2:
                balls = random.randint(2, 3)
                stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, grass[balls], curses.color_pair(1) | curses.A_BOLD) 
                if balls == 2:
                    stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # #  ", curses.color_pair(1) | curses.A_BOLD) 
                else:
                    stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # # #", curses.color_pair(1) | curses.A_BOLD)
                stdscr.refresh()                                
            if i == 3:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "#     #  ", curses.color_pair(1) | curses.A_BOLD)
                if balls == 2:
                    stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # #  ", curses.color_pair(1) | curses.A_BOLD)    
                else:
                    stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # # #", curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, "# # # # #", curses.color_pair(1) | curses.A_BOLD)
                stdscr.refresh()
            if i == 4:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "# # # #  ", curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, "# # # # #", curses.color_pair(1) | curses.A_BOLD)
                stdscr.refresh()
            if i == 5:
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, "# # # # #", curses.color_pair(1) | curses.A_BOLD)
                stdscr.refresh()
                break
            time.sleep(random.randint(5, 10))
        flum = stdscr.getch()
        if flum == curses.KEY_BACKSPACE:
            points = points + 1
            continue
        else:
            break

wrapper(main)
