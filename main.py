import curses
from curses import window

def main(stdscr: window):
    curses.curs_set(0)
    x, y = 0, 0
    old_x, old_y = 0, 0
    while True:
        comand = stdscr.getch()
        height, width = stdscr.getmaxyx()
        
        stdscr.move(old_y, old_x)
        stdscr.clrtoeol()

        if comand == curses.KEY_UP:
            y -= 1
        elif comand == curses.KEY_DOWN:
            y += 1
        elif comand == curses.KEY_LEFT:
            x -= 1
        elif comand == curses.KEY_RIGHT:
            x += 1

        if y >= height:
            y = 0
        elif y < 0:
            y = height - 1
        
        if x >= width:
            x = 0
        elif x < 0:
            x = width - 1

        try:
            stdscr.addstr(y, x, "@")
            stdscr.refresh()
        except curses.error:
            pass

        old_y, old_x = y, x

curses.wrapper(main)