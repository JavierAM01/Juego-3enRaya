import pygame


class Player:

    def __init__(self, game):
        self.game = game
        self.playing = True
    
    def move(self):
        self.playing = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.playing = False
    
    def reset(self):
        pass


class Human(Player): # 3 moves

    def __init__(self, game, enviroment):
        super().__init__(game)
        self.enviroment = enviroment
    
    def move(self):
        self.playing = True
        finished = False
        for event in pygame.event.get():
          if event.type == pygame.QUIT: 
            self.playing = False

          if event.type == pygame.MOUSEBUTTONDOWN: 
                        
            # finished buttons
            if self.enviroment.activate_finished_buttons:
              for b in self.enviroment.buttons:
                if self.enviroment.cursor.colliderect(b.rectangle):
                  b.command()
              break
                    
            # play human
            if self.game.count_chips() < 3:
              for i in range(3):
                for j in range(3):
                  box = self.enviroment.boxes[j][i]          # TRANSPOSE !! ------------------
                  if self.enviroment.cursor.colliderect(box.rectangle) and self.game.board[i][j] == 0:
                    action = 3*i+j
                    finished = self.game.make_move(action)
            else:
              for i in range(3):
                for j in range(3):
                  box = self.enviroment.boxes[j][i]          # TRANSPOSE !! ------------------
                  if self.enviroment.cursor.colliderect(box.rectangle) and self.game.board[i][j] == self.game.player:
                    action = 3*i+j
                    finished = self.game.make_move(action, erase=True)

        return finished
    


class Human(Player): # full

    def __init__(self, game, enviroment):
        super().__init__(game)
        self.enviroment = enviroment
    
    def move(self):
        self.playing = True
        finished = False
        for event in pygame.event.get():
          if event.type == pygame.QUIT: 
            self.playing = False

          if event.type == pygame.MOUSEBUTTONDOWN: 
                        
            # finished buttons
            if self.enviroment.activate_finished_buttons:
              for b in self.enviroment.buttons:
                if self.enviroment.cursor.colliderect(b.rectangle):
                  b.command()
              break
                    
            # play human
            for i in range(3):
              for j in range(3):
                box = self.enviroment.boxes[j][i]          # TRANSPOSE !! ------------------
                if self.enviroment.cursor.colliderect(box.rectangle) and self.game.board[i][j] == 0:
                  action = 3*i+j
                  finished = self.game.make_move(action)

        return finished
