"""Singleton game state class :P ."""

import pygame

screenx, screeny = 700, 700

screen = pygame.display.set_mode((screenx, screeny), 0, 32)
clock = pygame.time.Clock()

key_listeners = []
repeat_key_listeners = []
astroids = []
ship = None
create_ship = False

running = True
menu_visible = True

ticks = 0

def start_game():
    global astroids, ship, running, create_ship
    astroids = []
    running = True
    if ship:
        repeat_key_listeners.remove(ship.key_pressed)
    create_ship = True
