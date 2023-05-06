from dice_class import Dice, BLACK, win
import pygame 

pygame.init()

clock = pygame.time.Clock()
FPS = 60

def main():
    run = True

    d1, d2, d3, d4, d5, d6 = Dice(1), Dice(2), Dice(3), Dice(4), Dice(5), Dice(6)

    while run:
        clock.tick(FPS)
        win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        # d2.draw_dice()
        d4.draw_dice()
        
        pygame.display.update()
    

if __name__ == '__main__':
    main()