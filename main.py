from turtle import bgcolor
import pygame
from random import randint
 
pygame.init()
 
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
 
# 4 compulsory method: init (create), destroy, set, get
 
class Area():
    def __init__(self, x, y, width, height, border_color, bg_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.border_color = border_color
    #Set Default, put it last
 
    def set_color(self, new_color):
        self.bg_color = new_color
        # pygame.draw.rect(Window, self.fill_color, rect)
    
    def fill_color(self):
        #draw the rectangle
        pygame.draw.rect(window, self.bg_color, self.rect)
        #draw the outline
        pygame.draw.rect(window, self.border_color, self.rect, 5)

 
class Label(Area):
    def __init__(self, x, y, width, height, border_color, bg_color, text):
        super().__init__(x, y, width, height, border_color, bg_color)
        # font =  pygame.font.Font(None, 70)
        self.text = text
 
    def set_text(self, new_text):
        self.text = new_text
 
    def draw(self):
        self.fill_color()
        txt_font =  pygame.font.Font(None, 36)
        window.blit(txt_font.render(self.text, True, (0, 0, 0)) ,(self.rect.x + 10, self.rect.y + 50))
 
Timer = 5
Timer_label = Label(10 ,10, 105, 75, (199, 253, 253), (199, 253, 253),'Timer: ' + str(Timer))
 
#point counter
point = 0
point_label = Label(300 ,10, 105, 75, (199, 253, 253), (199, 253, 253),'Score: ' + str(point))


# card1 = Label(10, 150, 100, 150, (255, 255, 0) , 'CLICK')
# card2 = Label(140, 150, 100, 150, (255, 255, 0) , 'CLICK')
# card3 = Label(270, 150, 100, 150, (255, 255, 0) , 'CLICK')
# card4 = Label(400, 150, 100, 150, (255, 255, 0) , 'CLICK')
 
cards = list()
for i in range(4):
    card = Label(10 + i * 130, 150, 100, 150, (79, 82, 246), (255, 255, 0) , "")
    cards.append(card)
 
 
 
timeout = 0      #about 20ms
begin = 0
finish = 0



while int(Timer) != 0:
    Timer -= finish - begin

    Timer_label.set_text('Timer: ' + str(int(Timer))) # set a new timer
    point_label.set_text('Score: ' + str(int(point)))
    begin = pygame.time.get_ticks() / 1000 #in millisecond
    if timeout <= 0:
        to_click = randint(0, 3)
        for i in range(4):
 
            #reset all card
            cards[i].set_color((255, 255, 0)) #yellow
            if i == to_click:
                    cards[i].set_text("CLICK!")
            else:
                    cards[i].set_text('')
        timeout = 20
    else:
        timeout -= 1
    # cards[to_click].set_text("CLICK")
 
    #key press event, mouse click event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
 
 
        if e.type == pygame.MOUSEBUTTONDOWN:
            for i in range(4):
                if cards[i].rect.collidepoint(pygame.mouse.get_pos()):
                    if i == to_click:
                        cards[i].set_color((0, 255, 51)) #green
                        point += 1

                    else:   
                        cards[i].set_color((255, 0, 0))#red
                        point -= 1

                            
    if Timer == 0:
        break
 
    window.fill((199, 253, 253))
 
    for card in cards:
        card.draw()
    Timer_label.draw()
    point_label.draw()
    
    

    finish = pygame.time.get_ticks() / 1000
    pygame.display.update()
    clock.tick(40) #FPS


Result = ''

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    # Result (Win or Lose):

    

    txt_font =  pygame.font.SysFont('comicsansms', 50)

    if point > 0:
        window.fill((0, 255, 51))
        window.blit(txt_font.render('YOU WIN!', True, (0, 0, 0)) ,(90, 240))
    else:
        window.fill((255, 0, 0))
        window.blit(txt_font.render('Close to winning', True, (0, 0, 0)) ,(80, 240))


    pygame.display.update()

#hand running: run  the code without the need of computer or in your mind