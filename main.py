import pygame
from pygame.locals import *
print(pygame.version.ver)

class Game:
    def __init__(self):
        self.board = Board()
        self.playerone = Playerone()
        self.playertwo = Playertwo()
        self.oimage = Oimage()
        self.turn_count = 0
        self.did_win = False

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

                # Craigs example of the for loop
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    for item in self.board.boxes:
                        if item.collidepoint(mouse_position):
                            self.oimage.image_o_rect.center = item.center
                            self.board.screen.blit(self.oimage.image_o,
                                                   self.oimage.image_o_rect)
                            pygame.display.flip()


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.board_cords = list(range(0,9))
        # Craigs code example
        self.screen = pygame.display.set_mode((640, 480))
        clock = pygame.time.Clock()
        BG_COLOR = pygame.Color('gray12')
        self.screen.fill(BG_COLOR)
        self.boxes = []
        points = []
        buffer_px = 10
        third_width = (640-(buffer_px*2))//3
        third_height = (480-(buffer_px*2))//3
        box_size = third_width, third_height
        width_points = [buffer_px, third_width+buffer_px, (third_width*2)+buffer_px]
        height_points = [buffer_px, third_height+buffer_px, (third_height*2)+buffer_px]
        for hp in height_points:
            for wp in width_points:
                points.append((wp, hp))

        for point in points:
            box = pygame.Rect(point, box_size)
            self.boxes.append(box)
            pygame.draw.rect(self.screen, (0, 100, 255), box, 2)
        pygame.display.flip()

        # Original Code below
        use_old = False
        if use_old:
            self.width = 500
            self.height = 500
            self.surface = pygame.display.set_mode((self.width, self.height))
            self.line_width = 4
            self.surface.fill((0, 0, 0))
            self.color_line = (255, 255, 0)
            self.win_color_line = (0, 128, 0)
            self.x_image = Ximage(self.surface)
            self.o_image = Oimage(self.surface)
            self.draw(self.surface)

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

    def draw(self, parent_surface):

        pygame.display.flip()
        # My old draw board code
        use_old = False
        if use_old:
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

class Playerone:
    def __init__(self):
        self.playerone_image = pygame.image.load("image_x_v2.bmp")
        self.playerone_rect = self.playerone_image.get_rect()

    def draw(self):
        pass



class Playertwo:
    def __init__(self):
        self.playertwo_image = pygame.image.load("image_o_v2.bmp")
        self.playertwo_rect = self.playertwo_image.get_rect()

    def draw(self):
        pass

class Ximage:
    def __init__(self):
        self.image = pygame.image.load("image_x_v2.bmp")

class Oimage:
    def __init__(self):
        self.image_o = pygame.image.load("image_o_v2.bmp")
        self.image_o_rect = self.image_o.get_rect()


if __name__ == '__main__':
    game = Game()
    game.run()
