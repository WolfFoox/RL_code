import pygame
import os
from pygame.locals import *
from sys import  exit
#得到当前工程目录
current_dir = os.path.split(os.path.realpath(__file__))[0]
print(current_dir)
#得到文件名
bird_file1 = current_dir+"/resources/Cat.png"
bird_file2 = current_dir+"/resources/Mouse.png"
obstacle_file = current_dir+"/resources/obstacle.png"
background_file = current_dir+"/resources/background.png"
#创建小鸟，
def load_cat():
    cat = pygame.image.load(bird_file1).convert_alpha()
    return cat
def load_mouse():
    mouse = pygame.image.load(bird_file2).convert_alpha()
    return mouse
#得到背景
def load_background():
    background = pygame.image.load(background_file).convert()
    return background
#得到障碍物
def load_obstacle():
    obstacle = pygame.image.load(obstacle_file).convert()
    return obstacle
