import pygame
import os, time
import numpy as np

from game import Game


# INTERFACE TO PLAY TIC TAC TOE (IN PYGAME):
# The coordinates in pygame start from the left top corner: 
# (x,y) --> 'x' steps right, 'y' steps down  -->  (0,0) is the top left corner.

# PLAYERS:
# -1 (O)
#  1 (X)


class Enviroment:

    def __init__(self):

        # control objects
        self.game = Game()
        self.cursor = Cursor()

        # counters 
        self.win_1 = 0
        self.win_2 = 0
        self.draws = 0
        self.counter = 0

        # pygame variables
        pygame.init()

        self.BOX_SIZE = 150  
        self.width, self.height = 3*self.BOX_SIZE, 3*self.BOX_SIZE

        self.window = pygame.display.set_mode((self.width, self.height)) 
        pygame.display.set_caption("Tres en raya. Autor: Javier Abollado")

        # board boxes
        self.boxes = [[Box(self.BOX_SIZE, i, j, self.window) for j in range(3)] for i in range(3)]

        # chip's images
        names = ["circulo.jpg", "cruz.png"]
        self.images = [load_image(name, (self.BOX_SIZE, self.BOX_SIZE)) for name in names]
        
        # end_game's buttons
        img_button = load_image("button.png", (150,70))
        self.buttons = [Button("Reset", self.reset, img_button, self.width // 4, self.height // 2 , self.window), 
                            Button("Finish", self.finish, img_button, 3* self.width // 4, self.height // 2, self.window)]

        # default values
        self.activate_finished_buttons = False
        self.playing = False

    def finish(self):
        self.playing = False

    def reset(self):
        self.game.reset()
        self.activate_finished_buttons = False
        self.win_player1 = self.win_player2 = False
        self.game.player = -1

    def reset_counters(self):
        self.win_1 = 0
        self.win_2 = 0
        self.draws = 0
        self.counter = 0

    def count_chips(self):
        chips = 0
        for k in range(9):
            if self.game.board[k//3][k%3] == self.game.player: chips += 1
        return chips

    def update(self):
        self.window.fill((255,255,255))
        
        for i in range(3):
            for j in range(3):
                value = self.game.board[i][j]
                image = self.images[(value+1)//2] if value != 0 else None
                self.boxes[j][i].draw(image)                       # TRANSPOSE !! ------------------

        if self.activate_finished_buttons:
            for b in self.buttons:
                b.update()
        
        self.cursor.update()
        pygame.display.update()

    def print_history(self):
        print("\n\n")   
        print("-----------------------------------")
        print("              SUMARY               ")
        print("-----------------------------------")
        print()
        print(f"Total games: {self.win_1+self.win_2+self.draws}\n")
        print("Number of victories for each player:")
        print(f" - Player O: {self.win_1}  ({np.round(100 * self.win_1 / (self.win_1+self.win_2+self.draws), 2)} %)")
        print(f" - Player X: {self.win_2}  ({np.round(100 * self.win_2 / (self.win_1+self.win_2+self.draws), 2)} %)")  
        print(f" - Draws   : {self.draws}  ({np.round(100 * self.draws / (self.win_1+self.win_2+self.draws), 2)} %)")   
        print()

    def close(self):
        pygame.quit()
        self.reset()
        self.reset_counters()

    def play(self, player1, player2):
        self.timer = pygame.time.Clock() 
        self.win_player1, self.win_player2 = False, False
        self.activate_finished_buttons = False
        self.playing = True
        fps = 60

        while self.playing:
            self.timer.tick(fps)

            # player 1
            if self.game.player == -1: 
                self.win_player1 = player1.move()

            # player 2
            else:
                self.win_player2 = player2.move()

            # update
            self.update()

            # check end game
            if not self.activate_finished_buttons and (self.win_player1 or self.win_player2 or self.game.draw()):
                self.counter += 1
                self.activate_finished_buttons = True
                if self.win_player1:
                    self.win_1 += 1
                elif self.win_player2:
                    self.win_2 += 1
                else:
                    self.draws += 1

        self.print_history()

def load_image(name, scale):
    imagen = pygame.image.load(os.path.join("images", name))
    return pygame.transform.scale(imagen, scale)

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite): 
    def __init__(self, text, command, imagen, x, y, window):
        self.window = window
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = (x, y)
        self.rectangle = (self.rect.left, self.rect.top, self.rect.width, self.rect.height)
        self.command = command   
        self.text = pygame.font.SysFont("Arial", 30).render(text, 0, (255,255,255))

    def update(self):
        self.window.blit(self.image, self.rect)
        self.window.blit(self.text, (self.rect.centerx - 30, self.rect.centery - 18))

class Box:
    def __init__(self, size, i, j, window):
        self.size = size
        self.coordinates = (i,j)
        self.rectangle = (i*self.size, j*self.size, size, size)
        self.window = window
    def draw(self, image):
        if image == None:
            return
        self.window.blit(image, (self.rectangle[0], self.rectangle[1]))
