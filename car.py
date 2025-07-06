import pygame
class Car:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.speed = 1.5


        self.car_image = pygame.image.load(r"C:\Users\sunch\OneDrive\racing_car for python.jpeg")
        self.rect = self.car_image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def position(self):
        self.screen.blit(self.car_image,self.rect)

    def update_ship_position(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.move_left and self.rect.left > 0:
             self.x -= self.speed 

        self.rect.x = self.x