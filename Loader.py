import pygame

def loader(WIDTH, HEIGHT, SLIME_WIDTH, SLIME_HEIGHT):

    assets = {}
    #Criando o background
    assets['background'] = pygame.image.load('Sprites/background.png').convert()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))

    #criando a flecha
    assets['flecha_img_right'] = pygame.image.load('Sprites/flecha.png').convert_alpha()
    assets['flecha_img_right'] = pygame.transform.scale(assets['flecha_img_right'], (55, 19))
    assets['flecha_img_up'] = pygame.transform.rotate(assets['flecha_img_right'], 90)
    assets['flecha_img_left'] = pygame.transform.rotate(assets['flecha_img_right'], 180)
    assets['flecha_img_down'] = pygame.transform.rotate(assets['flecha_img_right'], 270)
    assets['som_flecha'] = pygame.mixer.Sound('Sound effects/MC_Arrow_shoot.wav')

    #Criando as animações de tiro
    # Atirando de frente
    tiro_frente = []
    for i in range(1, 5):
        file = f'Sprites/Atirando frente/atirando_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,115))
        tiro_frente.append(img)
    assets['tiro_frente'] = tiro_frente

    # Atirando de traz
    tiro_traz = []
    for i in range(1, 5):
        file = f'Sprites/Atirando traz/atirando_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,115))
        tiro_traz.append(img)
    assets['tiro_traz'] = tiro_traz

    # Atirando para a direita
    tiro_direita = []
    for i in range(1, 5):
        file = f'Sprites/Atirando lado/atirando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(105,101))
        tiro_direita.append(img)
    assets['tiro_direita'] = tiro_direita

    # Atirando para esquerda
    tiro_esquerda = []
    for i in range(1, 5):
        file = f'Sprites/Atirando lado/atirando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(105,101))
        img = pygame.transform.flip(img, True, False)
        tiro_esquerda.append(img)
    assets['tiro_esquerda'] = tiro_esquerda


    # Criando as animações - Sprites do jogo the legend of zelda: minish cap
    # Movendo de frente
    anim_frente = []
    for i in range(1,12):
        file = f'Sprites/Frente/link_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_frente.append(img)
    assets['anim_frente'] = anim_frente

    # Movendo de traz
    anim_traz = []
    for i in range(1,12):
        file = f'Sprites/Traz/link_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_traz.append(img)
    assets['anim_traz'] = anim_traz

    # Movendo para esquerda
    anim_esquerda = []
    for i in range(1,12):
        file = f'Sprites/Lado/link_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        img = pygame.transform.flip(img, True, False)
        anim_esquerda.append(img)
    assets['anim_esquerda'] = anim_esquerda

    # Movendo para direita
    anim_direita = []
    for i in range(1,12):
        file = f'Sprites/Lado/link_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        anim_direita.append(img)
    assets['anim_direita'] = anim_direita

    # Desviando para frente
    desv_frente = []
    for i in range(1,9):
        file = f'Sprites/desviando frente/desviando_frente{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_frente.append(img)
    assets['desv_frente'] = desv_frente

    # Desviando para traz
    desv_traz = []
    for i in range(1,9):
        file = f'Sprites/desviando traz/desviando_traz{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_traz.append(img)
    assets['desv_traz'] = desv_traz

    # Desviando para a direita
    desv_direita = []
    for i in range(1,9):
        file = f'Sprites/desviando lado/desviando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        desv_direita.append(img)
    assets['desv_direita'] = desv_direita

    # Desviando para a esquerda
    desv_esquerda = []
    for i in range(1,9):
        file = f'Sprites/desviando lado/desviando_lado{i}.png'
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img,(72,101))
        img = pygame.transform.flip(img, True, False)
        desv_esquerda.append(img)
    assets['desv_esquerda'] = desv_esquerda

    # Sprite do inimigo
    assets['inimigo'] = pygame.image.load('Sprites/inimigo.png').convert_alpha()
    assets['inimigo'] = pygame.transform.scale(assets['inimigo'], (SLIME_WIDTH, SLIME_HEIGHT))

    # Fonte
    assets['fonte'] = pygame.font.Font(None, 48)

    # Som do desvio
    assets['som_desv'] = pygame.mixer.Sound('Sound effects/MC_Link_Roll.wav')

    # Trilha sonora
    pygame.mixer.music.load('Sound effects/Soundtrack.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    return assets