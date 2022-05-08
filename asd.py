__docformat__ = "reStructuredText"

import pygame
import pymunk
from pymunk import Vec2d
X, Y = 0, 1
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def flipy(y):
    return -y + 600

def mouse_coll_func(arbiter, space, data):
    s1, s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True
    space = pymunk.Space()
    space.gravity = 0.0, -900.0
    balls = []
    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
    mouse_shape.collision_type = COLLTYPE_MOUSE
    space.add(mouse_body, mouse_shape)
