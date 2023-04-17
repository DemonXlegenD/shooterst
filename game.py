import pygame
import time
import random
from screen import Screen
from spaceship import Spaceship
from enemy import Enemy
from button import Button
from ult_event import UltimateCharging

#créer une classe qui va représenter notre jeu
class Game:

    def __init__(self):
        self.screen = Screen(1920, 1080)
        self.which_screen = 0
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        self.mode_is_choose = False
        self.planete_is_choose = False
        self.difficulty = 1

        # generer l'evenement ult
        self.ult_event = UltimateCharging(self.difficulty)

        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200,15,15)
        self.all_players.add(self.player)

        self.pressed = {}

        self.button_play = Button(self.screen, 2.7, 1.7, 400, 150,'PygameAssets/button.png')

        #=====================================================================================================================#
        #------------------------------------------------------PLANETES-------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_planetes = [
            Button(self.screen, 1.5, 2.50, 300, 300,'PygameAssets/terre.png'), 
            Button(self.screen, 2, 1.5, 200, 200,'PygameAssets/planete1.png'), 
            Button(self.screen, 1.80, 7.5, 250, 250,'PygameAssets/planete2.png'),
            Button(self.screen, 2.5, 3, 200, 200,'PygameAssets/planete3.png'),
            Button(self.screen, 8, 1.5, 450, 300,'PygameAssets/planete4.png'),
            Button(self.screen, 1.20, 8.5, 175, 175,'PygameAssets/planete5.png'),
            Button(self.screen, 1.25, 1.25, 150, 150,'PygameAssets/planete6.png')
            ]
        
        #=====================================================================================================================#
        #------------------------------------------------------SETTINGS-------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_settings = [
            Button(self.screen, 100, 100, 50, 50,'PygameAssets/button-settings.png'),
            Button(self.screen, 10.15, 4, 200, 150,'PygameAssets/Gameplay.png'),
            Button(self.screen, 10.15, 4, 200, 150,'PygameAssets/Gameplay_underline.png'),
            Button(self.screen, 2.25, 4, 200, 150,'PygameAssets/audio.png'),
            Button(self.screen, 2.25, 4, 200, 150,'PygameAssets/audio_underline.png'),
            Button(self.screen, 1.3, 4, 200, 150,'PygameAssets/controle.png'),
            Button(self.screen, 1.3, 4, 200, 150,'PygameAssets/controle_underline.png'),
            Button(self.screen, 100, 100, 100, 100,'PygameAssets/retour.png')
        ]

        #=====================================================================================================================#
        #---------------------------------------------------DIFFICULTIES------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_difficulties = [
            Button(self.screen, 3, 6, 500, 150,'PygameAssets/easy-button.png'),
            Button(self.screen, 3, 3, 500, 150,'PygameAssets/medium-button.png'),
            Button(self.screen, 3, 2, 500, 150,'PygameAssets/hard-button.png'),
            Button(self.screen, 3, 1.5, 500, 150,'PygameAssets/nightmare-button.png')
        ]
        #groupe de monstres
        self.all_enemy = pygame.sprite.Group()

        #mettre le score a 0
        self.score = 0
        self.font = pygame.font.Font("Roboto/Roboto-Bold.ttf", 25)
        #gérer le son
        # self.sound_manager = SoundManager()
    
    # def test_score(self):
        # self.load_score.new_score = self.score
        # self.load_score.check_update()
        # if self.loard_score.name_needed:
            
        


    def create_player(self, difficulty):
        #générer notre joueur
        self.difficulty = difficulty
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200, 10, 30)
        self.all_players.add(self.player)

    
    def show_settings(self):
        self.buttons_settings[1].show_button()
        self.buttons_settings[3].show_button()
        self.buttons_settings[5].show_button()
        self.buttons_settings[7].show_button()
    def show_gameplay(self):
        self.buttons_settings[2].show_button()
        self.buttons_settings[3].show_button()
        self.buttons_settings[5].show_button()
        self.buttons_settings[7].show_button()

    def show_audio(self):
        self.buttons_settings[1].show_button()
        self.buttons_settings[4].show_button()
        self.buttons_settings[5].show_button()
        self.buttons_settings[7].show_button()

    def show_controle(self):
        self.buttons_settings[1].show_button()
        self.buttons_settings[3].show_button()
        self.buttons_settings[6].show_button()
        self.buttons_settings[7].show_button()
    
    def show_menu(self):
        self.button_play.is_shown = True
        self.buttons_settings[0].is_shown = True
        for settings in self.buttons_settings[1:]:
            settings.is_shown = False
        for planete in self.buttons_planetes:
            planete.is_shown = False
        for difficulty in self.buttons_difficulties:
            difficulty.is_shown = False
    
    def show_planetes(self):
        self.button_play.is_shown = False
        for settings in self.buttons_settings:
            settings.is_shown = False
        for planete in self.buttons_planetes:
            planete.is_shown = True
        for difficulty in self.buttons_difficulties:
            difficulty.is_shown = False

    def show_game_modes(self):
        self.button_play.is_shown = False
        for settings in self.buttons_settings:
            settings.is_shown = False
        for planete in self.buttons_planetes:
            planete.is_shown = False
        for difficulty in self.buttons_difficulties:
            difficulty.is_shown = True

    def to_show_settings(self):
        self.button_play.is_shown = False
        self.buttons_settings[0].is_shown = False
        for settings in self.buttons_settings[1:]:
            settings.is_shown = True
        for planete in self.buttons_planetes:
            planete.is_shown = False
        for difficulty in self.buttons_difficulties:
            difficulty.is_shown = False

    def show_buttons(self):
        self.button_play.show_button()
        for settings in self.buttons_settings:
            settings.show_button()
        for planete in self.buttons_planetes:
            planete.show_button()
        for difficulty in self.buttons_difficulties:
            difficulty.show_button()

    def are_buttons_planete_shown(self):
        shown = True
        for button in self.buttons_planetes:
            if(not button.is_shown):
                shown = button.is_shown

        return shown
    
    def are_buttons_settings_shown(self):
        shown = True
        for button in self.buttons_settings[1:]:
            if(not button.is_shown):
                shown = button.is_shown

        return shown

    def are_buttons_difficulty_shown(self):
        shown = True
        for button in self.buttons_difficulties:
            if(not button.is_shown):
                shown = button.is_shown

        return shown
            

    def start(self):
        self.is_playing = True
        self.button_play.is_shown = False
        for settings in self.buttons_settings:
            settings.is_shown = False
        for planete in self.buttons_planetes:
            planete.is_shown = False
        for difficulty in self.buttons_difficulties:
            difficulty.is_shown = False
        


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre les joueurs à 100 de vie, jeu en attente
        self.all_enemy = pygame.sprite.Group()
        self.player.hp = self.player.max_hp
        self.is_playing = False
        self.score = 0

    def add_score(self, points = 10):
        self.score += points

    def update(self, screen, seconde):

        #afficher le score sur l'écran  
        score_text = self.font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.screen.blit(score_text, (20, 20))

        #appliquer l'image de notre joueur
        screen.screen.blit(self.player.image, self.player.rect)
        
        # afficher barre de vie
        self.player.update_health_bar(screen.screen)

        # Spawn ennemis
        # if time.time() > self.screen.seconde + 30:
        #     self.spawn_monster()
        #     self.screen.seconde = time.time()


        # #actualiser la barre de vie du joueur
        # self.player.update_health_bar(screen)

        # #actualiser la barre d'évenement du jeu
        # self.comet_event.update_bar(screen)

        # #animer joueurs
        # self.player.update_animation()
        

        # #récuperer les projectiles du joueurs
        # for projectile in self.player.all_projectiles:
        #     projectile.move()

        # #récuperer les monstres du jeu
        # for monster in self.all_monsters:
        #     monster.forward()
        #     monster.update_health_bar(screen)
        #     monster.update_animation()

        #récuperer les comètes du jeu
        # for comet in self.comet_event.all_comets:
        #     comet.fall()

        # #appliquer l'ensemble des images de mon groupe de projectiles
        # self.player.all_projectiles.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de monstres
        # self.all_monsters.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de comètes
        # self.comet_event.all_comets.draw(screen)

        #vérifier si le joueur souhaite aller à gauche ou à droite
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) and self.player.rect.x + self.player.rect.width<= screen.screen.get_width():
            self.player.move_right()
        if (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) and self.player.rect.x >= 0 :
            self.player.move_left()
        if (self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_s)) and self.player.rect.y + self.player.rect.height<= screen.screen.get_height()-50:
            self.player.move_down()
        if (self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_z)) and self.player.rect.y >= 0 :
            self.player.move_up()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self, screen):
        enemy_number = random.randint(1, 2)
        print("number", enemy_number)

        for i in range(0, enemy_number):

            enemy_spawn = random.randint(0,2)
            print("spawn", enemy_spawn)

            if enemy_spawn == 0:
                print("0")
                # Ennemi de collision
                enemy = Enemy(self, 0, self.difficulty, screen)
            elif enemy_spawn == 1:
                print("1")
                # Ennemi one shot
                # Ennemi missiles
                enemy = Enemy(self, 1, self.difficulty, screen)
            elif enemy_spawn == 2:
                #enemmi wave missiles
                enemy = Enemy(self, 2, self.difficulty, screen)

            self.all_enemy.add(enemy)