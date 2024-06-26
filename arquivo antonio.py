import pygame
import sys
from Jogo import game_screen

infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
SLIME_WIDTH = 80
SLIME_HEIGHT = 68

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

# configurações da tela
screen_width =infoObject.current_w
screen_height =infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu Inicial')

#  paletas de referência
COLOR1 = (63, 125, 77)   # Verde Escuro
COLOR2 = (112, 191, 65)  # Verde Claro
COLOR3 = (204, 228, 62)  # Verde Amarelo
COLOR4 = (246, 230, 142) # Amarelo Claro
COLOR5 = (246, 214, 66)  # Amarelo
COLOR6 = (238, 166, 73)  # Laranja
COLOR7 = (184, 118, 68)  # Marrom Claro
COLOR8 = (131, 78, 66)   # Marrom Escuro
COLOR9 = (255,255,255)   # Branco
COLOR10 =(0,0,0)

# fontes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

#  imagem de fundo
background = pygame.image.load('sprites/background inicio.png')
background = pygame.transform.scale(background, (screen_width, screen_height))
background2 = pygame.image.load('sprites/background creditos.jpg')
background2 = pygame.transform.scale(background2, (screen_width, screen_height))
# funções para exibir o texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# funções do menu inicial
def main_menu():
    click = False
    while True:
        screen.blit(background, (0, 0))
        draw_text('Zelda da shopee', font, COLOR9, screen, screen_width // 2, screen_height // 4)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(screen_width // 2.3, screen_height // 2, 200, 50)
        button_2 = pygame.Rect(screen_width // 2.3, screen_height // 2+100,200,50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                credits()

        pygame.draw.rect(screen, COLOR6, button_1)
        pygame.draw.rect(screen, COLOR7, button_2)

        draw_text('Iniciar Jogo', small_font, COLOR9, screen, screen_width // 2, screen_height // 2 + 25)
        draw_text('Créditos', small_font, COLOR9, screen, screen_width // 2, screen_height // 2 + 125)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# funções do jogo
def game():
    running = True

    while running:
        k=0
        # screen.fill(COLOR1)
        # draw_text('Jogo em Andamento...', font, COLOR4, screen, screen_width // 2, screen_height // 2)
        for event in pygame.event.get():
            # screen.fill(COLOR1)
            # draw_text('Jogo em Andamento...', font, COLOR4, screen, screen_width // 2, screen_height // 2)
            game_screen(screen)
            # if pygame.quit():

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            k+=1
        if k>0:
            screen.fill(COLOR8)
            draw_text('GAME OVER', font, COLOR4, screen, screen_width//2, screen_height//2)
            draw_text('toque em qualquer lugar para continuar', font,COLOR4, screen, screen_width//2, screen_height//2+100)

    # if running!= True:
    #     main_menu()
        pygame.display.update()
    main_menu()
# créditos
def credits():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background2, (0, 0))
        draw_text('Créditos:', font, COLOR9, screen, screen_width // 2, screen_height // 9)
        draw_text('Daniel', small_font, COLOR9, screen, screen_width // 2, screen_height // 4)
        draw_text('Lorenzo', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 50)
        draw_text('Antonio Victor', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 100)
        draw_text('Prof. Carlos (pelo apoio)', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 150)
        draw_text('Ninjas = Lídia e Laís', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 200)
        draw_text('NINTENDO (pela nossa infância)', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 250)
        draw_text('Victor Melchert (Autor da trilha sonora)', small_font, COLOR9, screen, screen_width // 2, screen_height // 4 + 300)
        vertices = [720, 595, 150, 40]
        pygame.draw.rect(screen, COLOR6, vertices)
        draw_text('voltar', small_font, COLOR10, screen, screen_width // 2, screen_height // 4 + 350)
        #button_3 = pygame.Rect(screen_width // 3, screen_height / 8, 200, 50)
        click = False
        button_3 = pygame.Rect(screen_width // 2, screen_height // 4+350, 350, 50)

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_3.collidepoint((screen_width // 2, screen_height // 4+350)):
            if click:
                main_menu()
        

        pygame.display.update()

if __name__ == '__main__':
    main_menu()
