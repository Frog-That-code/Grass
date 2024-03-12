import time
import random 
import curses 
from curses import wrapper 
screen = curses.initscr() 
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
curses.init_pair(8, 9, curses.COLOR_BLACK)
curses.init_color(9, 255, 230, 115)

lines = curses.LINES // 2
cols = curses.COLS // 2

def main(stdscr):
    saveFile = open("saveFile.txt", "a+")
    saveFile.close()
    saveFile = open("saveFile.txt", "r")
    data = saveFile.readlines()
    data1 = []
    #gets points from saveFile
    for i in range(len(data)):
        idk = str(data[i])
        data1.append(idk)
    if not data:
        points = 0
    else:
        points = int(data[0])
    saveFile.close()
    colo = 1
    fortnite = 0
    #check for saved skins
    if "yellow\n" in data1:
        yellow = 1
    else:
        yellow = 0
    if "magenta\n" in data1:
        magenta = 1
    else:
        magenta = 0
    if "cyan\n" in data1:
        cyan = 1
    else:
        cyan = 0
    if "white\n" in data1:
        white = 1
    else:
        white = 0
    #main game loop
    while True:
        curses.curs_set(0)
        stdscr.clear()
        grass = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
        stdscr.addstr(lines, cols, "#_#_#_#_#", curses.color_pair(colo)| curses.A_UNDERLINE | curses.A_BOLD)
        stdscr.addstr(lines - 5, cols + 4, str(points), curses.color_pair(22)| curses.A_BOLD) 
        stdscr.refresh()
        while True: 
            for i in range(len(grass)):
                for e in range(5):
                    if grass[i][e] == " ":
                        if i == 0 or grass[i - 1][e] == "#":
                            beans = random.randint(1, 2)
                            if beans == 1:
                                grass[i][e] = "#"
            time.sleep(random.randint(1, 5))
            gr = ' '.join(grass[0])
            gr1 = ' '.join(grass[1])
            gr2 = ' '.join(grass[2])
            gr3 = ' '.join(grass[3])
            stdscr.addstr(curses.LINES // 2 - 1, curses.COLS // 2, gr, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 2, curses.COLS // 2, gr1, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 3, curses.COLS // 2, gr2, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.addstr(curses.LINES // 2 - 4, curses.COLS // 2, gr3, curses.color_pair(colo) | curses.A_BOLD)
            stdscr.refresh()
            if grass[3][0] == "#" and grass[3][1] == "#" and grass[3][2] == "#" and grass[3][3] == "#" and grass[3][4] == "#":
                break
        stdscr.addstr(lines + 1, cols - 18, "[s] - Shop, [Backspace] - Cut grass, [c] - Skins")
        stdscr.refresh()
        curses.flushinp()
        flum = stdscr.getch()
        #Cuts grass
        if flum == curses.KEY_BACKSPACE:
            points = points + 1
            continue
        # Opens skins menu
        elif flum == ord('c'):
            curses.curs_set(1)
            fortnite = 0 
            yellow1 = 8
            magenta1 = 8
            cyan1 = 8
            white1 = 8
            if white == 1:
                white1 = 5
            if cyan == 1:
                cyan1 = 4
            if magenta == 1:
                magenta1 = 3
            if yellow == 1:
                yellow1 = 2
            stdscr.clear()
            stdscr.addstr(lines, cols, "green", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(lines + 1, cols, "yellow", curses.color_pair(yellow1) | curses.A_BOLD)
            stdscr.addstr(lines + 2, cols, "magenta", curses.color_pair(magenta1) | curses.A_BOLD)
            stdscr.addstr(lines + 3, cols, "cyan", curses.color_pair(cyan1) | curses.A_BOLD)
            stdscr.addstr(lines + 4, cols, "white", curses.color_pair(white1) | curses.A_BOLD)
            stdscr.addstr(lines + 5, cols - 15, "[e] - Enter, [q] - Quit, [w] - Up, [s] - Down")
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
            curses.curs_set(1)
            fortnite = 0 
            grey1 = 8
            grey2 = 8
            grey3 = 8
            grey4 = 8
            if points >= 150:
                grey4 = 1
            if points >= 50:
                grey3 = 1
            if points >= 25:
                grey2 = 1
            if points >= 10:
                grey1 = 1
            stdscr.clear()
            stdscr.addstr(lines, cols, "yellow - 10", curses.color_pair(grey1) | curses.A_BOLD)
            stdscr.addstr(lines + 1, cols, "magenta - 25", curses.color_pair(grey2) | curses.A_BOLD)
            stdscr.addstr(lines + 2, cols, "cyan - 50", curses.color_pair(grey3) | curses.A_BOLD)
            stdscr.addstr(lines + 3, cols, "white - 150", curses.color_pair(grey4) | curses.A_BOLD)
            stdscr.addstr(lines + 4, cols - 15, "[e] - Enter, [q] - Quit, [w] - Up, [s] - Down")
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
                    if y == lines and points >= 10 and yellow != 1:
                        colo = 2
                        yellow = 1
                        points = points - 10
                        break
                    elif y == lines + 1 and points >= 25 and magenta != 1 and yellow == 1:
                        colo = 3
                        magenta = 1
                        points = points - 25
                        break
                    elif y == lines + 2 and points >= 50 and cyan != 1 and magenta == 1:
                        colo = 4
                        cyan = 1
                        points = points - 50
                        break
                    elif y == lines + 3 and points >= 150 and white != 1 and cyan == 1:
                        colo = 5
                        white = 1
                        points = points - 150
                        break
            continue
        else:
            saveFile = open("saveFile.txt", "w+")
            saveFile.seek(0)
            saveFile.truncate()
            saveFile.write(str(points) + "\n")
            if yellow == 1:
                saveFile.write("yellow\n")
            if magenta == 1:
                saveFile.write("magenta\n")
            if cyan == 1:
                saveFile.write("cyan\n")
            if white == 1:
                saveFile.write("white\n")
            saveFile.close()
            break

wrapper(main)
