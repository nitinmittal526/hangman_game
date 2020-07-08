import pygame

#setup disply
pygame.init()
WIDTH,HEIGHT=800,500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!!")
#setup game loop
FPS=60
clock=pygame.time.Clock()
run=True

while run:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False
    if event.type==pygame.MOUSEBUTTONDOWN:
      pos=pygame.mouse.get_pos()
      print(pos)


pygame.quit()