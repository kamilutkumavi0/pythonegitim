# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:41:17 2023

@author: melio
"""

import pygame
import time
#pygame.init()
ekran_genislik = 400
ekran_yukseklik = 300
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
####RENKLER####
acik_mavi = (100,200,255)
yatay_hareket = 0



while True:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            pygame.quit()
            break
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            yatay_hareket -= 10
        if keys[pygame.K_d]:
            yatay_hareket += 10
        ekran.fill(acik_mavi)
        pygame.draw.polygon(ekran, "white", [[200 + yatay_hareket, 260], [190 + yatay_hareket, 275], [210 + yatay_hareket, 275]]) # 155-140=15
        pygame.display.update()
    