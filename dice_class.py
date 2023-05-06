import pygame 
from utils import generate_circle_points
pygame.init()

width, height = 500, 500
win = pygame.display.set_mode((width, height))

# colors 
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# misc
starting_point_value = 0

class Dice:
    def __init__(self, dice_number):
        self.dice_number = dice_number
        self.x , self.y =  150, 100
        self.width, self.height = 200, 160
        self.circle_x, self.circle_y = 150, 150
        
        self.x_offset, self.y_offset = 50, 50

    def draw_dice(self):
        pygame.draw.rect(win, GREEN, (self.x, self.y, self.width, self.height),border_radius=30)

        if self.dice_number == 1:
            pygame.draw.circle(win, WHITE, (self.x + self.x_offset, self.y + self.y_offset), 15)

        if self.dice_number == 2:
            points = generate_circle_points(starting_point_value, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)                               

        if self.dice_number == 3:
            points = generate_circle_points(starting_point_value, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)

        if self.dice_number == 4:
            points = generate_circle_points(starting_point_value, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)

        if self.dice_number == 5:
            points = generate_circle_points(starting_point_value, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)

        if self.dice_number == 6:
            points = generate_circle_points(starting_point_value, self.dice_number)
            for i in range(self.dice_number):
                pygame.draw.circle(win, WHITE, (self.circle_x + points[i], self.circle_y), 15)


def main():
    d = Dice(2)
    d.draw_dice()
    
if __name__ == '__main__':
    main()
    

        



        