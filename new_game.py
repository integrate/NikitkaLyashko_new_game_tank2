import wrap
import wrap_py.wrap_base
from wrap import sprite

wrap.world.create_world(1000,1000)


green_enemy_tank=wrap.sprite.add("battle_city_tanks",100,100,"tank_enemy_size1_green1")
purple_tank_enemy=wrap.sprite.add("battle_city_tanks",900,100,"tank_enemy_size1_purple1")
yellow_tank=wrap.sprite.add("battle_city_tanks",500,500,"tank_enemy_size2_yellow1")

wrap.sprite.set_reverse_y(green_enemy_tank,True)
wrap.sprite.set_reverse_y(purple_tank_enemy,True)


def is_collide_sprite(id1,id2):
    top1=sprite.get_top(id1)-2
    bottom1=sprite.get_bottom(id1)+2
    right1=sprite.get_right(id1)+2
    left1=sprite.get_left(id1)-2

    top2=sprite.get_top(id2)
    bottom2=sprite.get_bottom(id2)
    right2=sprite.get_right(id2)
    left2=sprite.get_left(id2)


    if (top2<=bottom1 and top2>=top1) or (bottom2<=bottom1 and bottom2>=top1) or\
        (top1<=bottom2 and top1>=top2) or (bottom1>=top2 and bottom1<=bottom2):

        y=True
    else:
        y=False

    if (left1>=left2 and left1<=right2) or (right1>=left2 and right1<=right2) or \
            (right2>=left1 and right2<=right1) or (left2>=left1 and left2<=right1):
        x=True
    else:
        x=False

    if x==True and y==True:
        return True
    else:
        return False



# W__________________________
@wrap.on_key_always(wrap.K_w,wrap.K_a,wrap.K_s,wrap.K_d,delay=10)
def actions_yellow_tank_W (keys):

    x_our_tank=sprite.get_x(yellow_tank)
    y_our_tank=sprite.get_y(yellow_tank)



    costum_tank=sprite.get_costume(yellow_tank)
    if costum_tank=="tank_enemy_size2_yellow1":
        sprite.set_costume(yellow_tank,"tank_enemy_size2_yellow2")
    else:
        sprite.set_costume(yellow_tank,"tank_enemy_size2_yellow1")


    if wrap.K_w in keys:
        sprite.move(yellow_tank,0,-3)
        sprite.set_angle(yellow_tank,0)


    elif wrap.K_a in keys:
        sprite.move(yellow_tank,-3,0)
        sprite.set_angle(yellow_tank,270)

    elif wrap.K_s in keys:
        sprite.move(yellow_tank,0,3)
        sprite.set_angle(yellow_tank,180)

    elif wrap.K_d in keys:
        sprite.move(yellow_tank,3,0)
        sprite.set_angle(yellow_tank,90)

    collide_our=is_collide_sprite(yellow_tank,green_enemy_tank)
    if collide_our==True:
        sprite.move_to(yellow_tank,x_our_tank,y_our_tank)

    collide_our = is_collide_sprite(yellow_tank, purple_tank_enemy)
    if collide_our == True:
        sprite.move_to(yellow_tank, x_our_tank, y_our_tank)


#Если осb X совпали, тогда вражеский танк доложен ехать по направлению к нашему танку по оси Y, до тех пор пока не доедет до границы в 100px.
#Если осb y совпали, тогда вражеский танк доложен ехать по направлению к нашему танку по оси x, до тех пор пока не доедет до границы в 100px.
#Если оси не совпадют, тогда вражеский танк должен ехать по направлению к нашему танку по оси У.


def enemy_tank(id):

    x_our_tank = sprite.get_x(yellow_tank)
    y_our_tank = sprite.get_y(yellow_tank)

    x_enemy = sprite.get_x(id)
    y_enemy = sprite.get_y(id)

    if y_our_tank!=y_enemy and x_our_tank!=x_enemy and y_our_tank>y_enemy:
        sprite.set_angle(id,180)
        sprite.move(id,0,1)

    if y_our_tank!=y_enemy and x_our_tank!=x_enemy and y_enemy>y_our_tank:
        sprite.set_angle(id,0)
        sprite.move(id,0,-1)

    if y_our_tank==y_enemy:
        if x_our_tank>x_enemy+100:
            sprite.set_angle(id, 90)
            sprite.move(id,1,0)
        if x_our_tank<x_enemy-100:
            sprite.set_angle(id, 270)
            sprite.move(id,-1,0)
    if x_our_tank==x_enemy:
        if y_our_tank>y_enemy+100:

            sprite.move(id,0,1)
        if y_our_tank<y_enemy-100:
            sprite.move(id,0,-1)

    enemy_enemy=is_collide_sprite(green_enemy_tank,purple_tank_enemy)
    if enemy_enemy==True:
        sprite.move_to(id,x_enemy,y_enemy)


    collide_enemy=is_collide_sprite(id,yellow_tank)
    # print(y_our_tank,y_enemy,collide_enemy,collide_1)
    if collide_enemy==True:
        sprite.move_to(id,x_enemy,y_enemy)




@wrap.always(delay=8)
def begin_tank():
    enemy_tank(green_enemy_tank)


@wrap.always(delay=6)
def begin_tank_purple():
    enemy_tank(purple_tank_enemy)
























    











