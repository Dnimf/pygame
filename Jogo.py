import pygame
import pygame.sprite
import random
pygame.init()
pygame.mixer.init()


infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
SLIME_WIDTH = 80
SLIME_HEIGHT = 68

window = pygame.display.set_mode((WIDTH, HEIGHT))
def game_screen(window):
    pygame.display.set_caption("Game")
    assets = {}

    # icon = pygame.image.load('Sprites/Triforce.png')
    # icon = pygame.transform.scale(icon, (32, 32))
    # pygame.display.set_icon(icon)

    #Criando o background
    assets['background'] = pygame.image.load('pygame/Sprites/background.png').convert()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))

    #criando a flecha
    assets['flecha_img_right'] = pygame.image.load('pygame/Sprites/flecha.png').convert_alpha()
    assets['flecha_img_right'] = pygame.transform.scale(assets['flecha_img_right'], (55, 19))
    assets['flecha_img_up'] = pygame.transform.rotate(assets['flecha_img_right'], 90)
    assets['flecha_img_left'] = pygame.transform.rotate(assets['flecha_img_right'], 180)
    assets['flecha_img_down'] = pygame.transform.rotate(assets['flecha_img_right'], 270)
    assets['som_flecha'] = pygame.mixer.Sound('pygame/Sound effects/MC_Arrow_shoot.wav')

    #Criando as animações de tiro
    # Atirando de frente
    tiro_frente = []
    for i in range(1, 5):
        file = f'pygame/Sprites/Atirando frente/atirando_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,115))
        tiro_frente.append(img)
    assets['tiro_frente'] = tiro_frente

    # Atirando de traz
    tiro_traz = []
    for i in range(1, 5):
        file = f'pygame/Sprites/Atirando traz/atirando_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,115))
        tiro_traz.append(img)
    assets['tiro_traz'] = tiro_traz

    # Atirando para a direita
    tiro_direita = []
    for i in range(1, 5):
        file = f'pygame/Sprites/Atirando lado/atirando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(105,101))
        tiro_direita.append(img)
    assets['tiro_direita'] = tiro_direita

    # Atirando para esquerda
    tiro_esquerda = []
    for i in range(1, 5):
        file = f'pygame/Sprites/Atirando lado/atirando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(105,101))
        img = pygame.transform.flip(img, True, False)
        tiro_esquerda.append(img)
    assets['tiro_esquerda'] = tiro_esquerda


    # Criando as animações - Sprites do jogo the legend of zelda: minish cap
    # Movendo de frente
    anim_frente = []
    for i in range(1,12):
        file = f'pygame/Sprites/Frente/link_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_frente.append(img)
    assets['anim_frente'] = anim_frente

    # Movendo de traz
    anim_traz = []
    for i in range(1,12):
        file = f'pygame/Sprites/Traz/link_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_traz.append(img)
    assets['anim_traz'] = anim_traz

    # Movendo para esquerda
    anim_esquerda = []
    for i in range(1,12):
        file = f'pygame/Sprites/Lado/link_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        img = pygame.transform.flip(img, True, False)
        anim_esquerda.append(img)
    assets['anim_esquerda'] = anim_esquerda

    # Movendo para direita
    anim_direita = []
    for i in range(1,12):
        file = f'pygame/Sprites/Lado/link_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_direita.append(img)
    assets['anim_direita'] = anim_direita

    # Desviando para frente
    desv_frente = []
    for i in range(1,9):
        file = f'pygame/Sprites/desviando frente/desviando_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_frente.append(img)
    assets['desv_frente'] = desv_frente

    # Desviando para traz
    desv_traz = []
    for i in range(1,9):
        file = f'pygame/Sprites/desviando traz/desviando_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_traz.append(img)
    assets['desv_traz'] = desv_traz

    # Desviando para a direita
    desv_direita = []
    for i in range(1,9):
        file = f'pygame/Sprites/desviando lado/desviando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_direita.append(img)
    assets['desv_direita'] = desv_direita

    # Desviando para a esquerda
    desv_esquerda = []
    for i in range(1,9):
        file = f'pygame/Sprites/desviando lado/desviando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        img = pygame.transform.flip(img, True, False)
        desv_esquerda.append(img)
    assets['desv_esquerda'] = desv_esquerda

    # Sprite do inimigo
    assets['inimigo'] = pygame.image.load('pygame/Sprites/inimigo.png').convert_alpha()
    assets['inimigo'] = pygame.transform.scale(assets['inimigo'], (SLIME_WIDTH, SLIME_HEIGHT))

    # Fonte
    assets['fonte'] = pygame.font.Font(None, 48)

    # Som do desvio
    assets['som_desv'] = pygame.mixer.Sound('pygame/Sound effects/MC_Link_Roll.wav')

    # Trilha sonora
    pygame.mixer.music.load('pygame/Sound effects/Soundtrack.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    #Criando a classe do player
    class link(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            # caracteristicas do player.
            pygame.sprite.Sprite.__init__(self)

            # Grupos
            self.groups = groups
            self.assets = assets

            # Imagens da animação de andar e variaveis utilizadas para que a animação ocorra
            self.img_frente = assets['anim_frente']
            self.img_traz = assets['anim_traz']
            self.img_esquerda = assets['anim_esquerda']
            self.img_direita = assets['anim_direita']
            self.frame = 0
            self.velocidade_anim = 0.3

            # Imagens e som do personagem atirando com o arco e flecha e variaveis utilizadas na função
            self.tiro_frente = assets['tiro_frente']
            self.tiro_traz = assets['tiro_traz']
            self.tiro_esquerda = assets['tiro_esquerda']
            self.tiro_direita = assets['tiro_direita']
            self.som_tiro = assets['som_flecha']
            self.last_shot = pygame.time.get_ticks()
            self.atirando = False
            self.frame_tiro = 0
            self.velocidade_anim_tiro = 0.17
            self.atirou = False

            # Imagens e som do personagem desviando e variaveis utilizadas na função
            self.desvio_frente = assets['desv_frente']
            self.desvio_traz = assets['desv_traz']
            self.desvio_direita = assets['desv_direita']
            self.desvio_esquerda = assets['desv_esquerda']
            self.som_desv = assets['som_desv']
            self.desviando = False
            self.tempo_desvio = 300
            self.inicio_desvio = 0
            self.velocidade_desvio = 6  
            self.direcao_desvio = None
            self.velocidade_anim_desv = 0.4
            self.frame_desv = 0
            self.anim_desv = None
            self.desv_ticks = 500
            self.last_desv = pygame.time.get_ticks()

            # Caracteristicas iniciais do personagem
            self.image = self.img_frente[0]
            self.image_tiro = self.tiro_traz
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 120
            self.speedx = 0
            self.speedy = 0

            # Variaveis utilizadas nas outras funções
            self.direction = 'down'

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Muda a direção do jogador baseado na direção
            # Define que se o jogador estiver parado, a sprite sera a inicial
            if self.atirando:
                self.frame_tiro += self.velocidade_anim_tiro
                if self.frame_tiro >= len(self.image_tiro):
                    self.frame_tiro = 0
                    self.atirando = False
                    self.shoot()
                if self.direction == 'left':
                    self.image = self.tiro_esquerda[int(self.frame_tiro)]
                elif self.direction == 'right':
                    self.image = self.tiro_direita[int(self.frame_tiro)]
                elif self.direction == 'up':
                    self.image = self.tiro_traz[int(self.frame_tiro)]
                elif self.direction == 'down':
                    self.image = self.tiro_frente[int(self.frame_tiro)]

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

            #definindo o tempo de desvio (Ajuda: Chat GPT)
            if self.desviando:

                now = pygame.time.get_ticks()
                if now - self.inicio_desvio > self.tempo_desvio:
                    self.desviando = False
                    self.direcao_desvio = None
                else:
                    if self.direction == 'left':
                        self.rect.x -= self.velocidade_desvio
                        self.image = self.desvio_esquerda[int(self.frame_desv)]
                    elif self.direction == 'right':
                        self.rect.x += self.velocidade_desvio
                        self.image = self.desvio_direita[int(self.frame_desv)]
                    elif self.direction == 'up':
                        self.rect.y -= self.velocidade_desvio
                        self.image = self.desvio_traz[int(self.frame_desv)]
                    elif self.direction == 'down':
                        self.rect.y += self.velocidade_desvio
                        self.image = self.desvio_frente[int(self.frame_desv)]

                    self.frame_desv += self.velocidade_anim_desv
                    if self.frame_desv >= len(self.desvio_frente):
                        self.frame_desv = 0

        def shoot(self):
            # Verifica se pode atirar
            now = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde o último tiro.

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
            self.som_tiro.play()


            self.frame_tiro += self.velocidade_anim_tiro
            if self.frame_tiro >= len(self.tiro_frente):
                self.frame_tiro = 0
        
        def desvio(self):
            now = pygame.time.get_ticks()
            elapsed_ticks = now - self.last_desv

            if elapsed_ticks > self.desv_ticks:
                self.last_desv = now
                self.desviando = True
                self.inicio_desvio = now
            self.som_desv.play()
                    
    # Criando a classe das flechas
    class flecha(pygame.sprite.Sprite):
        def __init__(self, assets, py, px, direction):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets[f'flecha_img_{direction}']
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
                self.image = assets['flecha_img_left']
            elif self.direction == 'right':
                self.image = assets['flecha_img_right']
            elif self.direction == 'up':
                self.image = assets['flecha_img_up']
            elif self.direction == 'down':
                self.image = assets['flecha_img_down']

            if self.rect.bottom < 85 or self.rect.top > HEIGHT-115 or self.rect.right < 150 or self.rect.left > WIDTH-150:
                self.kill()

    class inimigo(pygame.sprite.Sprite):
        def __init__(self, assets):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets['inimigo']
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, (WIDTH-150)-SLIME_WIDTH)
            self.rect.y = random.randint(0, (HEIGHT-115)-SLIME_HEIGHT)
            self.speedx = -1
            self.speedy = -1
            self.vida = 3
            self.recuando = False
            self.tempo_recuo = 250
            self.inicio_recuo = 0
            self.velocidade_recuo = 6
            self.direction = 'down'
            self.rec_ticks = 500

        def update(self):
            # Define direção do inimigo
            if not self.recuando:
                if self.speedx < 0:
                    self.direction = 'left'
                elif self.speedx > 0:
                    self.direction = 'right'
                elif self.speedy < 0:
                    self.direction = 'up'
                elif self.speedy > 0:
                    self.direction = 'down'

                # Mantem dentro da tela
                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0

                # Faz o inimigo seguir o player
                if self.rect.x - player.rect.x != WIDTH-999:
                    if self.rect.x > player.rect.x:
                        self.rect.x += self.speedx
                    elif self.rect.x < player.rect.x:
                        self.rect.x -= self.speedx
                if self.rect.y - player.rect.y != HEIGHT-699:
                    if self.rect.y > player.rect.y:
                        self.rect.y += self.speedy
                    elif self.rect.y < player.rect.y:
                        self.rect.y -= self.speedy

            # Faz inimigo recuar quando acerta o player
            if self.recuando:
                now = pygame.time.get_ticks()
                if now - self.inicio_recuo > self.tempo_recuo:
                    self.recuando = False
                else:
                    if self.direction == 'left':
                        self.rect.x -= self.velocidade_recuo
                    elif self.direction == 'right':
                        self.rect.x += self.velocidade_recuo
                    elif self.direction == 'up':
                        self.rect.y -= self.velocidade_recuo
                    elif self.direction == 'down':
                        self.rect.y += self.velocidade_recuo

        def recuar(self, player):
            self.recuando = True
            self.inicio_recuo = pygame.time.get_ticks()
            if self.rect.x > player.rect.x:
                self.direction = 'right'
            elif self.rect.x < player.rect.x:
                self.direction = 'left'
            if self.rect.y > player.rect.y:
                self.direction = 'down'
            elif self.rect.y < player.rect.y:
                self.direction = 'up'


    # Criando um grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_flechas = pygame.sprite.Group()
    all_slime=pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_flechas'] = all_flechas
    groups['all_slime'] = all_slime

    # Criando o inimigo
    slime = inimigo(assets)
    all_sprites.add(slime)
    all_slime.add(slime)

    # Criando o jogador
    player = link(groups, assets)
    all_sprites.add(player)

    # Parametros do jogo
    numero_slimes = 1
    vida_inimigo = 3
    j = 0
    vida_player = 3
    pontos = 0

    # Iniciando o loop do jogo
    DONE = 0
    PLAYING = 1
    state = PLAYING
    clock = pygame.time.Clock()
    FPS = 60

    # Define a última vez que o jogador tomou um hit
    last_hit_time = pygame.time.get_ticks()
    hit_cooldown = 1000  # 1 segundo de cooldown entre hits

    while state != DONE:
        clock.tick(FPS)
        window.fill((0, 0, 0))
        window.blit(assets['background'], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE

            # Ações do jogador
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
                elif event.key == pygame.K_SPACE:
                    player.desvio()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.atirando = True

            elif event.type == pygame.KEYUP:
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

        hits = pygame.sprite.groupcollide(all_flechas, all_slime, True, False,pygame.sprite.collide_mask)

        for hit_inimigo in hits:
            vida_inimigo -= 1
            if vida_inimigo == 0:
                pontos += 50
                slime.kill()
                j += 1
                if j == 1:
                    slime = inimigo(assets)
                    all_slime.add(slime)
                    all_sprites.add(slime)
                    vida_inimigo = 6
                if j == 2:
                    slime = inimigo(assets)
                    all_slime.add(slime)
                    all_sprites.add(slime)
                    vida_inimigo = 9
                if j == 3:
                    slime = inimigo(assets)
                    all_slime.add(slime)
                    all_sprites.add(slime)
                    slime1=inimigo(assets)
                    all_slime.add(slime1)
                    all_sprites.add(slime1)
                    vida_inimigo = 6
                # if vida_inimigo==0:
                #     slime1.kill()
                if j==4:
                    vida_inimigo=6
            if vida_inimigo==0:
                slime1.kill()

        hits_player = pygame.sprite.spritecollide(player, all_slime, False, pygame.sprite.collide_mask)
        now = pygame.time.get_ticks()

        if hits_player and now - last_hit_time > hit_cooldown:
            vida_player -= 1
            last_hit_time = now
            for slime in hits_player:
                slime.recuar(player)
            if vida_player == 0:
                player.kill()
                state = DONE

        # Atualizando a tela
        all_sprites.update()
        all_sprites.draw(window)

        text_surface = assets['fonte'].render(f"{pontos:08d}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 10)
        window.blit(text_surface, text_rect)
        
        text_surface = assets['fonte'].render(f"{vida_player:08d}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 4, 10)
        window.blit(text_surface, text_rect)

        text_surface = assets['fonte'].render(f"{vida_inimigo:08d}", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 4, 40)
        window.blit(text_surface, text_rect)    
        pygame.display.update()

    # Finalizando o jogo
    pygame.quit()
