import pygame


class Player:
    def __init__(self, enviroment):
        self.game = enviroment.game
        self.enviroment = enviroment
        self.playing = True


class Player_3moves(Player):

    def __init__(self, enviroment):
        super().__init__(enviroment)
    
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
                    
            # play
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
    


class Player_FullBaoard(Player): 

    def __init__(self, enviroment):
        super().__init__(enviroment)
    
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
