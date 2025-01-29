import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "virus"
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bg", (0,0))

def update():
    pass

def get_option(extra_items):
    items_to_create = ["paper"]
    for i in range(extra_items):

























pgzrun.go()