import pyxel


def draw_hud(score=1):
    pyxel.text(10, 5, "Score: " + str(score), 7)


def draw_game_over(score=1):
    title = "GAME OVER"
    score_text = "You Scored: " + str(score) + " points"
    press_enter_text = "Press ENTER to try again"
    press_q_text = "Press Q to quit"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(score_text), pyxel.height / 12 * 5, score_text, 7)
    pyxel.text(center_text(press_enter_text), pyxel.height / 2, press_enter_text, 7)
    pyxel.text(center_text(press_q_text), pyxel.height / 12 * 7, press_q_text, 7)


def draw_ready_screen():
    title = "SNAKE SHORTEST PATH DEMO"
    press_one_text = "Press 1 to play SNAKE manually"
    press_two_text = "Press 2 to automatically play SNAKE with Breadth-First-Search"
    press_three_text = "Press 3 to automatically play SNAKE with A* Search"
    pyxel.text(center_text(title), pyxel.height / 3, title, 11)
    pyxel.text(center_text(press_one_text), pyxel.height / 12 * 5, press_one_text, 12)
    pyxel.text(center_text(press_two_text), pyxel.height / 2, press_two_text, 14)
    pyxel.text(center_text(press_three_text), pyxel.height / 12 * 7, press_three_text, 10)


def draw_manual_instructions():
    title = "Use WASD or Arrow Keys to move snake"
    sub_title = "Press P to pause, Q to quit, and E to force end"
    sub_sub_title = "Press ENTER to continue"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(sub_title), pyxel.height / 12 * 5, sub_title, 7)
    pyxel.text(center_text(sub_sub_title), pyxel.height / 12 * 7, sub_title, 7)


def draw_automatic_instructions():
    title = "Press P to pause, Q to quit, and E to force end"
    sub_title = "Press ENTER to continue"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)
    pyxel.text(center_text(sub_title), pyxel.height / 12 * 5, sub_title, 7)


def draw_avg_time_to_compute_path(time):
    title = f"Pathfinding Time: {round(time, 2)} ms"
    pyxel.text(10, pyxel.height - 10, title, 7)


def draw_pause_instructions():
    title = "Press P to unpause the game or Q to quit"
    pyxel.text(center_text(title), pyxel.height / 3, title, 7)


def draw_game_type(mode):
    game_type = None
    match mode:
        case 0:
            game_type = "Manual"
        case 1:
            game_type = "BFS"
        case 2:
            game_type = "A*"
    pyxel.text(right_text(game_type), pyxel.height - 10, game_type, 7)


def center_text(text, char_width=pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (pyxel.width - text_width) / 2


def right_text(text, char_width=pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return pyxel.width - (text_width + char_width)
