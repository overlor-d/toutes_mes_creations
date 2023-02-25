import pygame
from random import randint


from jeu import Jeu
from joueur import Joueur



pygame.init()


#generer la fenêtre
pygame.display.set_caption("Jeux de la fuser")
screen = pygame.display.set_mode((1263, 720))

#configuration de la police
police=pygame.font.Font("police/police_n_1.ttf",36)
text=police.render("Score:",True,(0,0,0),(0,0,0))
screen.blit(text,(10,10))



#importer l'arrière plan du jeux
arriere_plan = pygame.image.load(r'image/arrierreplan.png')

#charger le jeux

jeu = Jeu()



#charger le joueur

joueur = jeu.joueur1

pygame.key.set_repeat()
#boucle du jeux
running = True

while running:
    screen.blit(text,(10,10))

    #appliquer l'arrièrre plan
    screen.blit(arriere_plan, (0, 0))
    screen.blit(joueur.image, joueur.rect)




    for projectile in jeu.joueur1.all_projectiles:
        projectile.move()

    for projectile2 in jeu.joueur1.all_projectiles2:
        projectile2.move()

    for meteorite in jeu.all_meteorite:
        meteorite.avancer()
        meteorite.barre_vie(screen)
        pygame.display.update()


    jeu.joueur1.all_projectiles.draw(screen)
    jeu.joueur1.all_projectiles2.draw(screen)


    jeu.all_meteorite.draw(screen)


    if jeu.presser.get(pygame.K_d) and jeu.joueur1.rect.x < 1150 :
        jeu.joueur1.mouvement_droit()

    elif jeu.presser.get(pygame.K_q) and jeu.joueur1.rect.x > -2:
        jeu.joueur1.mouvement_gauche()

    elif jeu.presser.get(pygame.K_s) and jeu.joueur1.rect.y < 641:
        jeu.joueur1.mouvement_haut()

    elif jeu.presser.get(pygame.K_z) and jeu.joueur1.rect.y > 0 :
        jeu.joueur1.mouvement_bas()





    pygame.display.flip()
    #fps
    clock = pygame.time.Clock()
    clock.tick(120)




    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



        elif event.type == pygame.KEYDOWN:
            jeu.presser[event.key] = True

            if event.key == pygame.K_SPACE:

                jeu.joueur1.lancer_projectile()
                jeu.joueur1.lancer_projectile2()


        elif event.type == pygame.KEYUP:
            pass

