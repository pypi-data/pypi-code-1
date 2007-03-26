import pygame
from pygame.locals import *
import os, sys

from cellulose import *


screen = None
screen_width = 0
screen_height = 0


class ReplaceableCellDescriptor(InputCellDescriptor):

    def __set__(self, obj, value):
        from widget import Widget
        if isinstance(value, InputCell):
            if not hasattr(obj, '_cells'):
                obj._cells = {}
            obj._cells[self.get_name(obj.__class__)] = value
        #elif isinstance(value, Widget) and hasattr(value, "value"):
            #if not hasattr(obj, '_cells'):
                #obj._cells = {}
            #obj._cells[self.get_name(obj.__class__)] = value._cells['value']
        else:
            self.get_cell(obj, value).set(value)


def init(sw=640, sh=480):
    global screen_width, screen_height, screen
    screen_width = sw
    screen_height = sh
    screen = pygame.display.set_mode((screen_width, screen_height))


update_rects = []

def blit(surf, (x,y), clip_rect=None):
    if not surf: return
    global update_rects
    if not clip_rect:
        clip_rect = surf.get_rect()
    rect = screen.blit(surf, (x,y), clip_rect)
    update_rects.append(rect)
    return rect

def draw_rect(surf, color, rect, width=0):
    global update_rects
    pygame.draw.rect(surf, color, rect, width)
    update_rects.append(rect)

def update_display():
    global update_rects
    pygame.display.update(update_rects)
    update_rects = []


imagestore = {}

def get_image(path, colorkey=-1, nocache=False):
    """ get_image(path, [colorkey, [nocache]]) -> pygame.Surface

    path should be a sting. Example: get_image("data/image/my_image.png")
    Use forward slashed as demonstrated even if you are developing under
    windows, it will open the files os independent. """


    if imagestore.has_key(path):
        return imagestore[path]
    else:
        key = path.split("/")
        if len(key) == 1:
            key = key[0]
        else:
            p = ""
            for k in key:
                p = os.path.join(p, k)
            key = p
        if path[0] == "/":
            # HACK: shouldn't have to do this... (and won't work on windows)
            key = "/"+key
        if not os.path.isfile(key):
            key = os.path.join(os.path.dirname(__file__), key)
            if not os.path.isfile(key):
                print key
                print "could not find image"
                sys.exit()
        image = pygame.image.load(key)
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)

        # Add it so it doesn't have to create surf again for this image.
        if not nocache:
            imagestore.update({path: image})

    return image


