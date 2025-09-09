"""
Crie um programa que abra e leia um aquivo MP3.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import pygame

pygame.init()

print("Bom dia! Hora de brilhar como o CR7 ✨💪")
pygame.mixer.music.load('arquivos/bom-dia-do-cr7.mp3')
pygame.mixer.music.play()
input("Pressione Enter para pular... mas você não vai fazer isso com o CR7, vai? 😏")
pygame.event.wait()
