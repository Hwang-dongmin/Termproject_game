
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
