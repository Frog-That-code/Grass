import curses
from curses import wrapper
import random
import time

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
curses.start_color()
#init colors 
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

grass = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
lines = curses.LINES // 2
cols = curses.COLS // 2

def main (stdscr):
        while True:
            #main game loop
            stdscr.clear()
            stdscr.addstr(lines, cols, "#_#_#_#_#", curses.color_pair(1)| curses.A_UNDERLINE | curses.A_BOLD)
            stdscr.refresh()
            for i in range(len(grass)):
                for e in range(5):
                    if grass[i][e] == " ":
                        if i == 0 or grass[i - 1][e] == "#":
                            beans = random.randint(1, 2)
                            if beans == 1:
                                grass[i][e] = "#"
                gr = ' '.join(grass[0])
                gr1 = ' '.join(grass[1])
                gr2 = ' '.join(grass[2])
                gr3 = ' '.join(grass[3])
                stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, gr, curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, gr1, curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, gr2, curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(curses.LINES // 2 - 4, curses.COLS // 2, gr3, curses.color_pair(1) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(random.randint(1, 5))




wrapper(main)
