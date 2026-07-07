import curses
from curses import window

# def move(y: int, x: int) -> list:
#     snake = [[0,2], [0,1], [0,0]]
#     old_snake = snake.copy()

#     if old_snake != snake:
#         snake[1] = old_snake[0]
#         snake[2] = old_snake[1]

#     return snake



def main(stdscr: window):
    curses.curs_set(0)
    x, y = 0, 0
    snake = [[0,2], [0,1], [0,0]]
    old_snake = snake.copy()
    while True:
        comand = stdscr.getch()
        height, width = stdscr.getmaxyx()

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

        snake[0] = [y, x]

        if old_snake != snake:
            snake[1] = old_snake[0]
            snake[2] = old_snake[1]
            try:
                stdscr.addstr(*old_snake[-1], " ")
            except curses.error:
                pass

        try:
            stdscr.addstr(*snake[0], "@")
            stdscr.addstr(*snake[1], "@")
            stdscr.addstr(*snake[2], "@")
            stdscr.refresh()
        except curses.error:
            pass

        old_snake = snake.copy()
curses.wrapper(main)