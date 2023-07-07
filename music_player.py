import pygame
import os

pygame.init()

music_directory = r"C:\Users\mycomputer\Music"

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
pygame.mixer.init()

pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():
        # Move to the next track
        current_track = (current_track + 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()

pygame.quit()

import pygame
import os

pygame.init()

music_directory = r"C:\Users\mycomputer\Music"

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
pygame.mixer.init()

def play_current_track():
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
    pygame.mixer.music.play()

play_current_track()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():
        # Move to the next track
        current_track = (current_track + 1) % len(music_files)
        # Play the next track
        play_current_track()

pygame.quit()

import pygame
import os
import keyboard

pygame.init()

music_directory = r"C:\Users\mycomputer\Music"

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
pygame.mixer.init()

pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))

pygame.mixer.music.play()

running = True
while running:
    if keyboard.is_pressed("space"):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    if keyboard.is_pressed("right"):
        current_track = (current_track + 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()

    if keyboard.is_pressed("left"):
        current_track = (current_track - 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

import pygame
import os
import keyboard

pygame.init()

music_directory = input("Enter the path to your music directory: ")

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_track = 0
pygame.mixer.init()

pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))

pygame.mixer.music.play()

running = True
while running:
    if keyboard.is_pressed("space"):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    if keyboard.is_pressed("right"):
        current_track = (current_track + 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()

    if keyboard.is_pressed("left"):
        current_track = (current_track - 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
