import pygame
import time
from random import randint
from pygame.locals import *
from image_load import *

#죽었을때 애니메이션 추가, 코드 수정 -> 적 클래스 여러개 만들기/ 렉 해결안됨 -> 렉해결( 이미지 미리 불러오기 )
#플레이어 생명력은 3칸, 공격 받을 때마다 달 부서지기

# 2 - Initialize the game   
pygame.init()
width, height = 960, 576
screen=pygame.display.set_mode((width, height))
start_time = time.time()

# 3 - Load images
background = pygame.image.load("resources/images/player/background.png")
player = pygame.image.load("resources/images/player/player.png")

t = 0
dir_left = 0
dir_right = 1
dir_top_left = 2
dir_top_right = 3
player_attacked = False
player_att_dir = dir_left
player_att_cool = 20 # 30fps , 1 sec
player_att_cool_tmp = 0
player_att_ready = True
player_att_on_dir = -1 # -1 : non , 0:l,1:r,2:l_t,3:r_t
tmp_up_pressed = False # UP키가 눌렸는가?
screen_shake = 0 #화면 흔들기
player_life = 50



class enemy1(pygame.sprite.Sprite):
    # att_dir = -1
    
    def __init__(self,att_dir): # top_left or right
        super(enemy1, self).__init__()
        global tmp_images
        self.images = enemy1_images
        
        #index value to get the image from the array
        #initially it is 0 
        
        self.index = 0
        self.att_dir = att_dir
        if att_dir == dir_left :#image flip 여부 결정하는 dir_bool
            self.att_dir_bool = True #left
        else:
            self.att_dir_bool = False
        self.alive =1
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.alive][self.index].convert_alpha()

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(0, 0, 960, 576)
        
    def update(self):
        global player_att_ready
        global player_att_on_dir
        global screen_shake
        global player_life
        global player_attacked
        #when the update method is called, we will increment the index
        self.index += 1
        
        #if the index is larger than the total images
        if self.index >= 26 and self.index <= 29:
            if player_att_on_dir == self.att_dir:
                player_att_ready = True #재공격 활성
                #enemy_att_group.remove(self) # 공격받으면 피해 애니메이션 전환, 자금은 그냥 삭제
                player_att_on_dir = -1 #공격 온 초기화
                self.alive = 0
                self.index = 0
                pygame.time.delay(30)
                screen_shake = 5
                
                return
            
        if self.index == 30:
            
            player_attacked = True
            player_life -= 1
            pygame.time.delay(30)
            screen_shake = 5

                
        if self.alive == 1:
            if self.index == len(self.images[1]): # 애니메이션 끝나면 삭제(삶)
                #we will make the index to 0 again
                self.alive = False
                #self.index = 0
                enemy_att_group.remove(self) #죽음 에니메이션 전환
            
                return
        else:
            if self.index == len(self.images[0]): # 애니메이션 끝나면 삭제(죽음)
                #we will make the index to 0 again

                #self.index = 0 초기화
                enemy_att_group.remove(self)
            
                return
        #finally we will update the image that will be displayed

        #if self.alive == True:
        self.image = pygame.transform.flip(self.images[self.alive][self.index].convert_alpha(),self.att_dir_bool,False) # 함수 밖의 fixed_dir값을 참조함 씨발. 클래스 내에 고정 값 못만드나?? -> 가능함 (self.~)
        # else:
        #     self.image = self.images[self.att_dir_bool][self.index].convert_alpha()

class enemy2(pygame.sprite.Sprite):
    # att_dir = -1
    
    def __init__(self,att_dir):
        super(enemy2, self).__init__()
        global tmp_images
        self.images = enemy2_images
        
        #index value to get the image from the array
        #initially it is 0 
        
        self.index = 0
        self.att_dir = att_dir
        if att_dir == dir_left :#image flip 여부 결정하는 dir_bool
            self.att_dir_bool = True #left
            self.att_dir = dir_left
        else:
            self.att_dir_bool = False
            self.att_dir = dir_right
        self.alive =1
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.alive][self.index].convert_alpha()

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(0, 0, 960, 576)
        
    def update(self):
        global player_att_ready
        global player_att_on_dir
        global screen_shake
        global player_life
        global player_attacked
        #when the update method is called, we will increment the index
        self.index += 1
        
        #if the index is larger than the total images
        if self.index >= 26 and self.index <= 29:
            if player_att_on_dir == self.att_dir:
                player_att_ready = True # 재공격 활성
                #enemy_att_group.remove(self) # 공격받으면 피해 애니메이션 전환, 자금은 그냥 삭제
                player_att_on_dir = -1# 공격 온 초기화
                self.alive = 0
                self.index = 0
                pygame.time.delay(30)
                screen_shake = 5
                
                return
        if self.index == 30:
            player_attacked = True
            player_life -= 1
            pygame.time.delay(30)
            screen_shake = 5
                
        if self.alive == 1:
            if self.index == len(self.images[1]): # 애니메이션 끝나면 삭제(삶)
                #we will make the index to 0 again
                self.alive = False
                #self.index = 0
                enemy_att_group.remove(self) #죽음 에니메이션 전환
            
                return
        else:
            if self.index == len(self.images[0]): # 애니메이션 끝나면 삭제(죽음)
                #we will make the index to 0 again

                #self.index = 0 초기화
                enemy_att_group.remove(self)
            
                return
        #finally we will update the image that will be displayed

        #if self.alive == True:
        self.image = pygame.transform.flip(self.images[self.alive][self.index].convert_alpha(),self.att_dir_bool,False) # 함수 밖의 fixed_dir값을 참조함 씨발. 클래스 내에 고정 값 못만드나?? -> 가능함 (self.~)
        # else:
        #     self.image = self.images[self.att_dir_bool][self.index].convert_alpha()

class enemy3(pygame.sprite.Sprite):
    # att_dir = -1
    
    def __init__(self,att_dir):
        super(enemy3, self).__init__()
        global tmp_images
        self.images = enemy3_images
        
        #index value to get the image from the array
        #initially it is 0 
        
        self.index = 0
        self.att_dir = att_dir
        if att_dir == dir_left :#image flip 여부 결정하는 dir_bool
            self.att_dir_bool = True #left
            self.att_dir = dir_top_left
        else:
            self.att_dir_bool = False
            self.att_dir = dir_top_right
        self.alive =1
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.alive][self.index].convert_alpha()

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(0, 0, 960, 576)
        
    def update(self):
        global player_att_ready
        global player_att_on_dir
        global screen_shake
        global player_life
        global player_attacked
        #when the update method is called, we will increment the index
        self.index += 1
        
        #if the index is larger than the total images
        if self.index >= 19 and self.index <= 22:
            if player_att_on_dir == self.att_dir:
                player_att_ready = True # 재공격 활성
                #enemy_att_group.remove(self) # 공격받으면 피해 애니메이션 전환, 자금은 그냥 삭제
                player_att_on_dir = -1# 공격 온 초기화
                self.alive = 0
                self.index = 0
                pygame.time.delay(30)
                screen_shake = 5
                
                return
            
        if self.index == 23:
            
            player_attacked = True
            player_life -= 1
            pygame.time.delay(30)
            screen_shake = 5
                
        if self.alive == 1:
            if self.index == len(self.images[1]): # 애니메이션 끝나면 삭제(삶)
                #we will make the index to 0 again
                self.alive = False
                #self.index = 0
                enemy_att_group.remove(self) #죽음 에니메이션 전환
            
                return
        else:
            if self.index == len(self.images[0]): # 애니메이션 끝나면 삭제(죽음)
                #we will make the index to 0 again

                #self.index = 0 초기화
                enemy_att_group.remove(self)
            
                return
        #finally we will update the image that will be displayed

        #if self.alive == True:
        self.image = pygame.transform.flip(self.images[self.alive][self.index].convert_alpha(),self.att_dir_bool,False) # 함수 밖의 fixed_dir값을 참조함 씨발. 클래스 내에 고정 값 못만드나?? -> 가능함 (self.~)
        # else:
        #     self.image = self.images[self.att_dir_bool][self.index].convert_alpha()


class PlayerAttack(pygame.sprite.Sprite):
    def __init__(self,dir):
        super(PlayerAttack, self).__init__()
        #adding all the images to sprite array
        self.images = player_att_images #image flip으로 수정하기;;
        self.fixed_dir = dir
        #index value to get the image from the array
        #initially it is 0 
        self.att_dir_bool = False #image flip
        self.index = 0
        self.att_dir_top = 0 #top_att == 1
        if self.fixed_dir == 0 :#image flip 여부 결정하는 dir_bool
            self.att_dir_bool = False #left
            self.att_dir_top = 0
        elif self.fixed_dir == 1:
            self.att_dir_bool = True
            self.att_dir_top = 0
        elif self.fixed_dir == 2:
            self.att_dir_bool = False
            self.att_dir_top = 1
        elif self.fixed_dir == 3:
            self.att_dir_bool = True
            self.att_dir_top = 1
 
        #now the image that we will display will be the index from the image array 
        self.image = pygame.transform.flip(self.images[self.att_dir_top][0].convert_alpha(),self.att_dir_bool,False)

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(0, 0, 960, 576)
        
        

    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1
        #if the index is larger than the total images
        if self.index >= len(self.images[self.att_dir_top]):
            #we will make the index to 0 again
            player_att_group.remove(self)
            return
        #if self.index >= 3:#두 틱만 공격 활성화
            
            #player_att_on_dir = -1
        #finally we will update the image that will be displayed
        # self.image = self.images[self.fixed_dir][self.index] # 함수 밖의 fixed_dir값을 참조함 씨발. 클래스 내에 고정 값 못만드나??
        self.image = pygame.transform.flip(self.images[self.att_dir_top][self.index].convert_alpha(),self.att_dir_bool,False)

class MoonAttacked(pygame.sprite.Sprite):
    def __init__(self):
        super(MoonAttacked, self).__init__()
        print(len(moon_attacked))
        self.images = moon_attacked 
        self.index = 0 
        self.image = self.images[0].convert_alpha()
        self.rect = pygame.Rect(0, 0, 960, 576)
        
    def update(self):
        global player_attacked
        
        if player_attacked == True:
            self.index += 1
            
            if self.index == 7:
                player_attacked = False
            if self.index == 14:
                player_attacked = False
            if self.index == 21:
                player_attacked = False
            if self.index == 28:
                player_attacked = False
            if self.index >= 29:
                pygame.quit()
                exit()
        self.image = self.images[self.index ].convert_alpha()



screen = pygame.display.set_mode((960,576))
moon_attacked_group = pygame.sprite.RenderPlain()
moon_attack = MoonAttacked()
moon_attacked_group.add(moon_attack)

player_att_group = pygame.sprite.RenderPlain()
enemy_att_group = pygame.sprite.RenderPlain()
clock = pygame.time.Clock()
# 4 - keep looping through
while 1:
    
    
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0,0))
    screen.blit(player, (0,0))
    # 7 - update the screen
    # 8 - loop through the events
    keys = pygame.key.get_pressed() #다중키 입력 받기
    if keys[pygame.K_UP]:
        if keys[pygame.K_LEFT]:
            player_att_dir = dir_top_left
        if keys[pygame.K_RIGHT]:
            player_att_dir = dir_top_right
    else:
        if keys[pygame.K_LEFT]:
            player_att_dir = dir_left
        if keys[pygame.K_RIGHT]:
            player_att_dir = dir_right

    if player_life <= 0:
        pygame.quit() 
        exit(0)
    
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a: # 적1 생성
                enemy = enemy1(0)
                enemy_att_group.add(enemy)
            if event.key == pygame.K_s: # 적1 생성
                enemy = enemy2(0)
                enemy_att_group.add(enemy)
            if event.key == pygame.K_d: # 적1 생성
                enemy = enemy3(0)
                enemy_att_group.add(enemy)
            if event.key == pygame.K_q: # 적1 생성
                enemy = enemy1(1)
                enemy_att_group.add(enemy)
            if event.key == pygame.K_w: # 적1 생성
                enemy = enemy2(1)
                enemy_att_group.add(enemy)
            if event.key == pygame.K_e: # 적1 생성
                enemy = enemy3(1)
                enemy_att_group.add(enemy)
                
            if event.key == pygame.K_UP:
                tmp_up_pressed = True
            # if tmp_up_pressed == True:
            #     if event.key == pygame.K_LEFT:
            #         player_att_dir = dir_top_left
            #     elif event.key == pygame.K_RIGHT:
            #         player_att_dir = dir_top_right
            # else:
            #     if event.key == pygame.K_LEFT:
            #         player_att_dir = dir_left
            #     elif event.key == pygame.K_RIGHT:
            #         player_att_dir = dir_right
                    
            if event.key == pygame.K_SPACE and player_att_ready == True: #공격 실행
                player_att = PlayerAttack(player_att_dir)#my_sprite를 리스트로 만들어서 여러개 저장,for문 이용 이때 mygroup도 for문으로 초기화시키기
                player_att_group.add(player_att)
                player_att_ready = False
                player_att_cool_tmp = 0
                
                player_att_on_dir = player_att_dir
                
        if event.type == pygame.KEYUP: #UP키 뗄경우
            if event.key == pygame.K_UP:
                tmp_up_pressed = False
                player_att_dir -= 2
    
    
    
    small_font = pygame.font.SysFont(None, 36)
    remain_time = int(time.time()-start_time)
    remain_time_image = small_font.render('Time {}'.format(remain_time), True, (255,255,0))
 
    screen.blit(remain_time_image, (10, 10))
 
    moon_attacked_group.update()
    moon_attacked_group.draw(screen)
    player_att_group.update()
    player_att_group.draw(screen)
    enemy_att_group.update()
    enemy_att_group.draw(screen)
    
#    pygame.time.set_timer(player_att_ready = True , 1000)
    if player_att_ready == False: # 준비중, 쿨타임 돌리
       player_att_cool_tmp += 1
       if player_att_cool_tmp >= 3:
           player_att_on_dir = -1
       if player_att_cool_tmp >= player_att_cool:
            player_att_cool_tmp = 0
            player_att_ready = True
    else:
        player_att_cool_tmp = 0 #when the paring success, reset tmp

    render_offset = [0,0] #화면 흔들기
    if screen_shake > 0 : 
        screen_shake -=1 
        render_offset[0] = randint(0,5) - 2.5
        render_offset[1] = randint(0,5) - 2.5


    screen.blit(screen,render_offset)
    pygame.display.flip()
    clock.tick(30)