import pygame
import pygame.sprite
import random
pygame.init()
pygame.mixer.init()

# Create window
WIDTH = 1000
HEIGHT = 700
SLIME_WIDTH = 50
SLIME_HEIGHT = 38
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
assets = {}
assets['player_img_up'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\link_traz.png').convert_alpha()
assets['player_img_down'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\link_frente.png').convert_alpha()
assets['player_img_left'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\link_esquerda.png').convert_alpha()
assets['player_img_right'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\link_direita.png').convert_alpha()
assets['player_img_up'] = pygame.transform.scale(assets['player_img_up'], (72, 101))
assets['player_img_down'] = pygame.transform.scale(assets['player_img_down'], (72, 101))
assets['player_img_left'] = pygame.transform.scale(assets['player_img_left'], (72, 101))
assets['player_img_right'] = pygame.transform.scale(assets['player_img_right'], (72, 101))
assets['flecha_img'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\Flecha.png').convert_alpha()
assets['flecha_img'] = pygame.transform.scale(assets['flecha_img'], (49, 13))
assets['slime'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\pixil-frame-0.png').convert_alpha()
assets['slime_img'] = pygame.transform.scale(assets['slime'], (SLIME_WIDTH, SLIME_HEIGHT))
assets['background'] = pygame.image.load(r'C:\Users\Daniel\OneDrive\Documentos\pygame\background.png').convert_alpha()
assets["fonte"]=pygame.font.Font(None, 48)
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
                print("left")
                new_flecha = flecha(self.assets, self.rect.centery, self.rect.left, self.direction)
            elif self.direction == 'right':
                print("right")
                new_flecha = flecha(self.assets, self.rect.centery, self.rect.right, self.direction)
            elif self.direction == 'up':
                print("up")
                new_flecha = flecha(self.assets, self.rect.top, self.rect.centerx, self.direction)
            elif self.direction == 'down':
                print("down")
                new_flecha = flecha(self.assets, self.rect.bottom, self.rect.centerx, self.direction)
            self.groups['all_sprites'].add(new_flecha)
            self.groups['all_flechas'].add(new_flecha)
            self.atirando=True
    # def follow(self):
    #     if link-inimigo>1:
    #         print('aaaa')
# objeto=link(assets, assets)
# objeto.calc()
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

        if self.rect.bottom < 85 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class inimigo(pygame.sprite.Sprite):

    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['slime_img']
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0, WIDTH-SLIME_WIDTH)
        self.rect.y = random.randint(0, HEIGHT-SLIME_HEIGHT)
        self.speedx=-1
        self.speedy = -1
    def update(self):
        # objeto1=link(assets, assets)
        # aa=objeto1
        # Atualização da posição da nave
        # self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    # def distancia(self):
        if self.rect.x-player.rect.x!=WIDTH-999:
            if self.rect.x>player.rect.x:
                self.rect.x += self.speedx
            elif self.rect.x<player.rect.x:
                self.rect.x -=self.speedx
        if self.rect.y-player.rect.y!=HEIGHT-699:
            if self.rect.y>player.rect.y:
                self.rect.y +=self.speedy
            elif self.rect.y<player.rect.y:
                self.rect.y-=self.speedy

# Criando um grupo de flechas
all_sprites = pygame.sprite.Group()
all_flechas = pygame.sprite.Group()
all_slime=pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_flechas'] = all_flechas
groups['all_slime']=all_slime
all_sprites=pygame.sprite.Group()

slime=inimigo(assets)
all_sprites.add(slime)
all_slime.add(slime)
# Criando o jogador
player = link(groups, assets)
all_sprites.add(player)
numero_slimes = 1
vida=3
j=0
lives=3
point=0
running = True
clock = pygame.time.Clock()
FPS = 60
k=0
delay=60
while running:
    clock.tick(FPS)
    # window.fill((0, 0, 0))
    now=pygame.time.get_ticks()
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
        if event.type==pygame.MOUSEBUTTONUP:
            player.atirando=False

    # slime=inimigo(assets['slime_img'])
    # all_slime.add(slime)
    # all_sprites.add(slime)
    # hit1=pygame.sprite.spritecollide(slime, slime, False)
    # hits=pygame.sprite.groupcollide(all_slime, all_slime, False, True)
    # for slime in hits:
    #     slime.rect.x=slime.rect.x
    hits=pygame.sprite.groupcollide(all_flechas, all_slime, True, False)
    # if len(hits)>0:
    
    for slime in hits:
        now=pygame.time.get_ticks()
        # all_slime.add(slime)
        # all_sprites.add(slime)     
        #kill em todos os slimes
        # for sl in all_slime:
        #for slime in hit1:
        # slime.kill()ddddddd
        vida=vida-1
        if vida==0:
            point+=50*len(hits[slime])
            for i in hits[slime]:
                i.kill()
                j+=1
            #slime.kill()
        # if point==50:
                if j==1:
                    sl=inimigo(assets)
                    all_slime.add( sl )
                    all_sprites.add(sl)
                    vida=6
                if j==2:
                    sl=inimigo(assets)
                    all_slime.add(sl)
                    all_sprites.add(sl)
                    vida=9
                if j==3:
                    for i in range(2):
                        sl=inimigo(assets)
                        all_slime.add( sl )
                        all_sprites.add(sl)
                        vida=6                        
    hits=pygame.sprite.spritecollide(player, all_slime, False)
    for slime in hits:
        now1=pygame.time.get_ticks()
        lives-=1
        slime.speedx*=-1
        slime.speedy*=-1
        print(slime.speedx)
        now2=pygame.time.get_ticks()
    # print(now)
    # print(now2)
        if slime.rect.x>player.rect.x+50 and slime.rect.y>player.rect.y+50:
            slime.speedx*=-1
            slime.speedy*=-1
        elif slime.rect.x>player.rect.x-50 and slime.rect.y>player.rect.y-50:
            print(slime.speedx)
            slime.speedx*=-1
            slime.speedy*=-1
        print(len(all_slime))
        # slime=inimigo(assets)
        # all_slime.add(slime)
        # all_sprites.add(slime)
        # slime.rect.x=player.rect.x-50
        # slime.rect.y=player.rect.y-50
        if lives==0:
            player.kill()
            pygame.quit()
        # for slime in hits:
        #     if slime.kill():
        #         k=k+2
        #     while i<=k:

        #         all_slime.add(sl)
        #         all_sprites.add(sl)
        #         i+=1

    all_sprites.update()
    all_flechas.update()
    all_slime.update()
    window.fill((0, 0, 0))
    window.blit(assets['background'], (0, 0))
    all_sprites.draw(window)
    text_surface=assets['fonte'].render("{:08d}".format(point), True, (255, 255, 255))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(WIDTH/2, 10)
    window.blit(text_surface, text_rect)
    
    text_surface=assets['fonte'].render("{:08d}".format(lives), True, (255, 255, 255))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(WIDTH/4, 10)
    window.blit(text_surface, text_rect) 

    text_surface=assets['fonte'].render("{:08d}".format(vida), True, (255, 255, 255))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(WIDTH/4, 50)
    window.blit(text_surface, text_rect)  
    pygame.display.update()


pygame.quit()
