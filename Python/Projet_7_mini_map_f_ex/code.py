################################################################################
#import des modules
################################################################################

import pygame

pygame.init()

################################################################################
#fonctions
################################################################################



################################################################################
#corp de programme
################################################################################

#variables
x_carte = 0
y_carte = 0
dim_fond_x = 1000
dim_fond_y = 1000
fond = pygame.image.load(r'Images\fond\fond_1.png')
fond = pygame.transform.scale(fond,(dim_fond_x,dim_fond_y))
fond_noir = pygame.image.load(r'Images\fond\fond_2.png')

#configuration de la fenetre
pygame.display.set_caption("carte")
dimension_fenetre = (1000, 1000)
screen = pygame.display.set_mode(dimension_fenetre)

marche = True 
scene = 1 

while marche :
    while scene == 1:
        screen.blit(fond_noir,(0,0))
        screen.blit(fond,(x_carte,y_carte))

        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    marche = False
                    pygame.quit()

            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    x_carte += 100
                elif event.key == pygame.K_d:
                    x_carte -= 100
                elif event.key == pygame.K_z:
                    y_carte += 100
                elif event.key == pygame.K_s:
                    y_carte -= 100

            elif event.type == pygame.MOUSEWHEEL:

                if event.y < 0:
                    dim_fond_x -= 500
                    dim_fond_y -= 500
                    if (dim_fond_x and dim_fond_y) == 500 :
                        dim_fond_x = 1000
                        dim_fond_y = 1000
                        x_carte = 0
                        y_carte = 0
                    fond = pygame.transform.scale(fond,(dim_fond_x,dim_fond_y))
                elif event.y > 0:
                    dim_fond_x += 500
                    dim_fond_y += 500
                    if (dim_fond_x and dim_fond_y) == 4500 :
                        dim_fond_x = 4000
                        dim_fond_y = 4000
                    fond = pygame.transform.scale(fond,(dim_fond_x,dim_fond_y))
