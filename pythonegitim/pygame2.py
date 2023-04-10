# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:36:39 2023

@author: melio
"""

import pygame
import time
ekran_genislik = 400
ekran_yukseklik = 300
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
####RENKLER####
siyah = (0,0,0)
kirmizi = (255,0,0)
yesil = (0,255,0)
mavi = (0,0,255)
beyaz = (255,255,255)
acik_mavi = (100,200,255)
renkler = [siyah, kirmizi, yesil, mavi, beyaz]
sayac = 0
yatay_hareket = 0
def ates(ekran, kordinat, dusman):
    for i in range(250):
        pygame.draw.rect(ekran, "white", pygame.Rect(kordinat+199,250-i,2,10))
        pygame.display.update()
        time.sleep(0.0001)
        pygame.draw.rect(ekran, acik_mavi, pygame.Rect(kordinat+199,250-i,2,10))
        pygame.display.update()
        for j in dusman:
            if dusman[j][0] < kordinat + 199 < dusman[j][0] + 20 and dusman[j][1] < 250-i < dusman[j][1] + 20:
                del dusman[j]
                return dusman
    return dusman
    
dusman = {"birinci": (30,30), "ikinci" : (70,50), "ucuncu" : (80,90), "dorduncu" : (120,60), "besinci" : (160,30), "besinci" : (160,30)}
while True:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            pygame.quit()
            break
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                dusman = ates(ekran, yatay_hareket, dusman)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if yatay_hareket > -190:
                yatay_hareket -= 2
        if keys[pygame.K_d]:
            if yatay_hareket < 190:
                yatay_hareket += 2
        #if keys[pygame.K_SPACE]:
         #   ates(ekran, yatay_hareket)
        ekran.fill(acik_mavi)
        for j in dusman:
            pygame.draw.rect(ekran, "red", pygame.Rect(dusman[j][0], dusman[j][1],20,20))
        pygame.draw.polygon(ekran, "white", [[200 + yatay_hareket, 260], [190 + yatay_hareket, 275], [210 + yatay_hareket, 275]])
        pygame.display.update()
    