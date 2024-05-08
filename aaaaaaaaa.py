print("tenho f")
print("obrigado")
import pygame
import random

pygame.init()
background=(0,0,225)
# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load(r'C:\Users\Daniel\referencia\assets\img\starfield.png').convert()
slime = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\pixil-frame-0.png').convert_alpha()
meteor_img = pygame.transform.scale(slime, (METEOR_WIDTH, METEOR_HEIGHT))
class inimigo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 20
        self.speedx=-1
        self.speedy = -1
    def update(self):
        # Atualização da posição da nave
        # self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    # def distancia(self):
        if self.rect.x>WIDTH/8:
            self.rect.x += self.speedx
        if self.rect.y>HEIGHT-120:
            self.rect.y +=self.speedy
game=True
all_sprites=pygame.sprite.Group()
slime=inimigo(meteor_img)
all_sprites.add(slime)

clock = pygame.time.Clock()
FPS = 30
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
                game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit() 

