from game_controller import GameController

gc = GameController()


def test_constructor():
    """
    Test required constructor args
    None => None
    """
    assert not gc.game_over and \
           len(gc.board) == 0 and \
           gc.ROW == 6 and \
           gc.COL == 7 and \
           gc.red_turn and \
           gc.if_red and \
           gc.circle_size == 90 and \
           gc.start_point == 50 and \
           len(gc.falling_circle) == 0 and \
           gc.blank_size == 100 and \
           gc.line_size == 20 and \
           gc.WIN_MOVES == 4 and \
           not gc.red_win and \
           not gc.yellow_win and \
           gc.start_time == 999 and \
           not gc.scored


def test_create_board():
    """
    Test create_board function
    None => None
    """
    gc.create_board()
    assert len(gc.board) == gc.ROW
    for i in gc.board:
        assert len(i) == gc.COL


def test_drop_disk():
    """
    Test drop_disk function
    None => None
    """
    gc.drop_disk(0, 0, 1)
    assert gc.board[0][0] == 1


def test_is_position_blank():
    """
    Test is_position_blank function
    None => None
    """
    assert gc.is_position_blank(1) and \
           gc.is_position_blank(2) and \
           gc.is_position_blank(3)


def test_next_row():
    """
    Test next_row function
    None => None
    """
    assert gc.next_row(0) == 1 and \
           gc.next_row(1) == 0 and \
           gc.next_row(2) == 0


def test_check_if_over():
    """
    Test check_if_over function
    None => None
    """
    assert not gc.check_if_over()


def test_update():
    """
    Test update function
    None => None
    """
    gc.update(100)
    assert gc.board[1][0] == 1


def test_check_win():
    """
    Test check_win function
    None => None
    """
    gc.drop_disk(2, 0, 1)
    gc.drop_disk(3, 0, 1)
    gc.check_win()
    assert gc.red_win


def test_ai():
    """
    Test ai function, see if ai drop its disk or not
    None => None
    """
    gc.ai()
    yellow_disk_count = 0
    for i in gc.board:
        for j in i:
            if j == 2:
                yellow_disk_count += 1
    assert yellow_disk_count == 1
