from disk import RedDisk
from disk import YellowDisk
import random
import time


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self):
        self.game_over = False
        self.board = []
        self.ROW = 6
        self.COL = 7
        self.red_turn = True
        self.if_red = True
        self.circle_size = 90
        self.start_point = 50
        self.falling_circle = []
        self.blank_size = 100
        self.line_size = 20
        self.WIN_MOVES = 4
        self.red_win = False
        self.yellow_win = False
        self.start_time = 999
        self.scored = False

    def create_board(self):
        """
        Create a game board, the size will depends on ROW and COL. "0" is default value, means blank spot.
        None => None
        """
        for i in range(self.ROW):
            self.board.append([])
            for i2 in range(self.COL):
                self.board[i].append(0)

    def drop_disk(self, row, col, disk):
        """
        Replace user's number (1 or 2) in board list.
        Integer, Integer, String => None
        """
        self.board[row][col] = disk

    def is_position_blank(self, col):
        """
        Check if the top line of this column is "0" or not, "0" means still has blank spot.
        Integer => Boolean
        """
        if self.board[-1][col] == 0:
            return True

        else:
            return False

    def next_row(self, col):
        """
        Get the lowest available blank spot of a column.
        Integer => Integer
        """
        for i in range(self.ROW):
            if self.board[i][col] == 0:
                return i

    def draw_blank(self):
        """
        Draw several blank spots on the game board.
        None => None
        """
        for i in range(self.COL):
            for i2 in range(self.ROW):
                noStroke()
                fill(200, 200, 200)
                rect(i * (self.blank_size + self.line_size) + self.line_size,
                     i2 * (self.blank_size + self.line_size) + self.blank_size,
                     self.blank_size, self.blank_size)

    def check_if_over(self):
        """
        Check if the board still contains "0" or not. If true, means every spot has a disk.
        None => None
        """
        blank_count = 0
        for i in self.board:
            for i2 in i:
                if i2 == 0:
                    blank_count += 1
        if blank_count == 0:
            self.game_over = True

    def check_win(self):
        """
        Check the game board and determine if players win or not
        None => None
        """
        red_disk = 1
        yellow_disk = 2
        red_row = 0
        red_col = 0
        yellow_row = 0
        yellow_col = 0

        # Check horizontal direction
        for i in self.board:
            for j in i:
                if j == red_disk:
                    red_row += 1
                    yellow_row = 0
                elif j == yellow_disk:
                    yellow_row += 1
                    red_row = 0
                elif j == 0:
                    red_row = 0
                    yellow_row = 0
                if red_row == self.WIN_MOVES:
                    self.red_win = True
                elif yellow_row == self.WIN_MOVES:
                    self.yellow_win = True
            red_row = 0
            yellow_row = 0

        # Check vertical direction
        for i in range(self.COL):
            for j in self.board:
                if j[i] == red_disk:
                    red_col += 1
                    yellow_col = 0
                elif j[i] == yellow_disk:
                    yellow_col += 1
                    red_col = 0
                elif j == 0:
                    red_col = 0
                    yellow_col = 0
                if red_col == self.WIN_MOVES:
                    self.red_win = True
                elif yellow_col == self.WIN_MOVES:
                    self.yellow_win = True
            red_col = 0
            yellow_col = 0

        # Check bottom-left to up-right direction
        for i in range(self.ROW - 3):
            for j in range(self.COL - 3):
                if self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == \
                        self.board[i][j] == red_disk:
                    self.red_win = True
                elif self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == \
                        self.board[i][j] == yellow_disk:
                    self.yellow_win = True

        # Check up-left to bottom right direction
        for i in range(3, self.ROW):
            for j in range(self.COL - 3):
                if self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3] == \
                        self.board[i][j] == red_disk:
                    self.red_win = True
                elif self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3] == \
                        self.board[i][j] == yellow_disk:
                    self.yellow_win = True

    def update(self, col):
        """
        Update the board once user make move.
        Integer => None
        """
        self.check_if_over()
        FIRSTLINE = 125
        SECONDLINE = FIRSTLINE + self.blank_size + self.line_size
        THIRDLINE = SECONDLINE + self.blank_size + self.line_size
        FOURTHLINE = THIRDLINE + self.blank_size + self.line_size
        FIFTHLINE = FOURTHLINE + self.blank_size + self.line_size
        SISTHLINE = FIFTHLINE + self.blank_size + self.line_size
        FIRST_COL = 0
        SECOND_COL = 1
        THIRD_COL = 2
        FOURTH_COL = 3
        FIFTH_COL = 4
        SISTH_COL = 5
        SEVEN_COL = 6
        if col <= FIRSTLINE:
            col = FIRST_COL
        elif FIRSTLINE < col <= SECONDLINE:
            col = SECOND_COL
        elif SECONDLINE < col <= THIRDLINE:
            col = THIRD_COL
        elif THIRDLINE < col <= FOURTHLINE:
            col = FOURTH_COL
        elif FOURTHLINE < col <= FIFTHLINE:
            col = FIFTH_COL
        elif FIFTHLINE < col <= SISTHLINE:
            col = SISTH_COL
        elif col > SISTHLINE:
            col = SEVEN_COL
        if not self.game_over:
            # Red turn
            if self.red_turn:
                if self.is_position_blank(col):
                    row = self.next_row(col)
                    self.drop_disk(row, col, 1)
                self.red_turn = False

    def ai(self):
        """
        AI will randomly make a legal move.
        None => None
        """
        top_space = []
        valid_move = False
        # Random choose a row and check if this row still have a blank
        ai_decision = random.randint(0, self.ROW)
        while not valid_move:
            if self.is_position_blank(ai_decision):
                valid_move = True
            else:
                ai_decision = random.randint(0, self.ROW)
        row = self.next_row(ai_decision)
        self.drop_disk(row, ai_decision, 2)
        board = self.board[::-1]
        for i in board:
            if i[ai_decision] == 0:
                top_space.append(i[ai_decision])
        lifespan = len(top_space)
        self.falling_circle.append(YellowDisk(ai_decision * (self.blank_size + self.line_size) +
                                              self.line_size + self.blank_size / 2, self.start_point, lifespan + 1))
        self.red_turn = True
        self.if_red = not self.if_red

    def refresh(self):
        """
        Updates game state on every frame
        None => None
        """
        current_time = time.time()
        AI_THINKING_TIME = 1
        FALLING_SPEED = 20
        self.draw_blank()
        self.check_if_over()
        for i in self.falling_circle:
            i.draw_it()
            if i.y < i.lifespan * (self.blank_size + self.line_size) + self.start_point - self.line_size:
                i.y += FALLING_SPEED
            if i.y >= i.lifespan * (self.blank_size + self.line_size) + self.start_point - self.line_size \
                    and current_time - self.start_time > AI_THINKING_TIME:
                if i.color_id == 1:
                    if not self.red_win:
                        if not self.if_red:
                            self.ai()
        if self.red_win:
            self.game_over = True
            textSize(90)
            fill(255, 0, 30)
            text("RED WINS!", 230, 400)
            if not self.scored:
                if i.y >= i.lifespan * (self.blank_size + self.line_size) + self.start_point - self.line_size \
                        and current_time - self.start_time > AI_THINKING_TIME:
                    score = self.input_score()
                    # If user didn't enter, pass this step
                    if bool(score):
                        self.edit_txt(score)
                    self.scored = True
        elif self.yellow_win:
            if not self.scored:
                self.input_score()
                self.scored = True
            self.game_over = True
            textSize(90)
            fill(255, 255, 0)
            text("YELLOW WINS!", 150, 400)

        if self.game_over and not self.yellow_win and not self.red_win:
            if not self.scored:
                self.input_score()
                self.scored = True
            self.game_over = True
            textSize(90)
            fill(255, 255, 255)
            text("No More Moves", 100, 400)
            text("Game Over", 150, 500)

    def hold_disk(self, x):
        """
        Animate the holding disk.
        Integer => None
        """
        fill(200, 0, 30)
        stroke(1.0, 1.0, 1.0)
        circle(x, 50, self.circle_size)

    def handle_mouse(self):
        """
        Updates game state on every time user click mouse.
        None => None
        """
        self.start_time = time.time()
        if not self.game_over:
            if self.if_red:
                FIRSTLINE = 125
                SECONDLINE = FIRSTLINE + self.blank_size + self.line_size
                THIRDLINE = SECONDLINE + self.blank_size + self.line_size
                FOURTHLINE = THIRDLINE + self.blank_size + self.line_size
                FIFTHLINE = FOURTHLINE + self.blank_size + self.line_size
                SISTHLINE = FIFTHLINE + self.blank_size + self.line_size
                FIRST_COL = 0
                SECOND_COL = 1
                THIRD_COL = 2
                FOURTH_COL = 3
                FIFTH_COL = 4
                SISTH_COL = 5
                SEVEN_COL = 6
                top_space = []
                if mouseX <= FIRSTLINE:
                    col = FIRST_COL
                elif FIRSTLINE < mouseX <= SECONDLINE:
                    col = SECOND_COL
                elif SECONDLINE < mouseX <= THIRDLINE:
                    col = THIRD_COL
                elif THIRDLINE < mouseX <= FOURTHLINE:
                    col = FOURTH_COL
                elif FOURTHLINE < mouseX <= FIFTHLINE:
                    col = FIFTH_COL
                elif FIFTHLINE < mouseX <= SISTHLINE:
                    col = SISTH_COL
                elif mouseX > SISTHLINE:
                    col = SEVEN_COL
                board = self.board[::-1]
                for i in board:
                    if i[col] == 0:
                        top_space.append(i[col])
                lifespan = len(top_space)
                if lifespan != 0:
                    self.falling_circle.append(RedDisk(col * (self.blank_size + self.line_size) +
                                                       self.line_size + self.blank_size / 2, self.start_point,
                                                       lifespan))
                    self.update(mouseX)
                    self.if_red = not self.if_red

    def input_score(message=''):
        """
        Let user input their name
        None => String
        """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, "Enter Your name: ")

    def edit_txt(self, name):
        """
        Update score txt file and rank users from highest score to lowest score.
        String => None
        """
        exist = False
        f = open('scores.txt', 'r')
        lines = f.readlines()
        score_dict = {}
        for i in lines:
            space = i.find(" ")
            if name in i:
                s = int(i[space + 1: -1])
                exist = True
                s += 1
                score_dict[i[0:space]] = int(s)
                continue
            score_dict[i[0:space]] = int(i[space + 1: -1])
        # sort users by their score from high to low
        sorted_list = sorted(score_dict.items(), key=lambda item: item[1], reverse=True)
        score_list = []
        for j in sorted_list:
            score_list.append(j[0] + " " + str(j[1]) + "\n")
        f2 = open('scores.txt', 'w')
        if exist:
            for i in score_list:
                f2.write(i)
        else:
            for i in score_list:
                f2.write(i)
            f2.write(name + " 1" + "\n")
