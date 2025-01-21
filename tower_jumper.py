import random

import pygame


knight_x, knight_y = 200, 400
direction_k = 'l'
menu = True
at = False
anim = 0
attack = 0
clock = pygame.time.Clock()

bg = []
upp = 0

game = True
screen = pygame.display.set_mode((3000, 1800), pygame.FULLSCREEN)
stand_left = pygame.image.load("sprites/knight/idol/left/knight_standing(left).png").convert_alpha()
stand_left = pygame.transform.scale(stand_left, (160, 160))
stand_right = pygame.image.load("sprites/knight/idol/right/knight_standing(right).png").convert_alpha()
stand_right = pygame.transform.scale(stand_right, (160, 160))
fall_left = pygame.image.load("sprites/knight/falling/left/knight_falling(left).png").convert_alpha()
fall_left = pygame.transform.scale(fall_left, (160, 160))
fall_right = pygame.image.load("sprites/knight/falling/right/knight_falling(right).png").convert_alpha()
fall_right = pygame.transform.scale(fall_right, (160, 160))

bg_s = []
walk_left = []
walk_right = []
attack_left = []
attack_right = []

for i in range(1, 9):
    walk_left.append(pygame.transform.scale(pygame.image.load(f"sprites/knight/walk/left/knight_walking(left){i}.png"),
                                            (160, 160)))
    walk_right.append(pygame.transform.scale(pygame.image.load(f"sprites/knight/walk/right/knight_walking(right){i}."
                                                               f"png"), (160, 160)))
for i in range(1, 11):
    attack_left.append((pygame.transform.scale(pygame.image.load(f"sprites/knight/attack/left/knight_attack(left){i}."
                                                                 f"png"), (160, 160))))
    attack_right.append((pygame.transform.scale(pygame.image.load(f"sprites/knight/attack/right/knight_attack(right){i}"
                                                                  f".png"), (160, 160))))
for i in range(1, 8):
    bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{i}.png"), (160, 160)))

bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{1}.png"), (160, 160)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{2}.png"), (160, 160)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{5}.png"), (160, 160)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{6}.png"), (160, 160)))
bg_s.append(pygame.transform.scale(pygame.image.load(f"sprites/bg/wall{8}.png"), (160, 160)))


class knight():
    def __init__(self, anim, attack):
        self.anim = anim
        self.attack = attack

    def move(self):
        global knight_x, direction_k, knight_y, upp
        if upp != 0:
            pass

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (not keys[pygame.K_RIGHT] and not keys[pygame.K_d]):
            knight_x -= 20
            screen.blit(walk_left[self.anim], (knight_x, knight_y))
            direction_k = 'l'

        if (not keys[pygame.K_LEFT] and not keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            knight_x += 20
            screen.blit(walk_right[self.anim], (knight_x, knight_y))
            direction_k = 'r'

        if ((not keys[pygame.K_LEFT] and not keys[pygame.K_a] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d]) or
                ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]))):
            if direction_k == 'l':
                screen.blit(stand_left, (knight_x, knight_y))
            if direction_k == 'r':
                screen.blit(stand_right, (knight_x, knight_y))

    def attacking(self):
        global at, knight_x, knight_y, direction_k
        if keys[pygame.K_z] or keys[pygame.K_SPACE]:
            at = True

    def create_bagraund(self):
        global bg
        bg = []
        for i in range(0, 1800, 160):
            for z in range(0, 4000, 160):
                bg.append((random.choice(bg_s), i, z))

    def bagraund(self):
        global bg
        for i in range(len(bg)):
            screen.blit(bg[i][0], (bg[i][1], bg[i][2]))

ng = 0


while game:
    keys = pygame.key.get_pressed()
    clock.tick(30)
    screen.fill('black')
    if menu:
        if anim == 7:
            anim = 0
        else:
            anim += 1

        knight_ = knight(anim, attack)
        if ng == 0:
            knight_.create_bagraund()
            ng = 1

        knight_.bagraund()

        if not at:
            knight_.move()

        if at:
            attack += 1
            if direction_k == 'l':
                screen.blit(attack_left[attack], (knight_x, knight_y))
            elif direction_k == 'r':
                screen.blit(attack_right[attack], (knight_x, knight_y))

        if attack == 9:
            attack = 0
            at = False

        knight_.attacking()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
