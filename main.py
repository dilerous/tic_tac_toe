import pygame
from pygame.locals import *
print(pygame.version.ver)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.board = Board()
        self.board_cords = list(range(0,9))
        self.turn_count = 0
        self.did_win = False
        self.surface = pygame.display.set_mode((self.board.width,
                                                self.board.height))
        self.surface.fill((0, 0, 0))
        self.x_image = Ximage(self.surface)
        self.o_image = Oimage(self.surface)
        self.board.draw(self.surface, self.board)

    def turn(self):
        self.turn_count+=1
        if (self.turn_count % 2) == 0:
            return True

    def draw_win_line(self, condition):
        pygame.draw.line(self.surface, self.board.win_color_line,
                            (condition[1][0], condition[1][1]),
                            (condition[2][0], condition[2][1]),
                         self.board.line_width)
        pygame.display.flip()

    def new_win(self):
        self.win_condition = [ slice(0,3), slice(3,6), slice(6,9), slice(0,9,3),
                              slice(1,9,3), slice(2,9,3), slice(0,9,4),
                              slice(2,8,2)]
        self.x_cords = [ (10, self.board.height//5), (10, self.board.height//2),
                        (10, self.board.height//1.25), (self.board.height//5, 10),
                        (self.board.height//2, 10), (self.board.height//1.25, 10),
                        (10, 10),(10, self.board.height-10) ]
        self.y_cords = [ (self.board.width-10, self.board.width//5),
                        (self.board.height-10, self.board.width//2),
                        (self.board.height-10, self.board.width//1.25),
                        (self.board.width//5, self.board.height-10),
                        (self.board.width//2, self.board.height-10),
                        (self.board.width//1.25, self.board.height-10),
                        (self.board.width-10, self.board.height-10),
                        (self.board.width, 10) ]
        self.win_with_cords = list(zip(self.win_condition,
                                       self.x_cords, self.y_cords))

        for condition in self.win_condition:
            if len(set(self.board_cords[condition])) == 1:
                print("Winner!")
                win_index = self.win_condition.index(condition)
                self.draw_win_line(self.win_with_cords[win_index])
            elif len(set(self.board_cords[condition])) > 1 and self.turn_count == 9:
                print("There was a tie, try again!")

    def run(self):
        while not self.did_win:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.did_win = True
                elif event.type == QUIT:
                    self.did_win = True
                elif ( event.type == pygame.MOUSEBUTTONUP ):
                    mouse_position = pygame.mouse.get_pos()
                    if ( self.board.click_middle.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 3, 3)
                            self.board_cords[4] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 3, 3)
                            self.board_cords[4] = 'x'
                            self.new_win()

                    if ( self.board.click_top_left.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 40, 40)
                            self.board_cords[0] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 40, 40)
                            self.board_cords[0] = 'x'
                            self.new_win()

                    if ( self.board.click_bottom_right.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 1.5, 1.5)
                            self.board_cords[8] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 1.5, 1.5)
                            self.board_cords[8] = 'x'
                            self.new_win()

                    if ( self.board.click_bottom_left.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 40, 1.5)
                            self.board_cords[6] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 40, 1.5)
                            self.board_cords[6] = 'x'
                            self.new_win()

                    if ( self.board.click_top_right.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 1.5, 40)
                            self.board_cords[2] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 1.5, 40)
                            self.board_cords[2] = 'x'
                            self.new_win()

                    if ( self.board.click_middle_right.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 1.5, 3)
                            self.board_cords[5] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 1.5, 3)
                            self.board_cords[5] = 'x'
                            self.new_win()

                    if ( self.board.click_middle_left.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 40, 3)
                            self.board_cords[3] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 40, 3)
                            self.board_cords[3] = 'x'
                            self.new_win()

                    if ( self.board.click_bottom_middle.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 3, 1.5)
                            self.board_cords[7] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 3, 1.5)
                            self.board_cords[7] = 'x'
                            self.new_win()

                    if ( self.board.click_top_middle.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                        if self.turn():
                            self.o_image.draw(self.board, 3, 40)
                            self.board_cords[1] = 'o'
                            self.new_win()
                        else:
                            self.x_image.draw(self.board, 3, 40)
                            self.board_cords[1] = 'x'
                            self.new_win()


class Board:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.line_width = 4
        self.color_line = (255, 255, 0)
        self.win_color_line = (0, 128, 0)
        self.click_middle  = pygame.Rect( self.width//3, self.height//3,
                                         self.width//3, self.height//3 )
        self.click_top_left  = pygame.Rect( self.width//40, self.height//40,
                                           self.width//3, self.height//3 )
        self.click_bottom_right  = pygame.Rect( self.width//1.5,
                                               self.height//1.5, self.width//3,
                                               self.height//3 )
        self.click_bottom_left  = pygame.Rect( self.width//40, self.height//1.5,
                                              self.width//3, self.height//3 )
        self.click_top_right  = pygame.Rect( self.width//1.5, self.height//40,
                                            self.width//3, self.height//3 )
        self.click_middle_right  = pygame.Rect( self.width//1.5, self.height//3,
                                               self.width//3, self.height//3 )
        self.click_middle_left  = pygame.Rect( self.width//40, self.height//3,
                                              self.width//3, self.height//3 )
        self.click_bottom_middle  = pygame.Rect( self.width//3, self.height//1.5,
                                                self.width//3, self.height//3 )
        self.click_top_middle  = pygame.Rect( self.width//3, self.height//40,
                                             self.width//3, self.height//3 )

    def draw(self, parent_surface, board):
        self.surface = parent_surface
        pygame.draw.line(self.surface, self.color_line, (0+10, self.height * .33),
                         (self.width - 10, self.height * .33),
                         self.line_width)
        pygame.draw.line(self.surface, self.color_line, (0+10, self.height * .66),
                         (self.width - 10, self.height * .66),
                         self.line_width)
        pygame.draw.line(self.surface, self.color_line, (self.width * .33, 0+10),
                         (self.width * .33, self.height - 10),
                         self.line_width)
        pygame.draw.line(self.surface, self.color_line, (self.width * .66, 0+10),
                         (self.width * .66, self.height - 10),
                         self.line_width)
        pygame.display.flip()


class Ximage:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("image_x_v2.bmp")
        self.image_size = 60

    def draw(self, board, x, y):
        self.board = board
        self.x = (self.board.width//x) + self.image_size
        self.y = (self.board.height//y) + self.image_size
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Oimage:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("image_o_v2.bmp")
        self.image_size = 60

    def draw(self, board, x, y):
        self.board = board
        self.x = (self.board.width//x) + self.image_size
        self.y = (self.board.height//y) + self.image_size
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
