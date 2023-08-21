import random

import pygame, sys
import circle
import time
from PIL import Image

kx = []
ky = []

w = 640
h = 480
l = 0

rand = random.Random()
def cords(pos, size):
    return (int(pos.x / size), int(pos.y / size))

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Hello World")
red = (255, 0, 0, 0)
ball_list = []

ballsize = 10
size = 2 * ballsize
gravity = pygame.Vector2(0, 0.1)
timestep = 1
iter = 8

maxx = int(w / size)
maxy = int(h / size)
grid = []
for i in range(maxx):
        grid.append([])
        for j in range(maxy):
            grid[i].append([])


num = 0
maxnum = int(maxy * maxx )

def checkcollisioningrid(box1, box2):
    for i in box1:
        for j in box2:
            i.checkCollision(j)
def checkcollisioninbox(box):
    for i in box:
        for j in box:
            if i == j:
                break
            i.checkCollision(j)
def checkcollision(boxlist, x, y):
    if len(boxlist[x][y]) == 0:
        return
    try:
        checkcollisioninbox(boxlist[x][y])
        try:
            checkcollisioningrid(boxlist[x][y], boxlist[x + 1][y])
        except:
            pass
        checkcollisioningrid(boxlist[x][y], boxlist[x - 1][y])
        checkcollisioningrid(boxlist[x][y], boxlist[x][y + 1])
        checkcollisioningrid(boxlist[x][y], boxlist[x][y - 1])
        checkcollisioningrid(boxlist[x][y], boxlist[x + 1][y + 1])
        checkcollisioningrid(boxlist[x][y], boxlist[x - 1][y + 1])
        checkcollisioningrid(boxlist[x][y], boxlist[x + 1][y - 1])
        checkcollisioningrid(boxlist[x][y], boxlist[x - 1][y - 1])
    except:
        pass

with Image.open(r"D:\smile.png") as im:
    pix = im.load()
    while True:
        screen.fill((0, 0, 255, 0))

        for i in ball_list:
            i.applyForce(gravity)
            i.updatepos(timestep)
        for k in range(iter):
            for x in range(maxx):
                for y in range(maxy):
                    checkcollision(grid, x, y)
        for i in grid:
            for j in i:
                j.clear()
        for each in ball_list:
            each.satisfyConstrain()
            grid[cords(each.pos, size)[0]][cords(each.pos, size)[1]].append(each)
        for each in ball_list:
            each.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ball = circle.Ball(pos, (0, 0), ballsize, red, w, h)
                grid[int(pos[0] / size)][int(pos[1] / size)].append(ball)
                ball_list.append(ball)
            if event.type == pygame.KEYDOWN:
                with open("demofile2.txt", "w") as f:
                    for each in ball_list:
                        f.write(str(each.pos.x) + "\n")
                        f.write(str(each.pos.y) + "\n")
        mouse = pygame.mouse.get_pressed(num_buttons=3)
        # if mouse[0]:
        #     pos = pygame.mouse.get_pos()
        #     ball = circle.Ball(pos, (0, 0), ballsize, red, w, h)
        #     grid[int(pos[0] / size)][int(pos[1] / size)].append(ball)
        #     ball_list.append(ball)
        #     time.sleep(0.01)

        pos = (w/2 , 100)
        with open("demofile2.txt", "r") as f:
            k = 0
            for each in f:
                if k % 2 == 0:
                    k += 1
                    try:
                        kx.append(float(each))
                        continue
                    except:
                        pass
                if k % 2 == 1:
                    k += 1
                    try:
                        ky.append(float(each))
                        continue
                    except:
                        pass
                # print(x)
                # print(y)
                # for px,py in zip(x,y):
                #     if num < maxnum:
                #         ball = circle.Ball(pos, (rand.random(), rand.random()), ballsize, pix[int(px / size),int(py / size)], w, h)
                #         grid[int(pos[0] / size)][int(pos[1] / size)].append(ball)
                #         ball_list.append(ball)
                #         break
                #     break
        # while num < maxnum:
        #     ball = circle.Ball(pos, (0, 0), ballsize, red,w, h)
        #     grid[int(pos[0] / size)][int(pos[1] / size)].append(ball)
        #     ball_list.append(ball)
        #     num += 1
        #     break
        while num < maxnum:
            ball = circle.Ball(pos, (0, 0), ballsize, pix[int(kx[num] / size),int(ky[num] / size)],w, h)
            grid[int(pos[0] / size)][int(pos[1] / size)].append(ball)
            ball_list.append(ball)
            num += 1
            time.sleep(0.01)
            break
        pygame.display.update()

