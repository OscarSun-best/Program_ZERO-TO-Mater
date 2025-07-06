import pygame
import sys
from car import Car
class racing_car:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Raqce.ding")
        self.bg_color = (20,20,20)
        self.car = Car(self)
        self.q = 0

    def run_game(self):
        while True:
            self.check_event()
            self.update_screen()
            self.car.update_ship_position()

    def check_event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                        self.check_Key_pres(event)
                elif event.type == pygame.KEYUP:
                        self.check_Key_Up(event)
                        
    def check_Key_pres(self,event):
        if event.key == pygame.K_RIGHT :
            self.car.move_right = True 
        if event.key == pygame.K_LEFT:
            self.car.move_left = True 
        elif event.key == pygame.K_q:
            self.q += 1
        if self.q ==2:
            sys.exit()

    def check_Key_Up(self,event):
         if event.key == pygame.K_RIGHT:
              self.car.move_right = False
         elif event.key == pygame.K_LEFT:
              self.car.move_left = Falseq
              
              
    def update_screen(self):
            self.screen.fill(self.bg_color)
            self.car.position()
            pygame.display.flip()

    

pygame.quit()
if __name__ == "__main__":
    ai = racing_car()
    ai.run_game()
            