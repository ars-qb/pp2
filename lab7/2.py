import os
import pygame
import eyed3

pygame.init()
pygame.mixer.init()

WIDTH = 400
HEIGHT = 400
FPS = 60
PLAYLIST = [
    'music/dancin.mp3',
    'music/medina.mp3',
    'music/mockingbird.mp3'
]
COUNT = len(PLAYLIST)



clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')


current_track = 0
pygame.mixer.music.load(PLAYLIST[current_track])

def update_album_art():
    global album_art_image
    audio_file = eyed3.load(PLAYLIST[current_track])
    if audio_file.tag and audio_file.tag.images:
        image_data = audio_file.tag.images[0].image_data
        image_type = audio_file.tag.images[0].mime_type
        with open("album_art." + image_type.split("/")[-1], "wb") as img_file:
            img_file.write(image_data)
        album_art_image = pygame.image.load("album_art." + image_type.split("/")[-1])
        album_art_image = pygame.transform.scale(album_art_image, (WIDTH, HEIGHT))
    else:

        album_art_image = None

def update_track_info():
    global track_name_text, track_artist_text
    audio_file = eyed3.load(PLAYLIST[current_track])
    if audio_file.tag:
        track_name = audio_file.tag.title
        track_artist = audio_file.tag.artist
    else:
        track_name = "Unknown"
        track_artist = "Unknown"
    font = pygame.font.SysFont(None, 36)
    track_name_text = font.render(track_name, True, (255, 255, 255))
    track_artist_text = font.render(track_artist, True, (255, 255, 255))

update_album_art()
update_track_info()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.play()

            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % COUNT
                pygame.mixer.music.load(PLAYLIST[current_track])
                pygame.mixer.music.play()
                update_album_art()
                update_track_info()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % COUNT
                pygame.mixer.music.load(PLAYLIST[current_track])
                pygame.mixer.music.play()
                update_album_art()
                update_track_info()

    screen.fill((255, 255, 255))
    if album_art_image:
        screen.blit(album_art_image, (0, 0))

    screen.blit(track_name_text, (10, 350))
    screen.blit(track_artist_text, (10, 370))
    pygame.display.update()