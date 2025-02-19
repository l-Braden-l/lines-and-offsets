# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   running = True
   while running:
      running = handle_events()
      screen.fill(config.GREEN) # Use color from config
      
      thickness = 2

      #-- For --#
      for y_offset in range(1,800,4):
         pygame.draw.line(screen,config.RED,[0, 0 + y_offset],[800, 5 + y_offset],thickness)

     
      #-- While --#
      y_offset = 0 
      while y_offset < 800:
         pygame.draw.line(screen,config.BLUE,[1, 0 + y_offset],[799, 6 + y_offset],thickness)
         y_offset = y_offset + 3

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate
      pygame.display.flip()

     

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()