import random
import curses
from curses import window

def main(stdscr: window):
    curses.curs_set(0)
    x, y = 0, 0
    snake = [[0,2], [0,1], [0,0]]
    old_snake = snake.copy()
    last_direction = None
    stdscr.nodelay(True)
    stdscr.timeout(100)
    stdscr.addstr(4, 5, "*")
    while True:
        direction = stdscr.getch()
        height, width = stdscr.getmaxyx()

        if direction != -1:
            last_direction = direction
        if last_direction is None:
            x += 1
        else:
            if last_direction == curses.KEY_UP:
                raw = stdscr.inch(y-1, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char != "@":
                    y -= 1
                else:
                    y += 1
                
                raw = stdscr.inch(y, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char == "*":
                    snake.insert(0, [y, x])
                    try:
                        for bit in snake:
                            stdscr.addstr(*bit, "@")
                        y_food = random.randint(1, height-2)
                        x_food = random.randint(3, width-2)
                        stdscr.addstr(y_food, x_food, "*")
                        stdscr.refresh()
                    except curses.error:
                        pass
                    old_snake = snake.copy()
                    continue

            elif last_direction == curses.KEY_DOWN:
                raw = stdscr.inch(y+1, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char != "@":
                    y += 1
                else:
                    y -= 1
                
                raw = stdscr.inch(y, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char == "*":
                    snake.insert(0, [y, x])
                    try:
                        for bit in snake:
                            stdscr.addstr(*bit, "@")
                        y_food = random.randint(1, height-2)
                        x_food = random.randint(3, width-2)
                        stdscr.addstr(y_food, x_food, "*")
                        stdscr.refresh()
                    except curses.error:
                        pass
                    old_snake = snake.copy()
                    continue
            elif last_direction == curses.KEY_LEFT:
                raw = stdscr.inch(y, x-1)
                char = chr(raw & curses.A_CHARTEXT)
                if char != "@":
                    x -= 1
                else:
                    x += 1
                
                raw = stdscr.inch(y, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char == "*":
                    snake.insert(0, [y, x])
                    try:
                        for bit in snake:
                            stdscr.addstr(*bit, "@")
                        y_food = random.randint(1, height-2)
                        x_food = random.randint(3, width-2)
                        stdscr.addstr(y_food, x_food, "*")
                        stdscr.refresh()
                    except curses.error:
                        pass
                    old_snake = snake.copy()
                    continue
            elif last_direction == curses.KEY_RIGHT:
                raw = stdscr.inch(y, x+1)
                char = chr(raw & curses.A_CHARTEXT)
                if char != "@":
                    x += 1
                else:
                    x -= 1
                
                raw = stdscr.inch(y, x)
                char = chr(raw & curses.A_CHARTEXT)
                if char == "*":
                    snake.insert(0, [y, x])
                    try:
                        for bit in snake:
                            stdscr.addstr(*bit, "@")
                        y_food = random.randint(1, height-2)
                        x_food = random.randint(3, width-2)
                        stdscr.addstr(y_food, x_food, "*")
                        stdscr.refresh()
                    except curses.error:
                        pass
                    old_snake = snake.copy()
                    continue

        if y >= height:
            y = 0
        elif y < 0:
            y = height - 1
        
        if x >= width:
            x = 0
        elif x < 0:
            x = width - 1

        snake[0] = [y, x]
        for i in range(1, len(snake)):
            snake[i] = old_snake[i-1]
        try:
            stdscr.addstr(*old_snake[-1], " ")
        except curses.error:
            pass

        try:
            for bit in snake:
                 stdscr.addstr(*bit, "@")
            stdscr.refresh()
        except curses.error:
            pass

        old_snake = snake.copy()
curses.wrapper(main)