from game_controller import GameController

SPACE = {'w': 850, 'h': 850}
gc = GameController()
gc.create_board()


def setup():
    size(SPACE['w'], SPACE['h'])


def draw():
    background(200, 200, 200)
    gc.hold_disk(mouseX)
    noStroke()
    fill(0, 50, 200)
    rect(0, 80, 860, 890)
    gc.refresh()
    gc.check_win()


def mousePressed():
    if not gc.game_over:
        gc.handle_mouse()
