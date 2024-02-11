import time
import random 
import curses 
from curses import wrapper 
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

lines = curses.LINES // 2
cols = curses.COLS // 2




def main(stdscr):
    points = 85
    colo = 1
    fortnite = 0
    grey1 = 6
    grey2 = 6
    grey3 = 6
    grey4 = 6
    yellow = 0
    magenta = 0
    cyan = 0
    white = 0
    while True:
        #main game loop
        stdscr.clear()
        grass = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
        stdscr.addstr(lines, cols, "#_#_#_#_#", curses.color_pair(colo)| curses.A_UNDERLINE | curses.A_BOLD)
        stdscr.addstr(lines - 5, cols + 4, str(points), curses.color_pair(22)| curses.A_BOLD) 
        stdscr.refresh()
        time.sleep(random.randint(1, 5))
        while grass[3][0] != "#" and grass[3][1] != "#" and grass[3][2] != "#" and grass[3][3] != "#" and grass[3][4] != "#": 
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
            stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, gr, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, gr1, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, gr2, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 4, curses.COLS // 2, gr3, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.refresh()
            time.sleep(random.randint(1, 5))
        stdscr.addstr(lines + 1, cols + 1, "[s] - Shop, [Backspace] - Cut grass, [c] - Skins")
        stdscr.refresh()
        flum = stdscr.getch()
        #Cuts grass
        if flum == curses.KEY_BACKSPACE:
            points = points + 1
            continue
        # Opens skins menu
        elif flum == ord('c'):
            fortnite = 0 
            yellow1 = 7
            magenta1 = 7
            cyan1 = 7
            white1 = 7
            if yellow == 1 and magenta == 1 and cyan == 1 and white == 1:
                yellow1 = 2
                magenta1 = 3
                cyan1 = 4
                white1 = 5
            elif magenta == 1 and yellow == 1 and cyan == 1:
                magenta1 = 3
                yellow1 = 2
                cyan1 = 4
            elif yellow == 1 and magenta == 1:
                magenta1 = 3
                yellow1 = 2
            elif yellow == 1:
                yellow1 = 1
            stdscr.clear()
            stdscr.addstr(lines, cols, "green", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(lines + 1, cols, "yellow", curses.color_pair(yellow1) | curses.A_BOLD)
            stdscr.addstr(lines + 2, cols, "magenta", curses.color_pair(magenta1) | curses.A_BOLD)
            stdscr.addstr(lines + 3, cols, "cyan", curses.color_pair(cyan1) | curses.A_BOLD)
            stdscr.addstr(lines + 4, cols, "white", curses.color_pair(white1) | curses.A_BOLD)
            stdscr.addstr(lines + 5, cols, "[e] - Enter, [q] - Quit, [w] - Up, [s] - Down")
            stdscr.move(lines, cols)
            stdscr.refresh()
            # move up and down and close skins
            while fortnite != ord('q'):
                fortnite  = stdscr.getch()
                if fortnite == ord('w'):
                    y, x = stdscr.getyx()
                    if y == lines:
                        continue
                    else:
                        stdscr.move(y - 1, x)
                if fortnite == ord('s'):
                    y, x = stdscr.getyx()
                    if y == lines + 4:
                        continue
                    else:
                        stdscr.move(y + 1, x)
                # choose color
                if fortnite == ord('e'):
                    y, x = stdscr.getyx()
                    if y == lines:
                        colo = 1
                        break
                    elif y == lines + 1 and yellow == 1:
                        colo = 2
                        break
                    elif y == lines + 2 and magenta == 1:
                        colo = 3
                        break
                    elif y == lines + 3 and cyan == 1:
                        colo = 4
                        break
                    elif y == lines + 4 and white == 1:
                        colo = 5
                        break
            continue
        # opens shop
        elif flum == ord('s'):
            fortnite = 0 
            grey1 = 6
            grey2 = 6
            grey3 = 6
            grey4 = 6
            if points >= 150:
                grey1 = 1
                grey2 = 1
                grey3 = 1
                grey4 = 1
            elif points >= 50:
                grey1 = 1
                grey2 = 1
                grey3 = 1
            elif points >= 25:
                grey1 = 1
                grey2 = 1
            elif points >= 10:
                grey1 = 1
            stdscr.clear()
            stdscr.addstr(lines, cols, "yellow - 10", curses.color_pair(grey1) | curses.A_BOLD)
            stdscr.addstr(lines + 1, cols, "magenta - 25", curses.color_pair(grey2) | curses.A_BOLD)
            stdscr.addstr(lines + 2, cols, "cyan - 50", curses.color_pair(grey3) | curses.A_BOLD)
            stdscr.addstr(lines + 3, cols, "white - 150", curses.color_pair(grey4) | curses.A_BOLD)
            stdscr.addstr(lines + 4, cols, "[e] - Enter, [q] - Quit, [w] - Up, [s] - Down")
            stdscr.move(lines, cols)
            stdscr.refresh()
            # move up and down and close shop
            while fortnite != ord('q'):
                fortnite  = stdscr.getch()
                if fortnite == ord('w'):
                    y, x = stdscr.getyx()
                    if y == lines:
                        continue
                    else:
                        stdscr.move(y - 1, x)
                if fortnite == ord('s'):
                    y, x = stdscr.getyx()
                    if y == lines + 3:
                        continue
                    else:
                        stdscr.move(y + 1, x)
                # choose color
                if fortnite == ord('e'):
                    y, x = stdscr.getyx()
                    if y == lines and points >= 10:
                        colo = 2
                        yellow = 1
                        points = points - 10
                        break
                    elif y == lines + 1 and points >= 25:
                        colo = 3
                        magenta = 1
                        points = points - 25
                        break
                    elif y == lines + 2 and points >= 50:
                        colo = 4
                        cyan = 1
                        points = points - 50
                        break
                    elif y == lines + 3 and points >= 150:
                        colo = 5
                        white = 1
                        points = points - 150
                        break
            continue
        else:
            break

wrapper(main)
