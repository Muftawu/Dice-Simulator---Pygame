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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        # check for key presses 
        key_pressed = pygame.key.get_pressed()
        numbers = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6]
        dices = [d1, d2, d3, d4, d5, d6]

        for i in range(len(numbers)):
            if key_pressed[numbers[i]]:
                win.fill(BLACK)
                print(f"Dice {dices[i].dice_number}")
                dices[i].draw_dice()
                
        pygame.display.update()
    

if __name__ == '__main__':
    main()