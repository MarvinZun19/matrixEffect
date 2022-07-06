import random
 
import pygame # Recuerden instalar virtual env ejecutar e instalar pygame

pwidth = 700
phight = 600
FONT_PX = 15
 
pygame.init()
 
winSur = pygame.display.set_mode((pwidth, phight))
 
font = pygame.font.SysFont("123.ttf", 25)
 
bg_suface = pygame.Surface((pwidth, phight), flags=pygame.SRCALPHA)
 
pygame.Surface.convert(bg_suface)
 
bg_suface.fill(pygame.Color(0, 0, 0, 28))
 
winSur.fill((0, 0, 0))
 
 # Digital Version
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
 
 # Letter Edition
letter = ['!', '@', '#', '$', '%', '&', '?', '¿', '¡', '1', '0', '@', '0', '0', '0', '1', '$', '!', '%', '$', '0', '1',
          '&', '1', '0', '$']
texts = [
    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)
]
 
 # Press the broadband calculation on the screen to @place some coordinate columns on the worktable and generate a list.
column = int(pwidth / FONT_PX)
drops = [0 for i in range(column)]
 
while True:
         # Get events from the queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
 
            chang = pygame.key.get_pressed()
            if(chang[32]):
                exit()
 
         # Will pause for a given number of milliseconds
    pygame.time.delay(30)
 
         # Re-edits the second image parameter
    winSur.blit(bg_suface, (0, 0))
 
    for i in range(len(drops)):
        text = random.choice(texts)
 
                 # Re-edits the image of each coordinate point
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
 
        drops[i] += 1
        if drops[i] * 10 > phight or random.random() > 0.95:
            drops[i] = 0
 
    pygame.display.flip()
    