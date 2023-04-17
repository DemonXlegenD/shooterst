import pygame
import sys
import math
import time
from enemy import Enemy
from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py
from spaceship import Spaceship
#import the class Spaceship from the file spaceship.py

from screen import *
from affichage import *

#définir une clock
clock = pygame.time.Clock()
FPS = 100

#Initialize Pygame
pygame.init()



game = Game()
settings = Settings()

game.screen.show_screen()
#Boucle de jeu

running = True

while running:

    # draw scrolling background
    if game.is_playing:
        #Scroll background
        game.screen.scrolling(5)
    else:
        #Scroll background
        game.screen.scrolling(2)
    

    # reset scroll
    if abs(game.screen.scroll) > game.screen.bg_width:
        game.screen.scroll = 0

    #  ------------------------------------------- Projectiles -------------------------------------------
    #recuperer les projectiles
    for projectile in game.player.all_projectile:
        projectile.move(game.ult_event)

    # appliquer l'ensemble des image de mon groupe de projectile
    game.player.all_projectile.draw(game.screen.screen)

        #recuperer les projectiles des ennemis
    for enemy in game.all_enemy:
        for projectile in enemy.all_projectile:
            projectile.move(game.ult_event)

    # appliquer l'ensemble des image de mon groupe de projectile
    for enemy in game.all_enemy:
        enemy.all_projectile.draw(game.screen.screen)

    #  ------------------------------------------- Enemy -------------------------------------------
    #recuperer les ennemy
    for enemy in game.all_enemy:
        enemy.forward(game.ult_event)
        enemy.update_health_bar(game.screen.screen) 
        # while enemy.rect.x != 1600:
        #     enemy.spawn()

    # appliquer l'ensemble des image de mon groupe de mosntres
    game.all_enemy.draw(game.screen.screen)

    #  ------------------------------------------- powerUp -------------------------------------------
    #recuperer les ennemy
    for powerUp in game.player.all_upgrades:
        powerUp.forward()
    game.player.all_upgrades.draw(game.screen.screen)
     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing):
        #déclencher les isntructions de la partie
        game.update(game.screen, game.screen.seconde) 
        print("game")
    #---------settings--------#
    elif((not game.is_playing) and game.are_buttons_settings_shown()):
        game.show_settings()
        print("set1")
    #verifier quelles sont les settings lancés
    elif((not game.is_playing) and game.are_buttons_settings_shown()):
        game.show_gameplay()
        print("set2")
    elif((not game.is_playing) and game.are_buttons_settings_shown()):
        game.show_audio()
        print("set3")
    elif((not game.is_playing) and game.are_buttons_settings_shown()):
        game.show_controle()
        print("set4")
        
    #Show the screen with the difficulties
    elif(not game.is_playing and game.are_buttons_planete_shown()):
        game.show_planetes()
        print("planete")

    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and game.are_buttons_difficulty_shown()):
        game.show_game_modes()
        print("mode")
    #vérifier si notre jeu n'a pas commencé
    else:
        print("noob")
        game.show_menu()

    game.show_buttons()

    #Dessin de la fenêtre
    pygame.display.flip()

    # Faire spawn des ennemis
    if game.is_playing == True:
        
        if time.time() > game.screen.seconde + 3:
            game.spawn_monster(game.screen.screen)
            game.screen.seconde = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
            

        if event.type == pygame.KEYDOWN and game.is_playing:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            #détecter si la touche ctrl est enclenchée pour lancer notre ult
            if event.key == pygame.K_LCTRL:
                game.player.ultimate(game.ult_event)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):


            #vérification pour svaoir si la souris est en collision avec le bouton
            if (game.button_play.button_rect.collidepoint(event.pos) and game.button_play.is_shown):
                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            elif(game.buttons_settings[0].button_rect.collidepoint(event.pos) and game.buttons_settings[0].is_shown):
                game.to_show_settings()
            elif(game.buttons_settings[1].button_rect.collidepoint(event.pos) and game.buttons_settings[1].is_shown):
                settings.show_gameplay()
            elif(game.buttons_settings[3].button_rect.collidepoint(event.pos) and game.buttons_settings[3].is_shown):
                settings.show_audio()
            elif(game.buttons_settings[5].button_rect.collidepoint(event.pos) and game.buttons_settings[5].is_shown):
                settings.show_commandes()
            elif(game.buttons_settings[-1].button_rect.collidepoint(event.pos) and game.buttons_settings[-1].is_shown):
                settings.back_settings()
            
             
            elif (game.buttons_difficulties[0].button_rect.collidepoint(event.pos) and game.buttons_difficulties[0].is_shown):
                game.create_player(1)
                game.start()

            elif (game.buttons_difficulties[1].button_rect.collidepoint(event.pos) and game.buttons_difficulties[1].is_shown):
                game.create_player(1.5)

                game.start()
            elif (game.buttons_difficulties[2].button_rect.collidepoint(event.pos) and game.buttons_difficulties[2].is_shown):
                game.create_player(2)

                game.start()
            elif (game.buttons_difficulties[3].button_rect.collidepoint(event.pos) and game.buttons_difficulties[3].is_shown):
                game.create_player(3)

                game.start()
                 
            for planete in game.buttons_planetes:

                if (planete.button_rect.collidepoint(event.pos) and game.are_buttons_planete_shown()):
                    game.show_game_modes()
                
                #mettre le jeu en monde "lancé"
                

           
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
