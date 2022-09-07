import pygame
import random
import os 
from classes import ramenbowl, softegg, rottenegg
pygame.font.init()
pygame.mixer.init()
 
digital = pygame.font.Font('slkscr.ttf', 20)
gameoverfont = pygame.font.Font('slkscr.ttf', 30)
WIDTH, HEIGHT = 360, 360
EGG_WIDTH, EGG_HEIGHT = 90, 90 
ENEMYEGG_WIDTH, ENEMYEGG_HEIGHT = 60, 60 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tan's Ramen Shop")
FPS = 60 
WHITE = (255, 255, 255)
ORANGE = (250, 140, 0)
BLACK = (0, 0, 0)
bgimg = pygame.transform.scale(pygame.image.load(os.path.join('images', 'ramenshop.PNG')), (WIDTH, HEIGHT))

eggcrack = pygame.mixer.Sound(os.path.join('sounds', 'eggcrack.mp3'))
points = pygame.mixer.Sound(os.path.join('sounds', 'point.mp3'))
bgmusic = pygame.mixer.Sound(os.path.join('sounds', 'bgmusic.mp3'))
pygame.mixer.Channel(0).play(bgmusic)
pygame.mixer.Channel(0).set_volume(0.3)
pygame.mixer.Channel(1).set_volume(0.8)
pygame.mixer.Channel(2).set_volume(0.8)

def game_over_screen(score_value):
    pygame.mixer.Channel(0).fadeout(3000)
    WIN.fill(ORANGE)
    gameover_text = gameoverfont.render("GAME OVER", 1, (255, 0,0))
    scoreover_text = digital.render("Final Score: " + str(score_value), 1, BLACK)
    WIN.blit(gameover_text, (WIDTH//2 - gameover_text.get_width()//2, HEIGHT//2 - gameover_text.get_height()))
    WIN.blit(scoreover_text, (WIDTH//2 - scoreover_text.get_width()//2, HEIGHT//2 - gameover_text.get_height() + 10 + scoreover_text.get_height()))
    restart_text = digital.render("CLICK SCREEN TO RESTART", 1, WHITE)
    WIN.blit(restart_text, (WIDTH//2- restart_text.get_width()//2, 300))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] ==1:
        pygame.mixer.Channel(0).play(bgmusic) 
        main()

def window(ramenlover, egg1, egg2, enemyegg, score_value, lives):
    WIN.fill(WHITE)
    if lives > 0:
        WIN.blit(bgimg, (0,0))
        score_text = digital.render("Score: " + str(score_value), 1, WHITE)
        lives_text = digital.render("Lives: " + str(lives), 1, BLACK)
        WIN.blit(score_text, (10, 20))
        WIN.blit(ramenlover.image, (ramenlover.x, ramenlover.y))
        WIN.blit(enemyegg.image, (enemyegg.x, enemyegg.y))
        WIN.blit(egg1.image, (egg1.x, egg1.y))
        WIN.blit(egg2.image, (egg2.x, egg2.y))
        WIN.blit(lives_text, (10, 300))
        pygame.display.update()
    else:
        game_over_screen(score_value)


def main():
    ramenlover = ramenbowl(125, 250, 120, 120)
    egg1 = softegg(random.randrange(0, WIDTH-45), 5, EGG_WIDTH, EGG_HEIGHT, 5)
    egg2 = softegg(random.randrange(0, WIDTH-45), 5, EGG_WIDTH, EGG_HEIGHT, 3)
    enemyegg = rottenegg(random.randrange(0, WIDTH-45), 3, ENEMYEGG_WIDTH, ENEMYEGG_HEIGHT, 3)
    clock = pygame.time.Clock()
    score_value = 0 
    lives = 3 
    run = True; 
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            ramenlover.move("RIGHT")
        if keys_pressed[pygame.K_LEFT]:
            ramenlover.move("LEFT")
        egg1.y += egg1.vel
        egg2.y += egg2.vel
        enemyegg.y += enemyegg.vel
        if egg1.y > ramenlover.y and lives != 0:
            if ramenlover.x <= egg1.x <= ramenlover.x + ramenlover.width//2:
                score_value += 1 
                egg1.RESPAWN()
                pygame.mixer.Channel(1).play(points, loops=0)
            else: 
                egg1.RESPAWN()

        if egg2.y > ramenlover.y and lives != 0: 
            if ramenlover.x <= egg2.x <= ramenlover.x + ramenlover.width//2:
                score_value += 1
                egg2.RESPAWN()
                pygame.mixer.Channel(1).play(points, loops=0)
            else:
                egg2.RESPAWN()

        if enemyegg.y > ramenlover.y and lives != 0: 
            if ramenlover.x <= enemyegg.x + enemyegg.width//2 and enemyegg.x <= ramenlover.x + ramenlover.width*.65:
                lives -= 1
                enemyegg.RESPAWN()
                pygame.mixer.Channel(2).play(eggcrack, loops=0)
            else:
                enemyegg.RESPAWN()

        window(ramenlover, egg1, egg2, enemyegg, score_value, lives)


    pygame.quit()


if __name__ == "__main__":
    main()