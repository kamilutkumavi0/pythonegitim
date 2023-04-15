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
def ates(ekran, kordinat):
    for i in range(250):
        pygame.draw.rect(ekran, "red", pygame.Rect(kordinat+197,250-i,5,10))
        pygame.display.update()
        time.sleep(0.0001)
        #pygame.draw.rect(ekran, mavi, pygame.Rect(kordinat+199,250-i,2,10))
        ekran.fill(mavi)
        pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                             [190 + hareket, 275], 
                                             [210 + hareket, 275]])
        
while True:
    pygame.display.update() #Ekranın güncellenmesi sağlanıyor
    ekran.fill(mavi)#Ekran rengi belirleniyor
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            pygame.quit()
            kapat = True
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                ates(ekran, hareket)
    if kapat:
        break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if hareket > -190:
            hareket -= 0.1
    if keys[pygame.K_d]:
        if hareket < 190:
            hareket += 0.1
    pygame.draw.polygon(ekran, "white", [[200 + hareket, 260], 
                                         [190 + hareket, 275], 
                                         [210 + hareket, 275]])
    
    
