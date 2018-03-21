import pygame

pygame.init()

# setting up the game window size
gameDisplay = pygame.display.set_mode((800,600))
#setting up the caption of the window
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

# initially we are not crashed
crashed = False

while not crashed:
    #this creates a list of events per frame 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()
    # this takes frames per second as input
    clock.tick(60)

#pygame quits 
pygame.quit()
quit()
    
          