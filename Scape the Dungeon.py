import pygame
import pygame.sprite

pygame.init()
pygame.mixer.init()

# Create window
WIDTH = 1000
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
assets = {}
assets['player_img_up'] = pygame.image.load('link_traz.png').convert_alpha()
assets['player_img_down'] = pygame.image.load('link_frente.png').convert_alpha()
assets['player_img_left'] = pygame.image.load('link_esquerda.png').convert_alpha()
assets['player_img_right'] = pygame.image.load('link_direita.png').convert_alpha()
assets['player_img_up'] = pygame.transform.scale(assets['player_img_up'], (72, 101))
assets['player_img_down'] = pygame.transform.scale(assets['player_img_down'], (72, 101))
assets['player_img_left'] = pygame.transform.scale(assets['player_img_left'], (72, 101))
assets['player_img_right'] = pygame.transform.scale(assets['player_img_right'], (72, 101))
assets['flecha_img'] = pygame.image.load('Flecha.png').convert_alpha()
assets['flecha_img'] = pygame.transform.scale(assets['flecha_img'], (49, 13))

#Criando a classe do player
class link(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player_img_down']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
        self.direction = 'down'


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Update player image based on direction
        if self.speedx < 0:
            self.image = self.assets['player_img_left']
            self.direction = 'left'
        elif self.speedx > 0:
            self.image = self.assets['player_img_right']
            self.direction = 'right'
        elif self.speedy < 0:
            self.image = self.assets['player_img_up']
            self.direction = 'up'
        elif self.speedy > 0:
            self.image = self.assets['player_img_down']
            self.direction = 'down'

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova flecha vai ser criada no centro horizontal do personagem
            # Linha 81 a 88: fonte - GPT
            if self.direction == 'left':
                new_flecha = flecha(self.assets, self.rect.centery, self.rect.left, self.direction)
            elif self.direction == 'right':
                new_flecha = flecha(self.assets, self.rect.centery, self.rect.right, self.direction)
            elif self.direction == 'up':
                new_flecha = flecha(self.assets, self.rect.top, self.rect.centerx, self.direction)
            elif self.direction == 'down':
                new_flecha = flecha(self.assets, self.rect.bottom, self.rect.centerx, self.direction)
            self.groups['all_sprites'].add(new_flecha)
            self.groups['all_flechas'].add(new_flecha)


# Criando a classe das flechas
class flecha(pygame.sprite.Sprite):
    def __init__(self, assets, py, px, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['flecha_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = px
        self.rect.y = py
        self.direction = direction
        self.speedy = 0  # Velocidade vertical fixa
        self.speedx = 0    # Velocidade horizontal inicialmente nula
        if self.direction == 'left':
            self.speedx = -10
        elif self.direction == 'right':
            self.speedx = 10
        elif self.direction == 'up':
            self.speedy = -10
        elif self.direction == 'down':
            self.speedy = 10

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.direction == 'left':
            self.image = assets['flecha_img']
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(assets['flecha_img'], 180)
        elif self.direction == 'up':
            self.image = pygame.transform.rotate(assets['flecha_img'], 270)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(assets['flecha_img'], 90)

        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

# Criando um grupo de flechas
all_sprites = pygame.sprite.Group()
all_flechas = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_flechas'] = all_flechas

# Criando o jogador
player = link(groups, assets)
all_sprites.add(player)

running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.speedx = -5
                player.speedy = 0
            elif event.key == pygame.K_d:
                player.speedx = 5
                player.speedy = 0
            elif event.key == pygame.K_w:
                player.speedy = -5
                player.speedx = 0
            elif event.key == pygame.K_s:
                player.speedy = 5
                player.speedx = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a and player.speedx < 0:
            player.speedx = 0
        elif event.key == pygame.K_d and player.speedx > 0:
            player.speedx = 0
        elif event.key == pygame.K_w and player.speedy < 0:
            player.speedy = 0
        elif event.key == pygame.K_s and player.speedy > 0:
            player.speedy = 0


    
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
