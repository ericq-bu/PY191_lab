import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    display = text[:cursor] + "|" + text[cursor:]

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # ==========================================================
        # LEFT ARROW
        #
        # Move the cursor one position to the left.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 2
        # display = "He|llo"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_LEFT:
            cursor += -1
            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # RIGHT ARROW
        #
        # Move the cursor one position to the right.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 4
        # display = "Hell|o"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:

            cursor += 1

            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # BACKSPACE
        #
        # Delete the character immediately before the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Helo"
        # cursor  = 2
        # display = "He|lo"
        #
        # ---------------- ANSWER ----------------

        elif key in (8, 127, curses.KEY_BACKSPACE):

            cursor += -1
            text = text[:cursor] + text[cursor + 1:]
            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        # ==========================================================
        # ENTER
        #
        # Insert a newline at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hel\nlo"
        # cursor  = 4
        # display = "Hel\n|lo"
        #
        # ---------------- ANSWER ----------------

        elif key == 10:

            text = text[:cursor] + "\n" + text[cursor:]
            display = text[:cursor] + "|" + text[cursor:]
            cursor += 1

        # ----------------------------------------

        # ==========================================================
        # INSERT CHARACTER
        #
        # Insert the typed character at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # Typing X
        #
        # After
        # text    = "HelXlo"
        # cursor  = 4
        # display = "HelX|lo"
        #
        # ---------------- ANSWER ----------------

        elif 32 <= key <= 126:

            text = text[:cursor] + chr(key) + text[cursor:]
            cursor += 1
            display = text[:cursor] + "|" + text[cursor:]

        # ----------------------------------------

        #BONUS: Can you figure out how to select one line up/down by yourself?

        elif key == curses.KEY_UP:
            lines_before = text[:cursor].split("\n")
            current_line = len(lines_before) - 1
            current_col = len(lines_before[-1])

            if current_line > 0:
                all_lines = text.split("\n")
                target_line = current_line - 1
                target_col = min(current_col, len(all_lines[target_line]))
                
                new_cursor = 0
                for i in range(target_line):
                    new_cursor += len(all_lines[i]) + 1
                new_cursor += target_col

                cursor = new_cursor


        elif key == curses.KEY_DOWN:
            lines_before = text[:cursor].split("\n")
            current_line = len(lines_before) - 1
            current_col = len(lines_before[-1])
            all_lines = text.split("\n")

            if current_line < len(all_lines) - 1:
                target_line = current_line + 1
                target_col = min(current_col, len(all_lines[target_line]))
                
                new_cursor = 0
                for i in range(target_line):
                    new_cursor += len(all_lines[i]) + 1
                new_cursor += target_col

                cursor = new_cursor

curses.wrapper(main)
