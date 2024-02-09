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
curses.init_pair(22, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLACK)


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
                        if i == 0 or grass[i - 1][e] == 1:
                            beans = random.randint(1, 5)
                            if beans == 3:
                                grass[i][e] = "#"
                            else:
                                continue
                    gr = ' '.join(grass[0])
                    gr1 = ' '.join(grass[1])
                    gr2 = ' '.join(grass[2])
                    gr3 = ' '.join(grass[3])
                    stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, gr, curses.color_pair(1) | curses.A_BOLD)
                    stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, gr1, curses.color_pair(1) | curses.A_BOLD)
                    stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, gr2, curses.color_pair(1) | curses.A_BOLD)
                    stdscr.addstr(curses.LINES // 2 - 4, curses.COLS // 2, gr3, curses.color_pair(1) | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(random.randint(2, 6))
            stdscr.getch()



wrapper(main)
