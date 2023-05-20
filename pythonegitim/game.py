import pygame
import time
import random

pygame.init()
#Ekran Boyutlandırma
ekranYukseklik = 300 #Ekran yüksekliği belirlendi
ekranGenislik = 400 #Ekran genişliği belirlendi
ekran = pygame.display.set_mode((ekranGenislik,ekranYukseklik)) # Ekran ayarları yapıldı
#Renkler
mavi = (100,200,255) #Kırmızı, Yeşil, Mavi 0-255
kapat = False
hareket = 0
def ates(ekran, kordinat, dusman, kill_counter):
    for i in range(250):
        pygame.draw.rect(ekran, "red", pygame.Rect(kordinat+197,250-i,5,10))
        pygame.display.update()
        time.sleep(0.00001)
        #pygame.draw.rect(ekran, mavi, pygame.Rect(kordinat+199,250-i,2,10))
        ekran.fill(mavi)
        for j in dusman:
            if dusman[j][1] == 3:
                pygame.draw.rect(ekran, "green", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
            elif dusman[j][1] == 2:
                pygame.draw.rect(ekran, "yellow", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
            elif dusman[j][1] == 1:
                pygame.draw.rect(ekran, "red", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
                
        for j in dusman:
            if dusman[j][0][0] < kordinat + 199 <= dusman[j][0][0] + 20  and dusman[j][0][1] < 250-i < dusman[j][0][1] + 20:
                if dusman[j][1]==1:
                    del dusman[j]
                    kill_counter += 1
                    return dusman, kill_counter
                else:
                    dusman[j][1] -= 1
                    return dusman, kill_counter
        pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                             [190 + hareket, 275], 
                                             [210 + hareket, 275]])
    return dusman, kill_counter
def dusman_olusturucu(level):
    dusman = {}
    for i in range(level + 7):
        dusman[str(i)] = [[random.randint(0, 19)*20, -1*random.randint(0, 19)*20], 3]
        
    return dusman
        
 
level = 1
dusman = dusman_olusturucu(level) 
font = pygame.font.Font('freesansbold.ttf', 15)   
kill_counter = 0   
while True:
    pygame.display.update() #Ekranın güncellenmesi sağlanıyor
    ekran.fill(mavi)#Ekran rengi belirleniyor
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            pygame.quit()
            kapat = True
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                dusman, kill_counter = ates(ekran, hareket, dusman, kill_counter)
    if kapat:
        pygame.quit()
        break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if hareket > -190:
            hareket -= 0.05
    if keys[pygame.K_d]:
        if hareket < 190:
            hareket += 0.05
    for j in dusman:
        if dusman[j][1] == 3:
            pygame.draw.rect(ekran, "green", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        elif dusman[j][1] == 2:
            pygame.draw.rect(ekran, "yellow", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        elif dusman[j][1] == 1:
            pygame.draw.rect(ekran, "red", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        dusman[j][0][1] += 0.007 
        if dusman[j][0][1] >= 280:
            kapat = True
    if dusman == {}:
        level += 1
        dusman = dusman_olusturucu(level) 
    pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                         [190 + hareket, 275], 
                                         [210 + hareket, 275]])
    text = font.render("Kill: " + str(kill_counter), True, "black")
    textRect = text.get_rect()
    textRect.left=0
    textRect.top=0
    ekran.blit(text,textRect)
    
    
       