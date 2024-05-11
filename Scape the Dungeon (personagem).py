import pygame
import pygame.sprite

pygame.init()
pygame.mixer.init()


infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game")
assets = {}

#Criando o background
assets['background'] = pygame.image.load('background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))

#criando a flecha
assets['flecha_img'] = pygame.image.load('flecha.png').convert_alpha()
assets['flecha_img'] = pygame.transform.scale(assets['flecha_img'], (55, 19))
assets['som_flecha'] = pygame.mixer.Sound('MC_Arrow_shoot.wav')

#Criando os srpites de tiro
assets['tiro_frente'] = pygame.image.load('Link_atirando_frente.png').convert_alpha()
assets['tiro_frente'] = pygame.transform.scale(assets['tiro_frente'], (72, 101))

assets['tiro_direita'] = pygame.image.load('Link_atirando_lado.png').convert_alpha()
assets['tiro_direita'] = pygame.transform.scale(assets['tiro_direita'], (72, 101))

assets['tiro_esquerda'] = pygame.transform.flip(assets['tiro_direita'], True, False)

assets['tiro_traz'] = pygame.image.load('Link_atirando_traz.png').convert_alpha()
assets['tiro_traz'] = pygame.transform.scale(assets['tiro_traz'], (72, 101))



# Criando as animações - Sprites do jogo the legend of zelda: minish cap
# Movendo para frente
anim_frente = []
for i in range(1,12):
    file = f'Frente/link_frente{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    anim_frente.append(img)
assets['anim_frente'] = anim_frente

# Movendo para traz
anim_traz = []
for i in range(1,12):
    file = f'Traz/link_traz{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    anim_traz.append(img)
assets['anim_traz'] = anim_traz

# Movendo para esquerda
anim_esquerda = []
for i in range(1,12):
    file = f'Lado/link_lado{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    img = pygame.transform.flip(img, True, False)
    anim_esquerda.append(img)
assets['anim_esquerda'] = anim_esquerda

# Movendo para direita
anim_direita = []
for i in range(1,12):
    file = f'Lado/link_lado{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    anim_direita.append(img)
assets['anim_direita'] = anim_direita

# Desviando para frente
desv_frente = []
for i in range(1,9):
    file = f'desviando frente/desviando_frente{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    desv_frente.append(img)
assets['desv_frente'] = desv_frente

# Desviando para traz
desv_traz = []
for i in range(1,9):
    file = f'desviando traz/desviando_traz{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    desv_traz.append(img)
assets['desv_traz'] = desv_traz

# Desviando para a direita
desv_direita = []
for i in range(1,9):
    file = f'desviando lado/desviando_lado{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    desv_direita.append(img)
assets['desv_direita'] = desv_direita

# Desviando para a esquerda
desv_esquerda = []
for i in range(1,9):
    file = f'desviando lado/desviando_lado{i}.png'
    img = pygame.image.load(file).convert_alpha()
    img = pygame.transform.scale(img,(72,101))
    img = pygame.transform.flip(img, True, False)
    desv_esquerda.append(img)
assets['desv_esquerda'] = desv_esquerda

#Criando a classe do player
class link(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # caracteristicas do player.
        pygame.sprite.Sprite.__init__(self)

        self.groups = groups
        self.assets = assets
        self.img_frente = assets['anim_frente']
        self.img_traz = assets['anim_traz']
        self.img_esquerda = assets['anim_esquerda']
        self.img_direita = assets['anim_direita']
        self.tiro_frente = assets['tiro_frente']
        self.tiro_traz = assets['tiro_traz']
        self.tiro_esquerda = assets['tiro_esquerda']
        self.tiro_direita = assets['tiro_direita']
        self.desvio_frente = assets['desv_frente']
        self.desvio_traz = assets['desv_traz']
        self.desvio_direita = assets['desv_direita']
        self.desvio_esquerda = assets['desv_esquerda']
        self.image = self.img_frente[0]
        self.image_tiro = self.tiro_traz
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 120
        self.speedx = 0
        self.speedy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 700
        self.direction = 'down'
        self.frame = 0
        self.velocidade_anim = 0.2
        self.atirando = False
        self.som_tiro = assets['som_flecha']
        self.desviando = False
        self.tempo_desvio = 300
        self.inicio_desvio = 0
        self.velocidade_desvio = 4  
        self.direcao_desvio = None
        self.velocidade_anim_desv = 1
        self.frame_desv = 0
        self.anim_desv = None

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Muda a direção do jogador baseado na direção
        # Define que se o jogador estiver parado, a sprite sera a inicial
        if self.atirando:
            self.image = self.image_tiro
        else:
            if self.speedx == 0 and self.speedy == 0:
                if self.direction == 'left':
                    self.image = self.img_esquerda[0]
                elif self.direction == 'right':
                    self.image = self.img_direita[0]
                elif self.direction == 'up':
                    self.image = self.img_traz[0]
                elif self.direction == 'down':
                    self.image = self.img_frente[0]

            # Define que se o jogador estiver se movimentando o sprite sera animado
            else:
                if self.speedx < 0:
                    self.image = self.img_esquerda[int(self.frame)]
                    self.direction = 'left'
                elif self.speedx > 0:
                    self.image = self.img_direita[int(self.frame)]
                    self.direction = 'right'
                elif self.speedy < 0:
                    self.image = self.img_traz[int(self.frame)]
                    self.direction = 'up'
                elif self.speedy > 0:
                    self.image = self.img_frente[int(self.frame)]
                    self.direction = 'down'
            
            self.frame += self.velocidade_anim
            if self.frame >= len(self.img_frente):
                self.frame = 0

        if self.rect.right > WIDTH-150:
            self.rect.right = WIDTH-150
        if self.rect.left < 150:
            self.rect.left = 150
        if self.rect.top < 85:
            self.rect.top = 85
        if self.rect.bottom > HEIGHT-115:
            self.rect.bottom = HEIGHT-115

        #definindo o tempo de desvio (Fonte: Chat GPT)
        if self.desviando:

            now = pygame.time.get_ticks()
            if now - self.inicio_desvio > self.tempo_desvio:
                self.desviando = False
                self.direcao_desvio = None
            else:
                if self.direcao_desvio == 'left':
                    self.rect.x -= self.velocidade_desvio
                    self.image = self.desvio_esquerda[int(self.frame_desv)]
                elif self.direcao_desvio == 'right':
                    self.rect.x += self.velocidade_desvio
                    self.image = self.desvio_direita[int(self.frame_desv)]
                elif self.direcao_desvio == 'up':
                    self.rect.y -= self.velocidade_desvio
                    self.image = self.desvio_traz[int(self.frame_desv)]
                elif self.direcao_desvio == 'down':
                    self.rect.y += self.velocidade_desvio
                    self.image = self.desvio_frente[int(self.frame_desv)]

                self.frame_desv += self.velocidade_anim
                if self.frame_desv >= len(self.desvio_frente):
                    self.frame_desv = 0

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
                self.image_tiro = self.tiro_esquerda
            elif self.direction == 'right':
                new_flecha = flecha(self.assets, self.rect.centery, self.rect.right, self.direction)
                self.image_tiro = self.tiro_direita
            elif self.direction == 'up':
                new_flecha = flecha(self.assets, self.rect.top, self.rect.centerx, self.direction)
                self.image_tiro = self.tiro_traz
            elif self.direction == 'down':
                new_flecha = flecha(self.assets, self.rect.bottom, self.rect.centerx, self.direction)
                self.image_tiro = self.tiro_frente
            self.image = self.image_tiro
            self.groups['all_sprites'].add(new_flecha)
            self.groups['all_flechas'].add(new_flecha)
            self.som_tiro.play()
            self.atirando = True
    
    def desvio(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now
            self.desviando = True
            self.inicio_desvio = now
            self.direcao_desvio = self.direction
                
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
            self.image = pygame.transform.rotate(assets['flecha_img'], 180)
        elif self.direction == 'right':
            self.image = assets['flecha_img']
        elif self.direction == 'up':
            self.image = pygame.transform.rotate(assets['flecha_img'], 90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(assets['flecha_img'], 270)

        if self.rect.bottom < 85 or self.rect.top > HEIGHT-115 or self.rect.right < 150 or self.rect.left > WIDTH-150:
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
    window.blit(assets['background'], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.speedx = -3
                player.speedy = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.speedx = 3
                player.speedy = 0
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.speedy = -3
                player.speedx = 0
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.speedy = 3
                player.speedx = 0
            if event.key == pygame.K_SPACE:
                player.desvio()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            player.speedx = 0
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            player.speedx = 0
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            player.speedy = 0
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            player.speedy = 0
        if event.key == pygame.K_SPACE:
            player.desviando = False
    if event.type == pygame.MOUSEBUTTONUP:
        player.atirando = False


    
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
