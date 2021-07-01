import pygame
from pygame.locals import *
print(pygame.version.ver)

class Game:
    def __init__(self):
        self.board = Board()
        self.playerone = Player()
        self.playertwo = Player()
        self.turn_count = 0
        self.did_win = False
        self.board_cords = list(range(0,9))
        self.win_condition = [ slice(0,3), slice(3,6), slice(6,9), slice(0,9,3),
                              slice(1,9,3), slice(2,9,3), slice(0,9,4),
                              slice(2,8,2)]

    def turn(self):
        self.turn_count+=1
        if (self.turn_count % 2) == 0:
            return True

    def game_over(self):
        return true
        pass

    def display_text(self):
        self.board.screen.blit(self.board.text, self.board.text_rect)
        pygame.display.update()

    def update_cords(self, box):
        if self.turn():
            icon = 'x'
        else:
            icon = 'o'
        self.board_cords[box] = icon
        self.check_win()
        self.display_text()

    def check_win(self):
        for condition in self.win_condition:
            if len(set(self.board_cords[condition])) == 1:
                print("Winner!")
                win_index = self.win_condition.index(condition)
            elif len(set(self.board_cords[condition])) > 1 and self.turn_count == 9:
                print("There was a tie, try again!")

    def run(self):
        while not self.did_win:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.did_win = True
                if event.type == QUIT:
                    self.did_win = True
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    for item in self.board.boxes:
                        if item.collidepoint(mouse_position):
                            self.playerone.image_o_rect.center = item.center
                            self.board.screen.blit(self.playerone.image_o,
                                                   self.playerone.image_o_rect)
                            self.update_cords(self.board.boxes.index(item))
                            print(self.playerone.image_o_rect.center)
                            pygame.display.flip()


    def draw_win_line(self, condition):
        # Cleanup
        pygame.draw.line(self.surface, self.board.win_color_line,
                            (condition[1][0], condition[1][1]),
                            (condition[2][0], condition[2][1]),
                         self.board.line_width)
        pygame.display.flip()


    def new_win(self):
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


class Board:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        font = pygame.font.SysFont('freesansbold.tff', 30)
        self.text = font.render(message, 1, (255, 255, 255))
        self.text_rect = text.get_rect(center =(width / 2, 500-50))
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

class Player:
    def __init__(self):
        self.image_o = pygame.image.load("image_o_v2.bmp")
        self.image_o_rect = self.image_o.get_rect()
        self.image_x = pygame.image.load("image_x_v2.bmp")
        self.image_x_rect = self.image_x.get_rect()

    def get_name(self):
        self.playerone_name = input("Please enter your name:\n")


if __name__ == '__main__':
    game = Game()
    game.run()
