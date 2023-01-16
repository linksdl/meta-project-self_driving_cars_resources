#coding=utf-8
import pygame
from pygame.locals import *
import sys
BLACK =(0,0,0)
WHITE = (255,255,255)

SCREEN_SIZE = [320,400]#屏幕大小
BAR_SIZE = [20,5]#挡板大小
BALL_SIZE = [15,15]#球的尺寸

class Game(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()#定时器
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Simple Game')

        self.ball_pos_x = SCREEN_SIZE[0]//2 - BALL_SIZE[0]/2
        self.ball_pos_y = SCREEN_SIZE[1]//2 - BALL_SIZE[1]/2
        #ball 移动方向
        self.ball_dir_x = -1 #-1:left 1:right
        self.ball_dir_y = -1# -1:up

        self.ball_pos = pygame.Rect(self.ball_pos_x,self.ball_pos_y,BALL_SIZE[0],BALL_SIZE[1])

        self.score =0
        self.bar_pos_x = SCREEN_SIZE[0]//2 - BAR_SIZE[0]//2
        self.bar_pos = pygame.Rect(self.bar_pos_x,SCREEN_SIZE[1]-BAR_SIZE[1],BAR_SIZE[0],BALL_SIZE[1])

    def bar_move_left(self):#左移
        self.bar_pos_x = self.bar_pos_x - 2

    def bar_move_right(self):
        self.bar_pos_x = self.bar_pos_x + 2

    def run(self):
        pygame.mouse.set_visible(0) #移动鼠标不可见
        bar_move_left =False
        bar_move_right = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()#接收到退出事件后退出程序

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:#鼠标左键按下
                    bar_move_left = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #左键弹起
                    bar_move_left = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:#右键
                    bar_move_right = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # 左键弹起
                    bar_move_right = False

            if bar_move_left == True and bar_move_right ==False:
                self.bar_move_left()
            if bar_move_left == False and bar_move_right == True:
                self.bar_move_right()

            self.screen.fill(BLACK)
            self.bar_pos.left = self.bar_pos_x
            pygame.draw.rect(self.screen, WHITE, self.bar_pos)

            self.bar_pos.left += self.ball_dir_x * 2
            self.ball_pos.bottom += self.ball_dir_y * 3
            pygame.draw.rect(self.screen, WHITE, self.ball_pos)

            if self.ball_pos.top <= 0 or self.ball_pos.bottom >= (SCREEN_SIZE[1]- BAR_SIZE[1] + 1):
                self.ball_dir_y =self.ball_dir_y * -1
            if self.ball_pos.left <=0 or self.ball_pos.right >= (SCREEN_SIZE[0]):
                self.ball_dir_x = self.ball_dir_x * -1

            if self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left < self.ball_pos.right and self.bar_pos.right > self.ball_pos.left):
                self.score += 1
                print("Score: ", self.score, end='\r')
            elif self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left > self.ball_pos.right or self.bar_pos.right < self.ball_pos.left):
                print("Game Over: ", self.score)
                return self.score

            pygame.display.update()#更新软件界面显示
            self.clock.tick(60)
game = Game()
game.run()#启动