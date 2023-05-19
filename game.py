

class Game:

    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.depth = 0
        self.player = -1
        self.last_action = -1
        self.last_erase = -1

    def reset(self):
        self.__init__()

    def available_moves(self, board=None, erase=False):
        state = self.board if board == None else board
        if erase:
            return [n for n in range(9) if state[n//3][n%3] == self.player]
        else:
            return [n for n in range(9) if state[n//3][n%3] == 0]

    def is_possible_to_move(self):
        return False if len(self.available_moves()) == 0 else True

    def make_move(self, a, erase=False):
        if erase:
            self.last_erase = a
            self.board[a//3][a%3] = 0
            return False
        self.last_action = a
        self.board[a//3][a%3] = self.player
        self.change_player()
        self.depth += 1
        return self.game_over()

    def count_chips(self):
        chips = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.player:
                    chips += 1
        return chips

    def change_player(self):
        self.player = -1 if self.player == 1 else 1

    def get_state(self, board=None):
        turn = (self.player + 1) // 2
        state = self.board if board == None else board
        b1 = [[int(state[i][j] == -1) for j in range(3)] for i in range(3)]
        b2 = [[int(state[i][j] ==  1) for j in range(3)] for i in range(3)]
        b3 = [[turn for _ in range(3)] for _ in range(3)]
        final_state = [b1, b2, b3]
        return final_state

    def get_state2(self, board=None):
        turn = (self.player + 1) // 2
        erase = 1 if self.count_chips() == 3 else 0
        state = self.board if board == None else board
        b1 = [[int(state[i][j] == -1) for j in range(3)] for i in range(3)]
        b2 = [[int(state[i][j] ==  1) for j in range(3)] for i in range(3)]
        b3 = [[turn for _ in range(3)] for _ in range(3)]
        b4 = [[erase for _ in range(3)] for _ in range(3)]
        final_state = [b1, b2, b3, b4]
        return final_state

    def get_state_supervised(self, board=None):
        turn = (self.player + 1) // 2
        state = self.board if board == None else board
        t = [[turn for _ in range(3)] for _ in range(3)]
        final_state = [state, t]
        return final_state

    def draw(self, board=None):
        state = self.board if board == None else board
        for n in range(9):
            if state[n//3][n%3] == 0:
                return False
        return True

    def game_over(self, board=None):
        state = self.board if board == None else board
        # rows
        for i in range(3):
            total = sum(state[i])
            if abs(total) == 3:
                return True
        # columns
        for j in range(3):
            total = sum([state[i][j] for i in range(3)])
            if abs(total) == 3:
                return True
        # diagonals
        d1 = state[0][0] + state[1][1] + state[2][2]
        d2 = state[0][2] + state[1][1] + state[2][0]
        if abs(d1) == 3 or abs(d2) == 3:
            return True
        # else
        return False

    # opción de hacer un print por pantalla del juego - para pruebas
    def print_board(self):
        print("               ")
        for i in range(3):
            x1 = " " if self.board[i][0] == 0 else ("X" if self.board[i][0] == -1 else "O")
            x2 = " " if self.board[i][1] == 0 else ("X" if self.board[i][1] == -1 else "O")
            x3 = " " if self.board[i][2] == 0 else ("X" if self.board[i][2] == -1 else "O")
            print(" ", x1, " | ", x2, " | ", x3)
            if i != 2:
                print(" --------------")
        print("               ")

