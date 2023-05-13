import pygame
import time

#Ekran Boyutlandırma
ekranYukseklik = 300 #Ekran yüksekliği belirlendi
ekranGenislik = 400 #Ekran genişliği belirlendi
ekran = pygame.display.set_mode((ekranGenislik,ekranYukseklik)) # Ekran ayarları yapıldı
#Renkler
mavi = (100,200,255) #Kırmızı, Yeşil, Mavi 0-255
kapat = False
hareket = 0
def ates(ekran, kordinat, dusman):
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
                    return dusman
                else:
                    dusman[j][1] -= 1
                    return dusman
        pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                             [190 + hareket, 275], 
                                             [210 + hareket, 275]])
    return dusman

dusman = {"birinci": [[30,309], 3], "ikinci" : [[70,50], 3], 
          "ucuncu" : [[80,90], 3], "dorduncu" : [[120,60], 3], 
          "besinci" : [[160,30], 3]}        
while True:
    pygame.display.update() #Ekranın güncellenmesi sağlanıyor
    ekran.fill(mavi)#Ekran rengi belirleniyor
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            pygame.quit()
            kapat = True
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                dusman = ates(ekran, hareket, dusman)
    if kapat:
        break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if hareket > -190:
            hareket -= 0.01
    if keys[pygame.K_d]:
        if hareket < 190:
            hareket += 0.01
    for j in dusman:
        if dusman[j][1] == 3:
            pygame.draw.rect(ekran, "green", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        elif dusman[j][1] == 2:
            pygame.draw.rect(ekran, "yellow", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        elif dusman[j][1] == 1:
            pygame.draw.rect(ekran, "red", pygame.Rect(dusman[j][0][0], dusman[j][0][1],20,20))
        dusman[j][0][1] += 0.001
    pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                         [190 + hareket, 275], 
                                         [210 + hareket, 275]])
    
    