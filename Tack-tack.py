import wrap

from wrap import  sprite

wrap.world.create_world(1920,900)
wrap.world.set_back_color(0,190,0)


mario=wrap.sprite.add("mario-1-big",800,450,"stand")

@wrap.on_key_always(wrap.K_d,wrap.K_a,delay=10)
def actions_mario(keys):

    x_mario=sprite.get_x(mario)
    y_mario=sprite.get_y(mario)

    if wrap.K_d in keys:
        sprite.move(mario,3,0)
    if wrap.K_a in keys:
        sprite.move(mario,-3,0)


