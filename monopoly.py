import pygame
import time
import random

pygame.init()

#화면 크기 설정
screen_width = 1080
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("추억의 모노폴리")          #화면설정 screen변수로 선언

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
game_info_font = pygame.font.Font(None, 30)

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("bg_monopoly.jpg")

#주사위(sprite)불러오기
dice_1 = pygame.image.load("dice1-001.png")
dice_2 = pygame.image.load("dice2-001.png")
dice_3 = pygame.image.load("dice3-001.png")
dice_4 = pygame.image.load("dice4-001.png")
dice_5 = pygame.image.load("dice5-001.png")
dice_6 = pygame.image.load("dice6-001.png")

# 빌딩(sprite)불러오기
house_1 = pygame.image.load("house_1p-001.png")
house_2 = pygame.image.load("house_2p-001.png")
house_3 = pygame.image.load("house_3p-001.png")
house_4 = pygame.image.load("house_4p-001.png")

building_1 = pygame.image.load("building_1p-001.png")
building_2 = pygame.image.load("building_2p-001.png")
building_3 = pygame.image.load("building_3p-001.png")
building_4 = pygame.image.load("building_4p-001.png")

village_1 = pygame.image.load("building2_1p-001.png")
village_2 = pygame.image.load("building2_2p-001.png")
village_3 = pygame.image.load("building2_3p-001.png")
village_4 = pygame.image.load("building2_4p-001.png")

# 캐릭터(sprite) 불러오기
char_p1 = pygame.image.load("1p-001.png")
char_p2 = pygame.image.load("2p-001.png")
char_p3 = pygame.image.load("3p-001.png")
char_p4 = pygame.image.load("4p-001.png")

char_p1_x_pos = 110             # 화면 가로 위치
char_p1_y_pos = 758             # 화면 세로 위치
char_p2_x_pos = 400
char_p2_y_pos = 210
char_p3_x_pos = 480
char_p3_y_pos = 210
char_p4_x_pos = 560
char_p4_y_pos = 210

#부루마블 지도 좌표
map = {0:(110,758), 1:(191,758), 2:(272,758), 3:(353,758), 4:(434,758), 5:(515,758), 6:(596,758), 7:(677,758),
 8:(758,758), 9:(758,677), 10:(758,596), 11:(758,515), 12:(758,434), 13:(758,353), 14:(758,272), 15:(758,191),
 16:(758,110), 17:(677,110), 18:(596,110), 19:(515,110), 20:(434,110), 21:(353,110), 22:(272,110), 23:(191,110),
 24:(110, 110), 25:(110,191), 26:(110,272), 27:(110,353), 28:(110,434), 29:(110,515), 30:(110,596), 31:(110,677)}

map_building = {0:(110,870), 1:(191,870), 2:(272,870), 3:(353,870), 4:(434,870), 5:(515,870), 6:(596,870), 7:(677,870),
 8:(870,758), 9:(870,677), 10:(870,596), 11:(870,515), 12:(870,434), 13:(870,353), 14:(870,272), 15:(870,191),
 16:(758,10), 17:(677,10), 18:(596,10), 19:(515,10), 20:(434,10), 21:(353,10), 22:(272,10), 23:(191,10),
 24:(10, 110), 25:(10,191), 26:(10,272), 27:(10,353), 28:(10,434), 29:(10,515), 30:(10,596), 31:(10,677)}

map_name = ["START", "SEOUL", "NEW YORK", "?", "TOKYO", "HANOI", "SYDNEY", "KUALA LUMPUR",
            "GO TO JAIL", "NEW DELHI", "KAT MANDU", "MOSCOW", "BEIJING", "HAWAII", "?", "SIEM REAP",
            "FREE PARKING", "ATHEN", "MEXICO CITY", "VENCOUVER", "RIO", "?", "FLORENCE", "BUENOS AIRES",
            "JAIL", "KAIRO", "SANTIAGO", "BERLIN", "?", "PARIS", "BARCELONA", "LONDON"]

random_reward_list = [2000, 5000, 10000, 20000, 30000, -2000, -5000, -10000, -20000, -30000]


map_price = [10000, -10000, -13000, 0, -11000, -4500, -9000, -6000,
             0, -8000, -6000, -7500, -8500, -10000, 0, -5500,
             0, -7500, -7000, -10000, -9000, 0, -10000, -9500,
             -20000, -9000, -9000, -12000, 0, -11500, -10500, -13000]

#플레이어 재산
p1_money = 100000
p2_money = 100000
p3_money = 100000
p4_money = 100000

p1_property = {}
p2_property = {}
p3_property = {}
p4_property = {}

bankrupt_1p = False
bankrupt_2p = False
bankrupt_3p = False
bankrupt_4p = False
sell = False

build_1p = False
build_2p = False
build_3p = False
build_4p = False

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
char_speed = 84

#주사위 생성

dice = 0

free_parking_1p = False
free_parking_2p = False
free_parking_3p = False
free_parking_4p = False

go_to_jail_1p = False
go_to_jail_2p = False
go_to_jail_3p = False
go_to_jail_4p = False

#주사위 결과에 따라 플레이어의 이동거리 계산
p1_move = 0
p2_move = 0
p3_move = 0
p4_move = 0

c1 = 0
c2 = 0
c3 = 0
c4 = 0

players = ["Player 1", "Player 2", "Player 3", "Player 4"]
current_player = players[0]
turn = 1

#이벤트 루프
running = True  #게임이 진행중인가?
info = 1
while running:
    # dt = clock.tick(10)     #게임화면 초당 프레임 수를 설정

    for event in pygame.event.get():    # 어떤 이벤트가 발생했는가? [사용자 event가 들어오는지 확인하는 로직.]
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생했는가?
            running = False             # 게임이 진행중이 아님

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                dice = random.randint(1, 6)

                if turn == 1:
                    p1_move += dice
                    if p1_move >= 32:
                        p1_move -= 32

                    if p1_money < abs(map_price[p1_move]):
                        if p1_money <= 0:
                            p1_money = 0
                            if sum(p1_property.values()) <= 0:
                                bankrupt_1p = True
                                char_p1_x_pos = 320
                                char_p1_y_pos = 210
                        try:
                            returned = p1_property.pop(list(p1_property.keys())[0])
                            p1_money += returned
                        except IndexError:
                            pass

                        sell = True
                        turn = 2
                    else:
                        char_p1_x_pos = map[p1_move][0]
                        char_p1_y_pos = map[p1_move][1]

                        if go_to_jail_1p:
                            p1_move = 24
                            jail_count_1p -= 1
                            if jail_count_1p == 0 or free_parking_1p:
                                go_to_jail_1p = False
                                free_parking_1p = False
                            char_p1_x_pos = map[p1_move][0]
                            char_p1_y_pos = map[p1_move][1]

                        elif p1_move in [3, 14, 21, 28]:
                            draw_reward = random.sample(random_reward_list, 1)
                            p1_money += draw_reward[0]

                        elif p1_move == 8:
                            go_to_jail_1p = True
                            jail_count_1p = 3

                        elif p1_move == 16:
                            free_parking_1p = True

                        elif map_name[p1_move] not in list(p2_property.keys())+list(p3_property.keys())+list(p4_property.keys()):
                            if c1 == 1:
                                build_1p = False
                                p1_money += map_price[p1_move]
                                buliding_1p = building_1
                            elif c1 >= 2:
                                build_1p = False
                                p1_money += map_price[p1_move]
                                buliding_1p = village_1
                            elif c1 == 0:
                                p1_property[map_name[p1_move]] = abs(map_price[p1_move])
                                p1_money += map_price[p1_move]
                                buliding_1p = house_1
                                c1 += 1
                            build_1p = True

                        elif map_name[p1_move] in list(p2_property.keys()):
                            p1_money += map_price[p1_move]
                            p2_money += abs(map_price[p1_move])

                        elif map_name[p1_move] in list(p3_property.keys()):
                            p1_money += map_price[p1_move]
                            p3_money += abs(map_price[p1_move])

                        elif map_name[p1_move] in list(p4_property.keys()):
                            p1_money += map_price[p1_move]
                            p4_money += abs(map_price[p1_move])

                        turn = 2
                    current_player = players[0]

                elif turn == 2:
                    p2_move += dice
                    if p2_move >= 32:
                        p2_move -= 32

                    if p2_money < abs(map_price[p2_move]):
                        if p2_money <= 0:
                            p2_money = 0
                            if sum(p2_property.values()) <= 0:
                                bankrupt_2p = True
                                char_p2_x_pos = 400
                                char_p2_y_pos = 210
                        try:
                            returned = p2_property.pop(list(p2_property.keys())[0])
                            p2_money += returned
                        except IndexError:
                            pass
                        sell = True
                        turn = 3
                    else:
                        char_p2_x_pos = map[p2_move][0]
                        char_p2_y_pos = map[p2_move][1]

                        if go_to_jail_2p:
                            p2_move = 24
                            jail_count_2p -= 1
                            if jail_count_2p == 0 or free_parking_2p:
                                go_to_jail_2p = False
                                free_parking_2p = False
                            char_p2_x_pos = map[p2_move][0]
                            char_p2_y_pos = map[p2_move][1]

                        elif p2_move in [3, 14, 21, 28]:
                            draw_reward = random.sample(random_reward_list, 1)
                            p2_money += draw_reward[0]

                        elif p2_move == 8:
                            go_to_jail_2p = True
                            jail_count_2p = 3

                        elif p2_move == 16:
                            free_parking_2p = True

                        elif map_name[p2_move] not in list(p1_property.keys())+list(p3_property.keys())+list(p4_property.keys()):
                            if c2 == 1:
                                p2_money += map_price[p2_move]
                                buliding_2p = building_2
                                c2 += 1
                            elif c2 >= 2:
                                p2_money += map_price[p2_move]
                                buliding_2p = village_2
                            elif c2 == 0:
                                p2_property[map_name[p2_move]] = abs(map_price[p2_move])
                                p2_money += map_price[p2_move]
                                buliding_2p = house_2
                                c2 += 1
                            build_2p = True
                        elif map_name[p2_move] in list(p1_property.keys()):
                            p2_money += map_price[p2_move]
                            p1_money += abs(map_price[p2_move])
                        elif map_name[p2_move] in list(p3_property.keys()):
                            p2_money += map_price[p2_move]
                            p3_money += abs(map_price[p2_move])
                        elif map_name[p2_move] in list(p4_property.keys()):
                            p2_money += map_price[p2_move]
                            p4_money += abs(map_price[p2_move])

                        turn = 3
                    current_player = players[1]

                elif turn == 3:
                    p3_move += dice
                    if p3_move >= 32:
                        p3_move -= 32

                    if p3_money < abs(map_price[p3_move]):
                        if p3_money <= 0:
                            p3_money = 0
                            if sum(p3_property.values()) <= 0:
                                bankrupt_3p = True
                                char_p3_x_pos = 480
                                char_p3_y_pos = 210
                        try:
                            returned = p3_property.pop(list(p3_property.keys())[0])
                            p3_money += returned
                        except IndexError:
                            pass
                        sell = True
                        turn = 4
                    else:
                        char_p3_x_pos = map[p3_move][0]
                        char_p3_y_pos = map[p3_move][1]

                        if go_to_jail_3p:
                            p3_move = 24
                            jail_count_3p -= 1
                            if jail_count_3p == 0 or free_parking_3p:
                                go_to_jail_3p = False
                                free_parking_3p = False
                            char_p3_x_pos = map[p3_move][0]
                            char_p3_y_pos = map[p3_move][1]

                        elif p3_move in [3, 14, 21, 28]:
                            draw_reward = random.sample(random_reward_list, 1)
                            p3_money += draw_reward[0]

                        elif p3_move == 8:
                            go_to_jail_3p = True
                            jail_count_3p = 3

                        elif p3_move == 16:
                            free_parking_3p = True

                        elif map_name[p3_move] not in list(p2_property.keys())+list(p1_property.keys())+list(p4_property.keys()):
                            if c3 == 1:
                                p3_money += map_price[p3_move]
                                buliding_3p = building_3
                                c3 += 1
                            elif c3 >= 2:
                                p3_money += map_price[p3_move]
                                buliding_3p = village_3
                            elif c3 == 0:
                                p3_property[map_name[p3_move]] = abs(map_price[p3_move])
                                p3_money += map_price[p3_move]
                                buliding_3p = house_3
                                c3 += 1
                            build_3p = True
                        elif map_name[p3_move] in list(p2_property.keys()):
                            p3_money += map_price[p3_move]
                            p2_money += abs(map_price[p3_move])
                        elif map_name[p3_move] in list(p1_property.keys()):
                            p3_money += map_price[p3_move]
                            p1_money += abs(map_price[p3_move])
                        elif map_name[p3_move] in list(p4_property.keys()):
                            p3_money += map_price[p3_move]
                            p4_money += abs(map_price[p3_move])

                        turn = 4
                    current_player = players[2]

                elif turn == 4:
                    p4_move += dice
                    if p4_move >= 32:
                        p4_move -= 32

                    if p4_money < abs(map_price[p4_move]):
                        if p4_money <= 0:
                            p4_money = 0
                            if sum(p4_property.values()) <= 0:
                                bankrupt_4p = True
                                char_p4_x_pos = 560
                                char_p4_y_pos = 210
                        try:
                            returned = p4_property.pop(list(p4_property.keys())[0])
                            p4_money += returned
                        except IndexError:
                            pass
                        sell = True
                        turn = 1
                    else:
                        char_p4_x_pos = map[p4_move][0]
                        char_p4_y_pos = map[p4_move][1]

                        if go_to_jail_4p :
                            p4_move = 24
                            jail_count_4p -= 1
                            if jail_count_4p == 0 or free_parking_4p:
                                go_to_jail_4p = False
                                free_parking_4p = False
                            char_p4_x_pos = map[p4_move][0]
                            char_p4_y_pos = map[p4_move][1]

                        elif p4_move in [3, 14, 21, 28]:
                            draw_reward = random.sample(random_reward_list, 1)
                            p4_money += draw_reward[0]

                        elif p4_move == 8:
                            go_to_jail_4p = True
                            jail_count_4p = 3

                        elif p4_move == 16:
                            free_parking_4p = True

                        elif map_name[p4_move] not in list(p2_property.keys())+list(p3_property.keys())+list(p1_property.keys()):
                            if c4 == 1:
                                p4_money += map_price[p4_move]
                                buliding_4p = building_4
                                c4 += 1
                            elif c4 >= 2:
                                p4_money += map_price[p4_move]
                                buliding_4p = village_4
                            elif c4 == 0:
                                p4_property[map_name[p4_move]] = abs(map_price[p4_move])
                                p4_money += map_price[p4_move]
                                buliding_4p = house_4
                                c4 += 1
                            build_4p = True
                        elif map_name[p4_move] in list(p2_property.keys()):
                            p4_money += map_price[p4_move]
                            p2_money += abs(map_price[p4_move])
                        elif map_name[p4_move] in list(p3_property.keys()):
                            p4_money += map_price[p4_move]
                            p3_money += abs(map_price[p4_move])
                        elif map_name[p4_move] in list(p1_property.keys()):
                            p4_money += map_price[p4_move]
                            p1_money += abs(map_price[p4_move])

                        turn = 1
                    current_player = players[3]

                time.sleep(0.3)

    next_str = game_font.render(str("NEXT"), True, (255, 255, 255))
    bkrt_str = game_info_font.render(str("Not enough money!"), True, (200, 100, 100))

    if turn == 2:
        game_info = game_info_font.render(str(">>> [{}] acquired [{}] at $[{}]".format(current_player,
                                          map_name[p1_move],abs(map_price[p1_move]))), True, (150, 20, 20))
    elif turn == 3:
        game_info = game_info_font.render(str(">>> [{}] acquired [{}] at $[{}]".format(current_player,
                                          map_name[p2_move],abs(map_price[p2_move]))), True, (150, 20, 20))
    elif turn == 4:
        game_info = game_info_font.render(str(">>> [{}] acquired [{}] at $[{}]".format(current_player,
                                          map_name[p3_move],abs(map_price[p3_move]))), True, (150, 20, 20))
    elif turn == 1:
        game_info = game_info_font.render(str(">>> [{}] acquired [{}] at $[{}]".format(current_player,
                                          map_name[p4_move],abs(map_price[p4_move]))), True, (150, 20, 20))

    p1_total_money = game_info_font.render(str("P1 : {}".format(p1_money)), True, (150, 20, 20))
    p2_total_money = game_info_font.render(str("P2 : {}".format(p2_money)), True, (150, 250, 150))
    p3_total_money = game_info_font.render(str("P3 : {}".format(p3_money)), True, (150, 150, 250))
    p4_total_money = game_info_font.render(str("P4 : {}".format(p4_money)), True, (20, 20, 250))

    screen.blit(background, (0, 0))                         # 배경 그리기
    screen.blit(char_p1, (char_p1_x_pos, char_p1_y_pos))    # 플레이어1 그리기
    screen.blit(char_p2, (char_p2_x_pos, char_p2_y_pos))    # 플레이어2 그리기
    screen.blit(char_p3, (char_p3_x_pos, char_p3_y_pos))    # 플레이어3 그리기
    screen.blit(char_p4, (char_p4_x_pos, char_p4_y_pos))    # 플레이어4 그리기
    screen.blit(next_str, (350, 665))

    screen.blit(p1_total_money, (220, 430))
    screen.blit(p2_total_money, (220, 455))
    screen.blit(p3_total_money, (220, 480))
    screen.blit(p4_total_money, (220, 505))




    if build_1p:
        for i in list(p1_property.keys()):
            screen.blit(buliding_1p,(map_building[map_name.index(i)][0],
                                     map_building[map_name.index(i)][1]))
        screen.blit(game_info, (310, 220))
    if build_2p:
        for i in list(p2_property.keys()):
            screen.blit(buliding_2p,(map_building[map_name.index(i)][0],
                                     map_building[map_name.index(i)][1]))
        screen.blit(game_info, (310, 220))
    if build_3p:
        for i in list(p3_property.keys()):
            screen.blit(buliding_3p,(map_building[map_name.index(i)][0],
                                     map_building[map_name.index(i)][1]))
        screen.blit(game_info, (310, 220))
    if build_4p:
        for i in list(p4_property.keys()):
            screen.blit(buliding_4p,(map_building[map_name.index(i)][0],
                                     map_building[map_name.index(i)][1]))
        screen.blit(game_info, (310, 220))

    if bankrupt_1p == True:
        screen.blit(bkrt_str,(310, 250))
    if bankrupt_2p == True:
        screen.blit(bkrt_str,(310, 250))
    if bankrupt_3p == True:
        screen.blit(bkrt_str,(310, 250))
    if bankrupt_4p == True:
        screen.blit(bkrt_str,(310, 250))

    if dice == 1:
        screen.blit(dice_1, (300, 650))
    elif dice == 2:
        screen.blit(dice_2, (300, 650))
    elif dice == 3:
        screen.blit(dice_3, (300, 650))
    elif dice == 4:
        screen.blit(dice_4, (300, 650))
    elif dice == 5:
        screen.blit(dice_5, (300, 650))
    elif dice == 6:
        screen.blit(dice_6, (300, 650))
    # dice = dice_next

    pygame.display.update()             # 게임화면 다시 그리기(필수)

# pygame QUIT
pygame.quit